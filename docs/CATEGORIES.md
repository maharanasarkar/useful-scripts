# Categories

This document describes the categories used to organize scripts in useful-scripts.

---

## Table of Contents

- [Language Overview](#language-overview)
- [Bash Categories](#bash-categories)
- [Python Categories](#python-categories)
- [PowerShell Categories](#powershell-categories)
- [Node.js Categories](#nodejs-categories)
- [Other Categories](#other-categories)
- [Choosing a Category](#choosing-a-category)

---

## Language Overview

| Language | Directory | Primary Use |
|----------|-----------|-------------|
| Bash | `scripts/bash/` | System administration, automation, CLI tools |
| Python | `scripts/python/` | Data processing, automation, APIs |
| PowerShell | `scripts/powershell/` | Windows administration, automation |
| Node.js | `scripts/nodejs/` | Web servers, APIs, tooling |
| Other | `scripts/other/` | Any other languages (Go, Rust, etc.) |

---

## Bash Categories

### `system/`

System administration and maintenance scripts.

**Examples:**
- Disk usage analysis
- Process monitoring
- Service management
- System information gathering

### `devtools/`

Development utilities and helpers.

**Examples:**
- Git helpers
- Docker management
- Environment setup
- Code formatting wrappers

### `utilities/`

General-purpose utilities that don't fit other categories.

**Examples:**
- File manipulation
- Text processing
- Network utilities
- Backup scripts

---

## Python Categories

### `automation/`

Task automation and workflow scripts.

**Examples:**
- File organization
- Email automation
- Scheduled tasks
- Report generation

### `data-processing/`

Data manipulation and transformation scripts.

**Examples:**
- CSV/JSON processing
- Data cleaning
- File conversions
- Data analysis

### `utilities/`

General-purpose Python utilities.

**Examples:**
- API clients
- File helpers
- Image processing
- Web scraping

---

## PowerShell Categories

### `windows/`

Windows-specific scripts and administration.

**Examples:**
- Windows configuration
- Active Directory management
- Registry editing
- Windows service management

### `system/`

Cross-platform system administration.

**Examples:**
- Service monitoring
- Log analysis
- Performance monitoring
- Backup automation

### `utilities/`

General PowerShell utilities.

**Examples:**
- File operations
- String manipulation
- Network diagnostics
- User management

---

## Node.js Categories

Node.js scripts follow similar categories but may include:

- `api/` - REST API servers and clients
- `cli/` - Command-line tools
- `automation/` - Task automation
- `utilities/` - General utilities

---

## Other Categories

For languages like Go, Rust, Ruby, etc., use:

- `scripts/other/[language]/`

Example:
```
scripts/other/
├── go/
│   └── cli-tools/
├── rust/
│   └── utilities/
└── ruby/
    └── automation/
```

---

## Choosing a Category

Use this decision tree to choose the right category:

```
Is the script language-specific?
│
├─ No → Put in appropriate language > appropriate category
│
└─ Yes → Is it a system administration script?
         │
         ├─ Yes → Use system/ category
         │
         └─ No → Is it a development tool?
                 │
                 ├─ Yes → Use devtools/ category
                 │
                 └─ No → Use utilities/ category
```

### Additional Guidelines

1. **When in doubt**: Use `utilities/` - it's the catch-all category
2. **Multiple categories**: If a script fits multiple categories, choose the primary one
3. **New categories**: If you need a new category, suggest it in an issue first
4. **Cross-language**: If a script uses multiple languages, categorize by primary language

---

## Creating New Categories

To propose a new category:

1. Open an [Issue](https://github.com/your-org/useful-scripts/issues)
2. Explain the proposed category
3. Provide examples of scripts that would fit
4. Wait for maintainer approval

---

## Current Statistics

| Category | Script Count |
|----------|-------------|
| bash/system | 0 |
| bash/devtools | 0 |
| bash/utilities | 0 |
| python/automation | 0 |
| python/data-processing | 0 |
| python/utilities | 0 |
| powershell/windows | 0 |
| powershell/system | 0 |
| powershell/utilities | 0 |
| nodejs | 0 |
| other | 0 |

*(This will be updated as scripts are added)*

---

## Related Documents

- [Script Guide](SCRIPT_GUIDE.md) - How to write and format scripts
- [CONTRIBUTING.md](../CONTRIBUTING.md) - Contribution guidelines
- [README.md](../README.md) - Main repository readme
