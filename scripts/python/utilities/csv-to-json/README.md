# CSV to JSON Converter

A Python script to convert CSV files to JSON format.

## Description

This script converts CSV (Comma-Separated Values) files to JSON format. It supports various CSV formats, handles headers, and provides options for customizing the output.

## Prerequisites

- Python 3.8 or higher
- No external dependencies (uses standard library only)

## Installation

```bash
# Clone the repository
git clone https://github.com/your-org/useful-scripts.git
cd useful-scripts

# No additional installation needed for Python 3.8+
```

## Usage

```bash
python scripts/python/utilities/csv-to-json/csv_to_json.py [OPTIONS] INPUT_FILE
```

### Options

| Option | Description | Default |
|--------|-------------|---------|
| `-h, --help` | Show help message | - |
| `-o, --output FILE` | Output JSON file | stdout |
| `-k, --key KEY` | Use KEY as parent key in output | records |
| `-e, --encoding ENCODING` | Input file encoding | utf-8 |
| `-d, --delimiter DELIM` | CSV delimiter character | , |
| `-H, --no-header` | Treat first row as data | false |
| `-p, --pretty` | Pretty-print JSON output | false |
| `--version` | Show version | - |

### Arguments

| Argument | Description | Required |
|----------|-------------|----------|
| INPUT_FILE | Path to CSV file | Yes |

## Examples

```bash
# Basic conversion (output to stdout)
python csv_to_json.py data.csv

# Convert and save to file
python csv_to_json.py data.csv -o output.json

# Pretty-print output
python csv_to_json.py data.csv -p

# Use custom delimiter
python csv_to_json.py data.csv -d ";"

# Convert without headers
python csv_to_json.py data.csv -H

# Use custom parent key
python csv_to_json.py data.csv -k "employees"
```

## Sample Input (data.csv)

```csv
name,age,city
John,30,New York
Jane,25,Los Angeles
Bob,35,Chicago
```

## Sample Output

```json
{
  "records": [
    {
      "name": "John",
      "age": "30",
      "city": "New York"
    },
    {
      "name": "Jane",
      "age": "25",
      "city": "Los Angeles"
    },
    {
      "name": "Bob",
      "age": "35",
      "city": "Chicago"
    }
  ]
}
```

## License

[MIT](LICENSE)

## Author

Your Name
