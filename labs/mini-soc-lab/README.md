# Mini SOC Lab

A small home SOC lab built to practice log collection, detection, investigation and incident reporting.

This lab uses Windows, Kali Linux, Sysmon and Splunk to simulate basic suspicious activity and investigate it from a blue team point of view.

## Objective

The goal of this lab is to practice SOC Analyst Level 1 workflows.

The lab focuses on:

```text
Collecting Windows logs
Collecting Sysmon events
Searching logs in Splunk
Detecting suspicious activity
Writing simple detection notes
Creating incident reports
Documenting evidence with screenshots
Mapping activity to MITRE ATT&CK
```

## Lab architecture

```text
Kali Linux
  Attacker and simulation machine

Windows host
  Monitored endpoint

Sysmon
  Endpoint telemetry and process creation logs

Windows Security logs
  Authentication and login events

Splunk
  SIEM used to search, investigate and document activity
```

## Lab network

```text
Kali Linux: attacker machine
Windows host-only IP: 192.168.56.1
Splunk web interface: localhost:8000
```

Public documentation should avoid real public IP addresses. Private lab IPs are used only for demonstration.

## Tools used

```text
Windows
Kali Linux
VirtualBox
Splunk
Sysmon
PowerShell
Nmap
smbclient
Windows Event Viewer
MITRE ATT&CK
```

## Data sources

```text
Microsoft-Windows-Sysmon/Operational
WinEventLog:Security
Windows Event Viewer
Kali terminal output
Splunk search results
```

## Detection scenarios

### PowerShell execution detection

Purpose:

Detect PowerShell process execution using Sysmon process creation logs.

Data source:

```text
Microsoft-Windows-Sysmon/Operational
```

Event:

```text
Sysmon Event ID 1
Process Create
```

Example Splunk search:

```spl
source="WinEventLog:Microsoft-Windows-Sysmon/Operational" "powershell.exe"
| table _time host _raw
| sort -_time
```

MITRE ATT&CK mapping:

```text
T1059.001
Command and Scripting Interpreter: PowerShell
```

Related files:

```text
detections/powershell-execution-detection.md
splunk-queries/powershell-execution-detection.spl
incident-reports/IR-003-powershell-execution.md
screenshots/04-powershell-detection/
```

## Failed login detection

Purpose:

Detect failed authentication attempts using Windows Security logs.

Data source:

```text
WinEventLog:Security
```

Event:

```text
EventCode 4625
Failed logon
```

Test performed from Kali:

```bash
smbclient -L //192.168.56.1 -U fakeuser
```

The username `fakeuser` was not created. It was used only to generate a failed login event in a controlled lab.

Expected result from Kali:

```text
NT_STATUS_LOGON_FAILURE
```

Example Splunk search:

```spl
sourcetype="WinEventLog:Security" EventCode=4625
| table _time host Account_Name Source_Network_Address Workstation_Name Failure_Reason Logon_Type
| sort -_time
```

Useful fields:

```text
Account_Name
Source_Network_Address
Workstation_Name
Failure_Reason
Logon_Type
```

Lab result:

```text
Account_Name: fakeuser
Failure_Reason: Unknown user name or bad password
Logon_Type: 3
Workstation_Name: KALI
```

Related files:

```text
detections/failed-login-detection.md
splunk-queries/failed-login-detection.spl
incident-reports/IR-002-failed-logins.md
screenshots/06-failed-logins/
```

## Nmap scan simulation

Purpose:

Simulate basic reconnaissance from Kali against the Windows host-only interface.

Tool:

```text
Nmap
```

Command used:

```bash
nmap -Pn -sV 192.168.56.1
```

Open ports observed:

```text
135/tcp    Microsoft RPC
139/tcp    NetBIOS
445/tcp    SMB
5357/tcp   Microsoft HTTPAPI
5432/tcp   PostgreSQL
8000/tcp   Splunk Web
8089/tcp   Splunk management
```

MITRE ATT&CK mapping:

```text
T1046
Network Service Discovery
```

Related files:

```text
detections/port-scan-detection.md
splunk-queries/port-scan-detection.spl
incident-reports/IR-001-port-scan.md
screenshots/05-nmap-scan/
```

## Folder structure

```text
mini-soc-lab/
  README.md

  architecture/
    Lab diagram and architecture notes

  setup/
    splunk-setup.md
    sysmon-setup.md
    kali-setup.md

  detections/
    powershell-execution-detection.md
    failed-login-detection.md
    port-scan-detection.md

  splunk-queries/
    powershell-execution-detection.spl
    failed-login-detection.spl
    port-scan-detection.spl

  incident-reports/
    IR-001-port-scan.md
    IR-002-failed-logins.md
    IR-003-powershell-execution.md

  screenshots/
    01-setup/
    02-sysmon/
    03-splunk/
    04-powershell-detection/
    05-nmap-scan/
    06-failed-logins/

  lessons-learned.md
```

## Screenshots collected

```text
Kali IP and Windows host-only IP
Sysmon running as a Windows service
Sysmon Event ID 1 in Event Viewer
Splunk ingesting Sysmon logs
Splunk ingesting Windows Security logs
PowerShell execution visible in Splunk
Nmap scan output from Kali
Failed login attempt from Kali
Windows Security EventCode 4625 in Splunk
Expanded failed login event details
```

## Incident reports

The lab includes short SOC-style incident reports.

Reports currently included:

```text
IR-001 Port Scan Simulation
IR-002 Failed Login Attempts
IR-003 PowerShell Execution
```

Each report includes:

```text
Summary
Detection source
Affected host
Evidence
Investigation notes
MITRE ATT&CK mapping
Recommended remediation
Lessons learned
```

## Skills demonstrated

```text
Splunk log searching
Sysmon process monitoring
Windows Security log analysis
PowerShell detection
Authentication failure investigation
Nmap scan analysis
Basic SOC triage
Incident report writing
MITRE ATT&CK mapping
Technical documentation
```

## Notes

This lab was built in a controlled local environment.

All activity was performed against systems I own and manage.

No public targets, real credentials or unauthorized systems were used.

## Next improvements

```text
Create Splunk dashboard panels
Add Windows Firewall logging
Improve Nmap detection using network events
Add alert-style saved searches
Add more PowerShell detection examples
Add suspicious process execution detection
Add Active Directory authentication events later
```
