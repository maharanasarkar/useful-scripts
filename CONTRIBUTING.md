# Contributing to useful-scripts

Welcome! We're excited that you're interested in contributing to useful-scripts. This document provides guidelines for contributing scripts, bug fixes, documentation, and other improvements.

---

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Script Standards](#script-standards)
- [Pull Request Process](#pull-request-process)
- [Review Process](#review-process)
- [Recognition](#recognition)

---

## Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md). Please read it before contributing.

---

## Getting Started

### Prerequisites

Before contributing, ensure you have:

- **Git** installed on your system
- **A GitHub account**
- **Language-specific tools** for the scripts you're contributing:
  - Bash: `bash`, `shellcheck` (for validation)
  - Python: Python 3.x, `pytest` (for testing)
  - PowerShell: PowerShell 7+, `PSScriptAnalyzer`
  - Node.js: Node.js LTS, `npm`

### Fork the Repository

1. Click the **Fork** button on the repository page
2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/useful-scripts.git
   cd useful-scripts
   ```
3. Add the upstream repository:
   ```bash
   git remote add upstream https://github.com/original-owner/useful-scripts.git
   ```

### Create a Branch

```bash
git checkout -b feature/your-script-name
# or
git checkout -b fix/bug-description
```

---

## How to Contribute

### 1. Add a New Script

Scripts are organized by language and category:

```
scripts/
├── bash/
│   ├── system/
│   ├── devtools/
│   └── utilities/
├── python/
│   ├── automation/
│   ├── data-processing/
│   └── utilities/
├── powershell/
│   ├── windows/
│   ├── system/
│   └── utilities/
├── nodejs/
└── other/
```

Each script should be in its own folder with:
- **Main script file** (required)
- **README.md** with usage instructions (required)
- **requirements.txt** or dependencies (if applicable)
- **Test file** (if applicable)
- **examples/** folder (optional)

See [Script Guide](docs/SCRIPT_GUIDE.md) for detailed standards.

### 2. Improve Documentation

Documentation improvements are always welcome! Whether it's fixing typos, clarifying instructions, or adding examples.

### 3. Report Bugs

Use the [Bug Report](.github/ISSUE_TEMPLATE/bug_report.md) template to report issues.

### 4. Request Features

Use the [Feature Request](.github/ISSUE_TEMPLATE/feature_request.md) template to suggest new scripts.

### 5. Request New Scripts

Use the [Script Request](.github/ISSUE_TEMPLATE/script_request.md) template to suggest scripts you'd like to see.

---

## Script Standards

All scripts must meet these requirements:

### Required

- [ ] Include a **README.md** with:
  - Description of what the script does
  - Prerequisites/dependencies
  - Installation instructions
  - Usage examples
  - Options/arguments (if any)
- [ ] Be **tested** before submission
- [ ] Follow language-specific **coding standards**
- [ ] Be **portable** (no hardcoded paths unless necessary)
- [ ] Handle **errors gracefully**

### Recommended

- [ ] Include **comments** for complex logic
- [ ] Provide **verbose mode** or `-h/--help`
- [ ] Include **version information**
- [ ] Add **license headers** if applicable

### Prohibited

- [ ] Hardcoded credentials, API keys, or secrets
- [ ] Scripts that could cause data loss without confirmation
- [ ] Malicious code of any kind
- [ ] Scripts that violate the license

---

## Pull Request Process

### Before Submitting

1. **Test your script** thoroughly
2. **Run validation tools**:
   - Bash: `shellcheck your-script.sh`
   - Python: `pylint your-script.py` or `flake8`
   - PowerShell: `Invoke-ScriptAnalyzer`
   - Node.js: `eslint`
3. **Update documentation** if needed
4. **Rebase your branch** on the latest upstream:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

### Creating a Pull Request

1. Push your branch:
   ```bash
   git push origin feature/your-script-name
   ```
2. Open a Pull Request using the [template](.github/PULL_REQUEST_TEMPLATE.md)
3. Fill in all required sections

### PR Checklist

- [ ] My script works as documented
- [ ] README.md is complete with usage examples
- [ ] Tests pass (if applicable)
- [ ] No hardcoded secrets/credentials
- [ ] Compatible with latest stable versions
- [ ] I have the rights to submit this code
- [ ] I agree to the Contributor License Agreement

---

## Review Process

| PR Type | Reviewers Required |
|---------|-------------------|
| New script | 1 reviewer |
| Bug fix | 1 reviewer |
| Documentation only | Maintainer discretion |
| Breaking changes | 2 reviewers |

### Review Criteria

Reviewers will evaluate:

1. **Functionality** - Does the script work as intended?
2. **Code Quality** - Is the code clean and maintainable?
3. **Documentation** - Is it clear how to use the script?
4. **Security** - Are there any security concerns?
5. **Testing** - Are there adequate tests?

### Addressing Feedback

- Respond to review comments
- Make necessary changes
- Request re-review when ready

---

## Recognition

Contributors will be recognized in:

- The [CONTRIBUTORS.md](CONTRIBUTORS.md) file
- Release notes for significant contributions

---

## Questions?

- Open an [Issue](https://github.com/your-org/useful-scripts/issues) for questions
- Join our community discussions
- Contact maintainers via email

Thank you for contributing!
