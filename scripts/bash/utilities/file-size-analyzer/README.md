# File Size Analyzer

A simple bash script to analyze and display file sizes in a directory.

## Description

This script analyzes files in the specified directory and displays their sizes in a human-readable format. It helps identify large files that might be taking up storage space.

## Prerequisites

- Bash 4.0 or higher
- Standard Unix utilities: `ls`, `du`, `awk`

## Installation

```bash
# Clone the repository
git clone https://github.com/your-org/useful-scripts.git
cd useful-scripts

# Make the script executable
chmod +x scripts/bash/utilities/file-size-analyzer/file-size-analyzer.sh
```

## Usage

```bash
./file-size-analyzer.sh [OPTIONS] [DIRECTORY]
```

### Options

| Option | Description | Default |
|--------|-------------|---------|
| `-h, --help` | Show this help message | - |
| `-n, --number` | Number of results to show | 10 |
| `-s, --sort` | Sort by: size, name, or date | size |
| `-r, --reverse` | Reverse the sort order | false |

### Arguments

| Argument | Description | Default |
|----------|-------------|---------|
| DIRECTORY | Directory to analyze | Current directory |

## Examples

```bash
# Analyze current directory
./file-size-analyzer.sh

# Analyze specific directory
./file-size-analyzer.sh /path/to/directory

# Show top 20 largest files
./file-size-analyzer.sh -n 20

# Sort by name
./file-size-analyzer.sh -s name

# Show smallest files first
./file-size-analyzer.sh -r
```

## Sample Output

```
Analyzing: /home/user/documents
Total files: 1,234

Top 10 largest files:
1.  1.2G  backup-2024.tar.gz
2.  456M  videos/vacation.mp4
3.  234M  projects/project.zip
4.  128M  downloads/game.exe
5.   89M  documents/report.pdf
```

## License

[MIT](LICENSE)

## Author

Your Name
