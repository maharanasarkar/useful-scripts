# Disk Usage Analyzer

A Windows GUI application to analyze and visualize disk space usage.

## Description

This script scans the C: drive (or any specified path) and displays the largest folders in a tree view. It helps identify which directories are consuming the most disk space. You can expand folders to see their subdirectories, open folders in Explorer, or delete items directly from the application.

## Prerequisites

- Python 3.8 or higher
- Windows OS (uses `tkinter` and Windows-specific paths)

### Dependencies

No external dependencies required - uses Python standard library only:
- `os`
- `threading`
- `tkinter`
- `subprocess`
- `shutil`

## Installation

```bash
# Clone the repository
git clone https://github.com/your-org/useful-scripts.git
cd useful-scripts

# No additional installation needed
```

## Usage

```bash
# Run the script
python scripts/python/utilities/disk-usage-analyzer/disk_usage_analyzer.py
```

### Features

- **Scan Drive**: Click "Scan C Drive" to analyze disk usage
- **Progress Bar**: Shows scanning progress
- **Tree View**: Displays folders sorted by size (largest first)
- **Expand Folders**: Click on a folder to expand and see subdirectories
- **Right-Click Menu**:
  - Open in Explorer
  - Delete folder/file

### Controls

| Action | Description |
|--------|-------------|
| Click folder | Expand/collapse to see subfolders |
| Right-click | Open context menu |
| Scan button | Start new scan |

## Sample Output

```
Folder                    Size        Files    Path
Windows                   45.23 GB    12543    C:\Windows
Program Files             12.45 GB    892      C:\Program Files
Users                     8.92 GB     4521     C:\Users
...
```

## Configuration

To scan a different drive or path, modify the `root_path` variable in the `scan_drive` method:

```python
root_path = "D:\\"  # Change to desired path
```

## Technical Details

- **Threading**: Uses separate thread for scanning to keep GUI responsive
- **Queue**: Communicates between scanning thread and GUI
- **Error Handling**: Gracefully handles permission errors and locked files
- **Top Items**: Configurable via `TOP_ITEMS` constant (default: 40)

## License

[MIT](LICENSE)
