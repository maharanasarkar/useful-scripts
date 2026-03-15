# JSON Formatter

A Node.js CLI tool to format and validate JSON files.

## Description

This tool formats, validates, and prettifies JSON files. It supports various output formats, sorting options, and can be used as a CLI tool or imported as a module.

## Prerequisites

- Node.js 18 or higher
- npm (comes with Node.js)

## Installation

```bash
# Clone the repository
git clone https://github.com/your-org/useful-scripts.git
cd useful-scripts

# Install dependencies
cd scripts/nodejs/json-formatter
npm install
```

## Usage

```bash
# Format JSON file (output to stdout)
node json-formatter.js input.json

# Save to file
node json-formatter.js input.json -o output.json

# Pretty print with custom indentation
node json-formatter.js input.json --indent 4

# Sort keys alphabetically
node json-formatter.js input.json --sort

# Minify JSON
node json-formatter.js input.json --minify

# Validate only (no output)
node json-formatter.js input.json --validate
```

### Options

| Option | Description | Default |
|--------|-------------|---------|
| `-o, --output FILE` | Output file path | stdout |
| `-i, --indent NUM` | Indentation spaces | 2 |
| `-s, --sort` | Sort object keys | false |
| `-m, --minify` | Minify output | false |
| `-v, --validate` | Validate only, no output | false |
| `--compact` | Compact output (no whitespace) | false |
| `-h, --help` | Show help | - |
| `--version` | Show version | - |

### Programmatic Usage

```javascript
const { formatJSON, validateJSON } = require('./json-formatter');

// Format JSON
const formatted = formatJSON('{"a":1,"b":2}', { indent: 2, sort: true });
console.log(formatted);

// Validate JSON
const result = validateJSON('{"a":1}');
console.log(result.valid); // true
```

## Examples

```bash
# Basic formatting
echo '{"name":"john","age":30}' | node json-formatter.js --stdin

# Pretty print with 4 spaces
node json-formatter.js data.json --indent 4

# Sort all keys
node json-formatter.js config.json --sort > sorted-config.json

# Minify
node json-formatter.js data.json --minify

# Validate and exit with code
node json-formatter.js data.json --validate && echo "Valid JSON!"
```

## Sample Input

```json
{"name":"useful-scripts","version":"1.0.0","author":"Community","scripts":["bash","python","powershell"]}
```

## Sample Output

```json
{
  "author": "Community",
  "name": "useful-scripts",
  "scripts": [
    "bash",
    "python",
    "powershell"
  ],
  "version": "1.0.0"
}
```

## License

[MIT](LICENSE)

## Author

Your Name
