# Incident Report: Port Scan Detected

## Incident ID

IR-001

## Severity

Low / Informational

## Summary

A Kali Linux VM performed a controlled Nmap service scan against a monitored Windows host in a VirtualBox host-only lab network. The scan identified multiple open ports and services.

## Detection Source

- Kali Linux Nmap output
- Splunk
- Sysmon / Windows event telemetry

## Affected Host

Windows lab host

## Source Host

Kali Linux VM

## Target IP

```text
192.168.56.1
```

## Timeline

| Time | Event |
|---|---|
| 10:07 | Nmap scan launched from Kali Linux |
| 10:07 | Windows host responded to scan |
| 10:07 | Open ports and services identified |
| After scan | Analyst reviewed Splunk and Sysmon logs |

## Evidence

- `../screenshots/05-nmap-scan/01-kali-nmap-results.png`

## Nmap Command

```bash
nmap -Pn -sV 192.168.56.1
```

## Open Ports Identified

- 135/tcp - Microsoft RPC
- 139/tcp - NetBIOS
- 445/tcp - SMB
- 5357/tcp - Microsoft HTTPAPI
- 5432/tcp - PostgreSQL
- 8000/tcp - Splunk Web
- 8089/tcp - Splunk management port

## MITRE ATT&CK Mapping

- T1046 - Network Service Discovery

## Analyst Assessment

The behavior is consistent with network reconnaissance. In this lab, the scan was authorized and performed for defensive learning. In a production environment, similar behavior should be investigated to determine whether it is approved vulnerability scanning or unauthorized reconnaissance.

## Recommendations

- Review exposed services
- Limit SMB and management interfaces to trusted hosts
- Investigate unexpected services such as PostgreSQL
- Enable network connection logging where appropriate
- Create SIEM detections for one source connecting to multiple ports in a short time window
