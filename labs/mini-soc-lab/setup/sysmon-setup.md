# Sysmon Setup

## Purpose

Sysmon is used to collect detailed endpoint telemetry from the Windows host, especially process creation events.

## Installed Component

- Microsoft Sysinternals Sysmon
- SwiftOnSecurity Sysmon config

## Installation Command

```powershell
.\Sysmon64.exe -accepteula -i .\sysmonconfig-export.xml
```

## Service Validation

```powershell
Get-Service Sysmon64
```

Expected result:

```text
Status   Name      DisplayName
Running  Sysmon64  Sysmon64
```

## Event Viewer Path

```text
Applications and Services Logs
→ Microsoft
→ Windows
→ Sysmon
→ Operational
```

## Important Event ID

| Event ID | Description |
|---:|---|
| 1 | Process Create |
| 3 | Network Connection, if enabled in config |
| 22 | DNS Query |

## Evidence

- `../screenshots/02-sysmon/01-sysmon-event-id-1-process-create.png`
- `../screenshots/02-sysmon/02-sysmon-service-running.png`
