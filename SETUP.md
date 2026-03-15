# Setup Guide

Welcome to useful-scripts! This guide will help you get started with using and contributing to this repository.

---

## Table of Contents

- [Quick Start](#quick-start)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Using Scripts](#using-scripts)
- [Contributing](#contributing)
- [Running Tests](#running-tests)
- [Validation](#validation)

---

## Quick Start

### Clone the Repository

```bash
git clone https://github.com/your-org/useful-scripts.git
cd useful-scripts
```

### Find a Script

Browse the `scripts/` directory to find useful scripts:

```
scripts/
├── bash/          # Shell scripts
├── python/        # Python scripts
├── powershell/   # PowerShell scripts
├── nodejs/       # Node.js scripts
└── other/        # Other languages
```

### Run a Script

Each script folder contains its own README with specific instructions.

---

## Prerequisites

### Required Tools

| Language | Minimum Version | Notes |
|----------|-----------------|-------|
| Git | 2.x | For version control |
| Bash | 4.x | For shell scripts |
| Python | 3.8+ | For Python scripts |
| PowerShell | 7+ | For PowerShell scripts |
| Node.js | 18+ | For Node.js scripts |

### Optional Tools (Recommended)

| Tool | Purpose | Installation |
|------|---------|--------------|
| shellcheck | Bash validation | `apt install shellcheck` / `brew install shellcheck` |
| pylint | Python linting | `pip install pylint` |
| PSScriptAnalyzer | PowerShell validation | `Install-Module -Name PSScriptAnalyzer` |
| npm | Node.js package management | Comes with Node.js |

---

## Installation

### Clone and Setup

```bash
# Clone the repository
git clone https://github.com/your-org/useful-scripts.git
cd useful-scripts

# (Optional) Install development dependencies
pip install -r requirements-dev.txt
```

### Script-Specific Dependencies

Check each script's README.md or requirements.txt for dependencies:

```bash
# Example: Install Python script dependencies
cd scripts/python/your-script
pip install -r requirements.txt

# Example: Install Node.js script dependencies
cd nodejs/your-script
npm install
```

---

## Using Scripts

### General Usage

1. Navigate to the script directory
2. Read the README.md for usage instructions
3. Make the script executable (if needed)
4. Run the script

### Bash Scripts

```bash
cd scripts/bash/your-script
chmod +x your-script.sh
./your-script.sh [options]
```

### Python Scripts

```bash
cd scripts/python/your-script
python main.py [options]
# or
pip install -e .
your-script-command [options]
```

### PowerShell Scripts

```powershell
cd scripts/powershell\your-script
.\script.ps1 -Option "value"
```

### Node.js Scripts

```bash
cd scripts/nodejs/your-script
npm start
# or
node index.js [options]
```

---

## Contributing

### Setting Up Development Environment

1. **Fork** the repository
2. **Clone** your fork
3. **Create** a feature branch

```bash
git clone https://github.com/YOUR_USERNAME/useful-scripts.git
cd useful-scripts
git checkout -b feature/your-feature
```

### Adding a New Script

See the [Script Guide](docs/SCRIPT_GUIDE.md) for detailed instructions.

Quick checklist:
- [ ] Create script in appropriate directory
- [ ] Add README.md with usage instructions
- [ ] Add requirements.txt if needed
- [ ] Add tests if applicable
- [ ] Run validation tools
- [ ] Submit Pull Request

---

## Running Tests

### Run All Tests

```bash
# Using the test runner (if available)
./run-tests.sh

# Or run manually
pytest tests/
```

### Run Language-Specific Tests

```bash
# Python tests
pytest tests/python/

# Bash tests
bash tests/bash/run-all.sh

# PowerShell tests
pwsh -Command "Invoke-Pester tests/powershell/"
```

---

## Validation

Before submitting a contribution, run these validation tools:

### Bash Scripts

```bash
shellcheck scripts/bash/**/*.sh
bashate scripts/bash/your-script.sh
```

### Python Scripts

```bash
flake8 scripts/python/
pylint scripts/python/your-script/
```

### PowerShell Scripts

```powershell
Invoke-ScriptAnalyzer -Path scripts/powershell/your-script.ps1
```

### Node.js Scripts

```bash
eslint scripts/nodejs/
```

---

## Troubleshooting

### Common Issues

**Permission Denied**
```bash
chmod +x your-script.sh
```

**Module Not Found**
```bash
pip install -r requirements.txt
```

**Python Version Error**
```bash
python3 --version  # Check version
pyenv install 3.11  # Install newer version if needed
```

**Missing Dependencies**
- Check script README.md
- Check requirements.txt
- Check package.json (for Node.js)

---

## Getting Help

- **Issues**: Open a [GitHub Issue](https://github.com/your-org/useful-scripts/issues)
- **Discussions**: Use GitHub Discussions
- **Documentation**: Check the [docs/](docs/) directory

---

## Next Steps

- Read the [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines
- Check out the [Script Guide](docs/SCRIPT_GUIDE.md) for writing new scripts
- Review [CATEGORIES.md](docs/CATEGORIES.md) to understand the structure

Happy scripting!
