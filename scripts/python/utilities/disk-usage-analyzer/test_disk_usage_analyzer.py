import os
import tempfile
import pytest
from pathlib import Path
from disk_usage_analyzer import format_size, safe_scandir, get_folder_size


class TestFormatSize:
    """Tests for the format_size function."""

    def test_bytes(self):
        assert format_size(500) == "500.00 B"

    def test_kilobytes(self):
        assert format_size(1024) == "1.00 KB"

    def test_megabytes(self):
        assert format_size(1048576) == "1.00 MB"

    def test_gigabytes(self):
        assert format_size(1073741824) == "1.00 GB"

    def test_terabytes(self):
        assert format_size(1099511627776) == "1.00 TB"

    def test_decimal(self):
        assert format_size(1536) == "1.50 KB"


class TestSafeScandir:
    """Tests for the safe_scandir function."""

    def test_existing_directory(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            result = safe_scandir(tmpdir)
            assert result == []

    def test_with_files(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            for i in range(3):
                Path(tmpdir) / f"file{i}.txt"
            result = safe_scandir(tmpdir)
            assert len(result) == 3

    def test_nonexistent_directory(self):
        result = safe_scandir("C:\\nonexistent_path_12345")
        assert result == []

    def test_permission_denied(self):
        result = safe_scandir("C:\\System Volume Information")
        assert result == []


class TestGetFolderSize:
    """Tests for the get_folder_size function."""

    def test_empty_directory(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            size, files = get_folder_size(tmpdir)
            assert size == 0
            assert files == 0

    def test_directory_with_files(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            for i in range(3):
                filepath = os.path.join(tmpdir, f"file{i}.txt")
                with open(filepath, "w") as f:
                    f.write("a" * 100)

            size, files = get_folder_size(tmpdir)
            assert files == 3
            assert size == 300

    def test_nested_directories(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            subdir = os.path.join(tmpdir, "subdir")
            os.makedirs(subdir)

            with open(os.path.join(tmpdir, "file.txt"), "w") as f:
                f.write("hello")

            with open(os.path.join(subdir, "nested.txt"), "w") as f:
                f.write("world")

            size, files = get_folder_size(tmpdir)
            assert files == 2

    def test_nonexistent_directory(self):
        size, files = get_folder_size("C:\\nonexistent_path_12345")
        assert size == 0
        assert files == 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
