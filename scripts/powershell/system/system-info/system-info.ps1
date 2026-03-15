<#
.SYNOPSIS
    System Information - Gather and display system information.

.DESCRIPTION
    This script collects detailed system information including OS version,
    hardware specs, network configuration, and installed software.

.PARAMETER Category
    Category to report: All, OS, Hardware, Network, Software

.PARAMETER OutputFile
    Save output to file

.PARAMETER Format
    Output format: Text, JSON, HTML

.PARAMETER ShowHidden
    Include hidden network adapters

.EXAMPLE
    .\system-info.ps1

.EXAMPLE
    .\system-info.ps1 -Category Hardware

.EXAMPLE
    .\system-info.ps1 -Format JSON -OutputFile report.json

.NOTES
    Author: Your Name
    Version: 1.0.0
#>

[CmdletBinding()]
param(
    [Parameter()]
    [ValidateSet("All", "OS", "Hardware", "Network", "Software")]
    [string]$Category = "All",

    [Parameter()]
    [string]$OutputFile,

    [Parameter()]
    [ValidateSet("Text", "JSON", "HTML")]
    [string]$Format = "Text",

    [Parameter()]
    [switch]$ShowHidden
)

$ErrorActionPreference = "Stop"

$script:Report = @{
    Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    OS = @{}
    Hardware = @{}
    Network = @{}
    Software = @{}
}

function Get-OSInfo {
    $os = Get-CimInstance Win32_OperatingSystem
    $script:Report.OS = @{
        Name = $os.Caption
        Version = $os.Version
        Build = $os.BuildNumber
        Architecture = $os.OSArchitecture
        InstallDate = $os.InstallDate
        LastBootTime = $os.LastBootUpTime
    }
}

function Get-HardwareInfo {
    $cpu = Get-CimInstance Win32_Processor | Select-Object -First 1
    $mem = Get-CimInstance Win32_PhysicalMemory | Measure-Object -Property Capacity -Sum
    $disks = Get-CimInstance Win32_LogicalDisk -Filter "DriveType=3"

    $script:Report.Hardware = @{
        CPU = @{
            Name = $cpu.Name
            Cores = $cpu.NumberOfCores
            LogicalProcessors = $cpu.NumberOfLogicalProcessors
        }
        Memory = @{
            TotalGB = [math]::Round($mem.Sum / 1GB, 2)
        }
        Disks = @($disks | ForEach-Object {
            @{
                Drive = $_.DeviceID
                SizeGB = [math]::Round($_.Size / 1GB, 2)
                FreeGB = [math]::Round($_.FreeSpace / 1GB, 2)
            }
        })
    }
}

function Get-NetworkInfo {
    $adapters = Get-NetAdapter | Where-Object {
        $_.Status -eq "Up" -and ($ShowHidden -or $_.Hidden -eq $false)
    }

    $script:Report.Network = @($adapters | ForEach-Object {
        $ipConfig = Get-NetIPAddress -InterfaceIndex $_.ifIndex -AddressFamily IPv4 -ErrorAction SilentlyContinue
        @{
            Name = $_.Name
            Status = $_.Status
            LinkSpeed = $_.LinkSpeed
            IPAddress = $ipConfig.IPAddress
        }
    })
}

function Get-SoftwareInfo {
    $apps = Get-ItemProperty HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\*,
        HKLM:\Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\* -ErrorAction SilentlyContinue |
        Where-Object { $_.DisplayName } |
        Select-Object DisplayName, DisplayVersion, Publisher |
        Sort-Object DisplayName |
        Select-Object -First 20

    $script:Report.Software = @($apps | ForEach-Object {
        @{
            Name = $_.DisplayName
            Version = $_.DisplayVersion
            Publisher = $_.Publisher
        }
    })
}

function Format-TextOutput {
    $output = @()
    $output += "=== System Information Report ==="
    $output += "Generated: $($script:Report.Timestamp)"
    $output += ""

    if ($Category -eq "All" -or $Category -eq "OS") {
        $output += "--- Operating System ---"
        $output += "Name:    $($script:Report.OS.Name)"
        $output += "Version: $($script:Report.OS.Version)"
        $output += "Build:   $($script:Report.OS.Build)"
        $output += "Arch:    $($script:Report.OS.Architecture)"
        $output += ""
    }

    if ($Category -eq "All" -or $Category -eq "Hardware") {
        $output += "--- Hardware ---"
        $output += "CPU:     $($script:Report.Hardware.CPU.Name)"
        $output += "Cores:   $($script:Report.Hardware.CPU.Cores)"
        $output += "RAM:     $($script:Report.Hardware.Memory.TotalGB) GB"
        $output += ""
    }

    if ($Category -eq "All" -or $Category -eq "Network") {
        $output += "--- Network ---"
        foreach ($adapter in $script:Report.Network) {
            $output += "Adapter: $($adapter.Name)"
            $output += "IP:      $($adapter.IPAddress)"
            $output += ""
        }
    }

    if ($Category -eq "All" -or $Category -eq "Software") {
        $output += "--- Installed Software (Top 20) ---"
        foreach ($app in $script:Report.Software) {
            $output += "$($app.Name) - $($app.Version)"
        }
        $output += ""
    }

    return $output -join "`n"
}

try {
    Write-Verbose "Collecting system information..."

    if ($Category -eq "All" -or $Category -eq "OS") {
        Get-OSInfo
    }
    if ($Category -eq "All" -or $Category -eq "Hardware") {
        Get-HardwareInfo
    }
    if ($Category -eq "All" -or $Category -eq "Network") {
        Get-NetworkInfo
    }
    if ($Category -eq "All" -or $Category -eq "Software") {
        Get-SoftwareInfo
    }

    Write-Verbose "Formatting output..."

    $result = switch ($Format) {
        "JSON" { $script:Report | ConvertTo-Json -Depth 4 }
        "HTML" { "<pre>$(Format-TextOutput)</pre>" }
        default { Format-TextOutput }
    }

    if ($OutputFile) {
        $result | Out-File -FilePath $OutputFile -Encoding UTF8
        Write-Host "Report saved to: $OutputFile"
    } else {
        Write-Output $result
    }

} catch {
    Write-Error "Error gathering system information: $_"
    exit 1
}
