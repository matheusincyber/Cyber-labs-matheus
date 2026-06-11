# Splunk Setup

## Purpose

Splunk is used as the SIEM for this lab. It collects Windows Security logs and Sysmon logs from the monitored Windows host.

## Installed Component

- Splunk Enterprise for Windows

## Local Access

```text
http://localhost:8000
```

## Data Inputs Added

The following Windows Event Logs were added through Splunk local event log collection:

- Security
- System
- Application
- Microsoft-Windows-Sysmon/Operational

## Useful Validation Searches

```spl
index=*
| stats count by source
```

```spl
source="WinEventLog:Security"
```

```spl
source="WinEventLog:Microsoft-Windows-Sysmon/Operational"
```

## Evidence

- `../screenshots/03-splunk/02-splunk-sysmon-events.png`
- `../screenshots/03-splunk/03-splunk-security-events.png`
