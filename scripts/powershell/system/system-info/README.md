# System Information

A PowerShell script to gather and display system information.

## Description

This script collects detailed system information including OS version, hardware specs, network configuration, and installed software. Useful for system auditing and troubleshooting.

## Prerequisites

- PowerShell 7.0 or higher
- Administrator privileges may be required for some information

## Installation

```powershell
# Clone the repository
git clone https://github.com/your-org/useful-scripts.git
cd useful-scripts
```

## Usage

```powershell
# Basic usage
.\scripts\powershell\system\system-info\system-info.ps1

# Specific categories
.\system-info.ps1 -Category Hardware

# Export to file
.\system-info.ps1 -OutputFile system-report.txt

# Verbose output
.\system-info.ps1 -Verbose
```

### Parameters

| Parameter | Description | Type |
|-----------|-------------|------|
| `-Category` | Category to report: All, OS, Hardware, Network, Software | String |
| `-OutputFile` | Save output to file | String |
| `-Format` | Output format: Text, JSON, HTML | String |
| `-ShowHidden` | Include hidden network adapters | Switch |

### Examples

```powershell
# Get all system information
.\system-info.ps1

# Hardware information only
.\system-info.ps1 -Category Hardware

# Export to JSON
.\system-info.ps1 -Format JSON -OutputFile report.json

# Include hidden adapters
.\system-info.ps1 -ShowHidden
```

## Output Categories

### Operating System
- OS Name and Version
- Build Number
- Architecture
- Installation Date
- Last Boot Time

### Hardware
- CPU Model and Cores
- Total Memory
- Disk Information
- Graphics Cards

### Network
- IP Configuration
- Network Adapters
- DNS Servers

### Software
- Installed Applications
- Running Services

## Sample Output

```
=== System Information Report ===
Generated: 2024-01-15 10:30:00

--- Operating System ---
Name:    Microsoft Windows 11 Pro
Version: 23H2 Build 22631
Arch:    64-bit

--- Hardware ---
CPU:     Intel(R) Core(TM) i7-10700K
Cores:   8
RAM:     32 GB

--- Network ---
Adapter: Ethernet
IP:      192.168.1.100
Gateway: 192.168.1.1
```

## License

[MIT](LICENSE)

## Author

Your Name
