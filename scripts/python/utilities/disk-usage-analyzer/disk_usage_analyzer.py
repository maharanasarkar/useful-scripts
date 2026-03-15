import os
import threading
import tkinter as tk
from tkinter import ttk, messagebox
from queue import Queue, Empty
import subprocess
import shutil
from pathlib import Path

TOP_ITEMS = 40
DEFAULT_DRIVE = "C:\\"


def format_size(size):
    """Convert bytes to human-readable format."""
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} PB"


def safe_scandir(path):
    """Safely scan directory, returning empty list on error."""
    try:
        return list(os.scandir(path))
    except (PermissionError, OSError, FileNotFoundError):
        return []


def get_folder_size(path):
    """Calculate total size and file count for a directory."""
    total = 0
    files = 0
    stack = [path]

    while stack:
        current = stack.pop()

        for entry in safe_scandir(current):
            try:
                if entry.is_file(follow_symlinks=False):
                    total += entry.stat().st_size
                    files += 1
                elif entry.is_dir(follow_symlinks=False):
                    stack.append(entry.path)
            except (PermissionError, OSError, FileNotFoundError):
                pass

    return total, files


class DiskAnalyzer:
    """GUI application for analyzing disk usage."""

    def __init__(self, root):
        self.root = root
        self.queue = Queue()
        self.stop_flag = False
        self.scanning = False

        root.title("Advanced Disk Usage Analyzer")
        root.geometry("1100x700")
        root.minsize(800, 500)

        self._create_widgets()
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.process_queue()

    def _create_widgets(self):
        """Create and layout all GUI widgets."""
        toolbar = ttk.Frame(self.root)
        toolbar.pack(fill="x", side="top")

        drive_frame = ttk.Frame(toolbar)
        drive_frame.pack(side="left", padx=10, pady=10)

        ttk.Label(drive_frame, text="Drive:").pack(side="left")

        self.drive_var = tk.StringVar(value="C:")
        self.drive_combo = ttk.Combobox(
            drive_frame,
            textvariable=self.drive_var,
            values=self._get_available_drives(),
            width=5,
            state="readonly",
        )
        self.drive_combo.pack(side="left", padx=5)

        self.scan_btn = ttk.Button(toolbar, text="Scan Drive", command=self.start_scan)
        self.scan_btn.pack(side="left", padx=5)

        self.stop_btn = ttk.Button(
            toolbar, text="Stop", command=self.stop_scan, state="disabled"
        )
        self.stop_btn.pack(side="left", padx=5)

        self.progress = ttk.Progressbar(toolbar, length=300, mode="indeterminate")
        self.progress.pack(side="left", padx=10)

        columns = ("size", "files", "path")
        self.tree = ttk.Treeview(self.root, columns=columns, show="tree headings")

        self.tree.heading("#0", text="Folder")
        self.tree.heading("size", text="Size")
        self.tree.heading("files", text="Files")
        self.tree.heading("path", text="Path")

        self.tree.column("#0", width=250)
        self.tree.column("size", width=120)
        self.tree.column("files", width=80)
        self.tree.column("path", width=450)

        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(fill="both", expand=True, side="left")
        scrollbar.pack(fill="y", side="right")

        self.tree.bind("<<TreeviewOpen>>", self.expand_node)
        self.tree.bind("<Button-3>", self.right_click)

        self.status = ttk.Label(self.root, text="Ready", relief="sunken", anchor="w")
        self.status.pack(fill="x", side="bottom")

    def _get_available_drives(self):
        """Get list of available drives on Windows."""
        drives = []
        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            drive = f"{letter}:\\"
            if os.path.exists(drive):
                drives.append(letter + ":")
        return drives if drives else ["C:"]

    def start_scan(self):
        """Start the disk scanning process."""
        if self.scanning:
            return

        self.scanning = True
        self.stop_flag = False

        self.scan_btn.config(state="disabled")
        self.stop_btn.config(state="normal")
        self.progress.start(10)

        for item in self.tree.get_children():
            self.tree.delete(item)

        thread = threading.Thread(target=self.scan_drive, daemon=True)
        thread.start()

    def stop_scan(self):
        """Stop the current scan."""
        self.stop_flag = True

    def scan_drive(self):
        """Scan the selected drive and calculate folder sizes."""
        root_path = self.drive_var.get() + "\\"

        if not os.path.exists(root_path):
            self.queue.put(("error", f"Drive {root_path} does not exist"))
            self.queue.put(("done",))
            return

        folders = []
        scanned = 0

        for entry in safe_scandir(root_path):
            if self.stop_flag:
                return

            if entry.is_dir():
                size, files = get_folder_size(entry.path)
                folders.append((entry.path, size, files))
                scanned += 1
                self.queue.put(("log", f"Scanned {scanned} folders..."))

        folders.sort(key=lambda x: x[1], reverse=True)

        for folder, size, files in folders[:TOP_ITEMS]:
            self.queue.put(("insert", folder, size, files))

        self.queue.put(("done",))

    def process_queue(self):
        """Process messages from the scanning thread."""
        try:
            while True:
                msg = self.queue.get_nowait()

                if msg[0] == "insert":
                    path, size, files = msg[1], msg[2], msg[3]
                    node = self.tree.insert(
                        "",
                        "end",
                        text=os.path.basename(path) or path,
                        values=(format_size(size), files, path),
                    )
                    self.tree.insert(node, "end", text="Loading...")

                elif msg[0] == "log":
                    self.status.config(text=msg[1])

                elif msg[0] == "done":
                    self.progress.stop()
                    self.scanning = False
                    self.scan_btn.config(state="normal")
                    self.stop_btn.config(state="disabled")
                    self.status.config(text="Scan complete")

                elif msg[0] == "error":
                    messagebox.showerror("Error", msg[1])
                    self.progress.stop()
                    self.scanning = False

        except Empty:
            pass

        self.root.after(100, self.process_queue)

    def expand_node(self, event):
        """Expand a tree node to show subdirectories."""
        node = self.tree.focus()
        item_data = self.tree.item(node)

        if not item_data["values"]:
            return

        path = item_data["values"][2]
        children = self.tree.get_children(node)

        if children:
            self.tree.delete(children[0])

        folders = []
        for entry in safe_scandir(path):
            if entry.is_dir():
                size, files = get_folder_size(entry.path)
                folders.append((entry.path, size, files))

        folders.sort(key=lambda x: x[1], reverse=True)

        for folder, size, files in folders[:TOP_ITEMS]:
            child = self.tree.insert(
                node,
                "end",
                text=os.path.basename(folder),
                values=(format_size(size), files, folder),
            )
            self.tree.insert(child, "end", text="Loading...")

    def right_click(self, event):
        """Show context menu on right-click."""
        item = self.tree.identify_row(event.y)

        if not item:
            return

        path = self.tree.item(item)["values"]

        if not path:
            return

        path = path[2]

        menu = tk.Menu(self.root, tearoff=0)

        menu.add_command(
            label="Open in Explorer",
            command=lambda: subprocess.Popen(f'explorer "{path}"'),
        )

        menu.add_command(
            label="Open in Terminal",
            command=lambda: subprocess.Popen(
                f'start cmd /K "cd /d {path}"', shell=True
            ),
        )

        menu.add_separator()

        menu.add_command(label="Delete", command=lambda: self.delete_path(path))

        menu.post(event.x_root, event.y_root)

    def delete_path(self, path):
        """Delete a file or folder."""
        confirm = messagebox.askyesno(
            "Confirm Delete",
            f"Are you sure you want to delete?\n\n{path}",
            icon="warning",
        )

        if not confirm:
            return

        try:
            if os.path.isfile(path):
                os.remove(path)
                messagebox.showinfo("Success", f"Deleted:\n{path}")
            else:
                shutil.rmtree(path)
                messagebox.showinfo("Success", f"Deleted:\n{path}")

            parent = self.tree.parent(self.tree.focus())
            if parent:
                self.tree.item(parent, open=True)
                self.expand_node(None)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete:\n{str(e)}")

    def on_close(self):
        """Handle window close event."""
        self.stop_flag = True
        self.root.destroy()


def main():
    """Main entry point."""
    root = tk.Tk()
    app = DiskAnalyzer(root)
    root.mainloop()


if __name__ == "__main__":
    main()
