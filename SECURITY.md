# Security Policy

## Supported Versions

We currently support the following versions with security updates:

| Version | Supported          |
| ------- | ------------------ |
| 1.x.x   | :white_check_mark: |

---

## Reporting a Vulnerability

We take security vulnerabilities seriously. If you discover a security issue, please report it responsibly.

### How to Report

**DO NOT** create a public GitHub issue for security vulnerabilities.

Instead, please report vulnerabilities through one of these methods:

1. **Email**: Contact the maintainers privately
2. **GitHub Security Advisories**: Use the [Private Vulnerability Reporting](https://github.com/your-org/useful-scripts/security/advisories/new) feature

### What to Include

When reporting, please include:

- Description of the vulnerability
- Steps to reproduce the issue
- Potential impact of the vulnerability
- Any possible fixes or mitigations (if known)

### Response Timeline

- **Initial Response**: Within 48 hours
- **Severity Assessment**: Within 7 days
- **Fix Timeline**: Depends on severity (see below)

| Severity | Fix Timeline |
|----------|--------------|
| Critical | 24-72 hours |
| High     | 7 days       |
| Medium   | 30 days      |
| Low      | Next release |

---

## Security Best Practices for Contributors

When contributing scripts, please follow these security guidelines:

### Required

- **Never** hardcode credentials, API keys, or secrets
- **Never** include passwords or tokens in scripts
- **Always** use environment variables for sensitive data
- **Always** validate input data
- **Always** use parameterized queries for database operations

### Recommended

- Use secure comparison (timing-safe) for sensitive operations
- Implement proper error handling without exposing sensitive information
- Add input sanitization
- Use HTTPS for network requests
- Implement rate limiting where applicable

### Prohibited

- Scripts that collect or transmit user data without consent
- Scripts with backdoors or hidden functionality
- Scripts that bypass authentication or authorization
- Ransomware, cryptomining, or other malicious code

---

## Security Updates

We will publish security advisories for any vulnerabilities found:

- GitHub Security Advisories
- Release notes for affected versions
- Community announcements

---

## Scope

This security policy applies to:

- All scripts in the `scripts/` directory
- Documentation files
- CI/CD workflows
- GitHub Actions

It does **not** apply to user-generated content in issues or discussions.

---

## Attribution

Thank you for helping us keep this project secure!
