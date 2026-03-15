# Script Guide

This guide provides standards and templates for contributing scripts to useful-scripts.

---

## Table of Contents

- [Directory Structure](#directory-structure)
- [Required Files](#required-files)
- [Script Templates](#script-templates)
- [Coding Standards](#coding-standards)
- [Documentation Standards](#documentation-standards)
- [Testing](#testing)

---

## Directory Structure

Each script lives in its own directory under the appropriate language/category:

```
scripts/
├── bash/
│   ├── system/           # System administration
│   ├── devtools/        # Development utilities
│   └── utilities/       # General utilities
├── python/
│   ├── automation/      # Task automation
│   ├── data-processing/ # Data manipulation
│   └── utilities/       # General utilities
├── powershell/
│   ├── windows/         # Windows-specific
│   ├── system/          # System administration
│   └── utilities/       # General utilities
├── nodejs/
│   └── [category]/
└── other/
    └── [category]/
```

### Naming Conventions

| Item | Convention | Example |
|------|------------|---------|
| Directory | `kebab-case` | `backup-automation` |
| Bash script | `kebab-case.sh` | `backup-automation.sh` |
| Python script | `kebab-case.py` | `backup_automation.py` |
| PowerShell | `kebab-case.ps1` | `backup-automation.ps1` |
| Node.js | `kebab-case.js` | `backup-automation.js` |
| Test file | `test_script.py`, `script.test.sh` | `test_backup.py` |

---

## Required Files

Every script submission MUST include:

### 1. Main Script File

The executable script itself.

### 2. README.md (Required)

Must include:

```markdown
# Script Name

Brief description of what this script does.

## Description

Detailed description of the script's functionality.

## Prerequisites

- List any required tools or dependencies
- Minimum versions required

## Installation

Step-by-step installation instructions.

## Usage

Basic usage examples.

### Options/Arguments

| Option | Description | Default |
|--------|-------------|---------|
| -h, --help | Show help message | - |
| -v, --verbose | Enable verbose output | false |

### Examples

```bash
# Example 1: Basic usage
./script.sh

# Example 2: With options
./script.sh --option value
```

## License

[MIT](LICENSE) / [Same as repository]

## Author

Your Name
```

### 3. Other Required Files (If Applicable)

| File | When Required |
|------|----------------|
| `requirements.txt` | Python scripts with dependencies |
| `package.json` | Node.js scripts |
| `test_*.py` | Python scripts with tests |
| `*.test.sh` | Bash scripts with tests |
| `*.tests.ps1` | PowerShell scripts with tests |

---

## Script Templates

### Bash Script Template

```bash
#!/usr/bin/env bash

set -euo pipefail

SCRIPT_NAME="$(basename "$0")"
VERSION="1.0.0"

usage() {
    cat << EOF
Usage: $SCRIPT_NAME [OPTIONS]

Description of what the script does.

OPTIONS:
    -h, --help      Show this help message
    -v, --verbose   Enable verbose output
    -o, --option    Description of option

EXAMPLES:
    $SCRIPT_NAME
    $SCRIPT_NAME --option value

EOF
    exit 1
}

main() {
    while [[ $# -gt 0 ]]; do
        case $1 in
            -h|--help)
                usage
                ;;
            -v|--verbose)
                VERBOSE=true
                shift
                ;;
            -o|--option)
                OPTION="$2"
                shift 2
                ;;
            *)
                echo "Unknown option: $1"
                usage
                ;;
        esac
    done
    
    # Script logic here
    echo "Script completed"
}

main "$@"
```

### Python Script Template

```python
#!/usr/bin/env python3
"""Script name - Brief description."""

import argparse
import sys
from pathlib import Path

__version__ = "1.0.0"
__author__ = "Your Name"


def main():
    parser = argparse.ArgumentParser(
        description="Description of what the script does"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose output"
    )
    parser.add_argument(
        "-o", "--option",
        type=str,
        default="default",
        help="Description of option"
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}"
    )
    
    args = parser.parse_args()
    
    # Script logic here
    print("Script completed")


if __name__ == "__main__":
    main()
```

### PowerShell Script Template

```powershell
<#
.SYNOPSIS
    Short description

.DESCRIPTION
    Detailed description

.PARAMETER Option
    Description of option

.EXAMPLE
    .\script.ps1 -Option "value"

.NOTES
    Author: Your Name
    Version: 1.0.0
#>

[CmdletBinding()]
param(
    [Parameter()]
    [string]$Option = "default",
    
    [Parameter()]
    [switch]$Verbose
)

$ErrorActionPreference = "Stop"

# Script logic here
Write-Output "Script completed"
```

### Node.js Script Template

```javascript
#!/usr/bin/env node

const { program } = require('commander');

program
  .name('script-name')
  .description('Description of what the script does')
  .version('1.0.0')
  .option('-o, --option <value>', 'Description of option', 'default')
  .option('-v, --verbose', 'Enable verbose output')
  .parse(process.argv);

const options = program.opts();

// Script logic here
console.log('Script completed');
```

---

## Coding Standards

### Bash

- Use `set -euo pipefail`
- Use `[[ ]]` instead of `[ ]`
- Quote variables: `"$variable"`
- Use `snake_case` for variables
- Add error handling
- Use functions for reusable code
- Run `shellcheck` before submitting

### Python

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use type hints where appropriate
- Add docstrings to functions
- Use `argparse` for CLI
- Run `pylint` or `flake8` before submitting
- Minimum Python version: 3.8

### PowerShell

- Follow [PowerShell Best Practices](https://docs.microsoft.com/en-us/powershell/scripting/learn/best-practices)
- Use comment-based help
- Use `[CmdletBinding()]`
- Use strict mode: `$ErrorActionPreference = "Stop"`
- Run `PSScriptAnalyzer` before submitting
- Minimum PowerShell version: 7

### Node.js

- Use ES6+ features
- Use a linter (ESLint)
- Use a formatter (Prettier)
- Include `package.json` with proper metadata
- Use a CLI framework (Commander.js, Yargs)
- Minimum Node.js version: 18

---

## Documentation Standards

### README.md Requirements

1. **Title**: Script name as H1
2. **Description**: 1-2 sentences about what it does
3. **Prerequisites**: Required tools/dependencies
4. **Installation**: Clear installation steps
5. **Usage**: How to run the script
6. **Options**: All available options/arguments
7. **Examples**: At least 2 usage examples
8. **License**: Same as repository
9. **Author**: Your name (optional)

### Additional Documentation

For complex scripts, consider adding:
- TROUBLESHOOTING.md
- CHANGELOG.md
- CONTRIBUTING.md (if applicable)

---

## Testing

### Test File Locations

| Language | Test Directory | Test File Pattern |
|----------|---------------|-------------------|
| Python | `tests/python/` or script dir | `test_*.py` |
| Bash | `tests/bash/` or script dir | `*.test.sh` |
| PowerShell | `tests/powershell/` or script dir | `*.tests.ps1` |
| Node.js | `test/` in script dir | `*.test.js` |

### Test Coverage

Tests should cover:
- Basic functionality
- Edge cases
- Error handling
- Command-line arguments

### Running Tests

```bash
# Python
pytest tests/

# Bash
bats tests/

# PowerShell
Invoke-Pester

# Node.js
npm test
```

---

## Validation Checklist

Before submitting, ensure:

- [ ] Script runs without errors
- [ ] README.md is complete
- [ ] All examples work
- [ ] Validation tools pass:
  - Bash: `shellcheck`
  - Python: `pylint` or `flake8`
  - PowerShell: `PSScriptAnalyzer`
  - Node.js: `eslint`
- [ ] No hardcoded secrets
- [ ] Script handles errors gracefully

---

## Questions?

If you have questions about writing a script, please:
1. Check existing scripts for examples
2. Open a [Discussion](https://github.com/your-org/useful-scripts/discussions)
3. Contact maintainers
