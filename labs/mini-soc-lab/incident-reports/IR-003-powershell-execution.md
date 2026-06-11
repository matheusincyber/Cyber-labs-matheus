# Incident Report: PowerShell Execution Detected

## Incident ID

IR-003

## Severity

Low / Informational

## Summary

PowerShell execution was detected on the monitored Windows host using Sysmon process creation telemetry ingested into Splunk.

## Detection Source

- Sysmon Event ID 1
- Splunk

## Log Source

```text
WinEventLog:Microsoft-Windows-Sysmon/Operational
```

## Detection Query

```spl
source="WinEventLog:Microsoft-Windows-Sysmon/Operational" "powershell.exe"
```

## Evidence

- `../screenshots/04-powershell-detection/02-splunk-powershell-search.png`

## MITRE ATT&CK Mapping

- T1059.001 - Command and Scripting Interpreter: PowerShell

## Analyst Assessment

PowerShell is commonly used for legitimate administration but is also frequently abused by attackers. Analysts should review command-line arguments, parent process, user context, and execution time.

## Recommendations

- Monitor suspicious PowerShell command-line flags
- Enable PowerShell Script Block Logging where appropriate
- Review parent-child process relationships
- Investigate PowerShell launched by unusual parent processes
- Create higher-fidelity detections for suspicious command patterns
