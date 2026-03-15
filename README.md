# useful-scripts

A community-driven collection of useful scripts for various tasks and purposes.

[![Contributors](https://img.shields.io/github/contributors/your-org/useful-scripts)](https://github.com/your-org/useful-scripts/graphs/contributors)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

---

## Table of Contents

- [About](#about)
- [Quick Start](#quick-start)
- [Available Scripts](#available-scripts)
- [Contributing](#contributing)
- [Community](#community)
- [License](#license)

---

## About

useful-scripts is an open-source collection of scripts designed to help developers, system administrators, and power users automate common tasks. Our goal is to provide high-quality, well-documented scripts that anyone can use.

### Features

- **Multi-language support**: Bash, Python, PowerShell, Node.js, and more
- **Well-documented**: Every script includes comprehensive documentation
- **Community-driven**: Built by contributors from around the world
- **Tested**: Scripts are validated through CI/CD pipelines
- **Free to use**: MIT licensed

---

## Quick Start

### Clone the Repository

```bash
git clone https://github.com/your-org/useful-scripts.git
cd useful-scripts
```

### Browse Scripts

Explore the `scripts/` directory:

```
scripts/
├── bash/          # Shell scripts (Linux/macOS/Windows WSL)
├── python/        # Python scripts
├── powershell/   # PowerShell scripts (Windows)
├── nodejs/       # Node.js scripts
└── other/        # Other languages
```

### Use a Script

Each script is in its own directory with documentation:

```bash
# Example: Using a Python script
cd scripts/python/utilities/csv-to-json
python csv_to_json.py data.csv -o output.json

# Example: Using a bash script
cd scripts/bash/utilities/file-size-analyzer
./file-size-analyzer.sh /path/to/directory
```

For detailed instructions, see [SETUP.md](SETUP.md).

---

## Available Scripts

### Bash Scripts

| Script | Category | Description |
|--------|----------|-------------|
| [file-size-analyzer](scripts/bash/utilities/file-size-analyzer/) | utilities | Analyze and display file sizes |

### Python Scripts

| Script | Category | Description |
|--------|----------|-------------|
| [disk-usage-analyzer](scripts/python/utilities/disk-usage-analyzer/) | utilities | Analyze Windows disk space usage with GUI |
| [csv-to-json](scripts/python/utilities/csv-to-json/) | utilities | Convert CSV files to JSON format |

### PowerShell Scripts

| Script | Category | Description |
|--------|----------|-------------|
| [system-info](scripts/powershell/system/system-info/) | system | Gather system information |

### Node.js Scripts

| Script | Category | Description |
|--------|----------|-------------|
| [json-formatter](scripts/nodejs/json-formatter/) | utilities | Format and validate JSON files |

*Browse the [scripts/](scripts/) directory for the complete list.*

---

## Contributing

We welcome contributions from the community! Whether you want to:

- Add a new script
- Fix a bug
- Improve documentation
- Request a new feature

Please read our [Contributing Guide](CONTRIBUTING.md) to get started.

### Quick Contribution Steps

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/your-feature`
3. **Add** your script following our [Script Guide](docs/SCRIPT_GUIDE.md)
4. **Test** your script
5. **Submit** a Pull Request

### Requirements

- Scripts must include a `README.md`
- Follow language-specific coding standards
- Pass validation checks (shellcheck, pylint, etc.)
- No hardcoded secrets or credentials

For more details, see:
- [Script Guide](docs/SCRIPT_GUIDE.md)
- [Categories](docs/CATEGORIES.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)

---

## Community

### Discussion

Join our [Discussions](https://github.com/your-org/useful-scripts/discussions) to:
- Ask questions
- Share ideas
- Get help

### Issues

- **Bug Reports**: Use [Bug Report](.github/ISSUE_TEMPLATE/bug_report.md) template
- **Feature Requests**: Use [Feature Request](.github/ISSUE_TEMPLATE/feature_request.md) template
- **Script Requests**: Use [Script Request](.github/ISSUE_TEMPLATE/script_request.md) template

### Security

See [SECURITY.md](SECURITY.md) for reporting security vulnerabilities.

---

## License

This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.

---

## Related Documentation

- [SETUP.md](SETUP.md) - Quick start guide
- [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guidelines
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) - Community code of conduct
- [SECURITY.md](SECURITY.md) - Security policy
- [docs/SCRIPT_GUIDE.md](docs/SCRIPT_GUIDE.md) - Script writing standards
- [docs/CATEGORIES.md](docs/CATEGORIES.md) - Category descriptions

---

<p align="center">
  Made with :heart: by the community
</p>
