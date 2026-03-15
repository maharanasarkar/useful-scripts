#!/usr/bin/env python3
"""CSV to JSON Converter - Convert CSV files to JSON format."""

import argparse
import csv
import json
import sys
from pathlib import Path
from typing import Any

__version__ = "1.0.0"
__author__ = "Your Name"


def read_csv(
    filepath: Path, delimiter: str, encoding: str, has_header: bool
) -> tuple[list, list]:
    """Read CSV file and return headers and data."""
    with open(filepath, "r", encoding=encoding) as f:
        if has_header:
            reader = csv.DictReader(f, delimiter=delimiter)
            data = list(reader)
            first_row = data[0] if data else {}
            headers = list(first_row.keys()) if hasattr(first_row, "keys") else []
            return headers, data
        else:
            reader = csv.reader(f, delimiter=delimiter)
            rows = list(reader)
            headers = [f"column_{i}" for i in range(len(rows[0]))] if rows else []
            data = [{f"column_{i}": row[i] for i in range(len(row))} for row in rows]
            return headers, data


def convert_csv_to_json(
    input_file: str,
    output_file: str | None,
    key: str,
    encoding: str,
    delimiter: str,
    has_header: bool,
    pretty: bool,
) -> None:
    """Convert CSV file to JSON."""
    input_path = Path(input_file)

    if not input_path.exists():
        print(f"Error: File '{input_file}' not found", file=sys.stderr)
        sys.exit(1)

    try:
        headers, data = read_csv(input_path, delimiter, encoding, has_header)
    except Exception as e:
        print(f"Error reading CSV file: {e}", file=sys.stderr)
        sys.exit(1)

    if not data:
        print("Warning: CSV file is empty", file=sys.stderr)
        json_output = {}
    else:
        json_output = {key: data}

    json_str = json.dumps(json_output, indent=2 if pretty else None, ensure_ascii=False)

    if output_file:
        try:
            with open(output_file, "w", encoding=encoding) as f:
                f.write(json_str)
            print(f"Successfully converted '{input_file}' to '{output_file}'")
        except Exception as e:
            print(f"Error writing output file: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print(json_str)


def main() -> None:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Convert CSV files to JSON format",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s data.csv
  %(prog)s data.csv -o output.json
  %(prog)s data.csv -d ";" -p
  %(prog)s data.csv -H -k "employees"
        """,
    )

    parser.add_argument("input_file", help="Path to CSV file", metavar="INPUT_FILE")
    parser.add_argument(
        "-o", "--output", help="Output JSON file (default: stdout)", metavar="FILE"
    )
    parser.add_argument(
        "-k",
        "--key",
        help="Parent key for records (default: records)",
        default="records",
        metavar="KEY",
    )
    parser.add_argument(
        "-e",
        "--encoding",
        help="Input file encoding (default: utf-8)",
        default="utf-8",
        metavar="ENCODING",
    )
    parser.add_argument(
        "-d",
        "--delimiter",
        help="CSV delimiter character (default: ,)",
        default=",",
        metavar="DELIM",
    )
    parser.add_argument(
        "-H",
        "--no-header",
        help="Treat first row as data, not as headers",
        action="store_true",
    )
    parser.add_argument(
        "-p", "--pretty", help="Pretty-print JSON output", action="store_true"
    )
    parser.add_argument(
        "--version", action="version", version=f"%(prog)s {__version__}"
    )

    args = parser.parse_args()

    convert_csv_to_json(
        input_file=args.input_file,
        output_file=args.output,
        key=args.key,
        encoding=args.encoding,
        delimiter=args.delimiter,
        has_header=not args.no_header,
        pretty=args.pretty,
    )


if __name__ == "__main__":
    main()
