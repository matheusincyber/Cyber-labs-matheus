# Detection: Port Scan / Network Service Discovery

## Objective

Simulate network reconnaissance from Kali Linux and document exposed services on the monitored Windows host.

## Scenario

A Kali Linux VM was used to perform a version/service scan against the Windows host-only interface.

## Attack Command

```bash
nmap -Pn -sV 192.168.56.1
```

## Nmap Results

Open services discovered:

| Port | Service | Notes |
|---:|---|---|
| 135/tcp | msrpc | Microsoft Windows RPC |
| 139/tcp | netbios-ssn | NetBIOS session service |
| 445/tcp | microsoft-ds | SMB |
| 5357/tcp | http | Microsoft HTTPAPI |
| 5432/tcp | postgresql | PostgreSQL database service |
| 8000/tcp | http | Splunk Web |
| 8089/tcp | ssl/http | Splunk management port |

## Evidence

![Kali Nmap scan](../screenshots/05-nmap-scan/01-kali-nmap-results.png)

## MITRE ATT&CK Mapping

| Technique | Name |
|---|---|
| T1046 | Network Service Discovery |

## Detection Concept

A port scan can be detected by looking for one source host connecting to multiple destination ports in a short period.

Example Splunk searches to validate network telemetry:

```spl
source="WinEventLog:Microsoft-Windows-Sysmon/Operational" "192.168.56"
```

```spl
source="WinEventLog:Microsoft-Windows-Sysmon/Operational" EventCode=3
```

```spl
source="WinEventLog:Microsoft-Windows-Sysmon/Operational" ("135" OR "139" OR "445" OR "5357" OR "5432" OR "8000" OR "8089")
```

## Analyst Notes

The scan was performed in a controlled VirtualBox host-only lab network. The scan identified multiple exposed services, including SMB and Splunk services.

## Recommended Remediation / Monitoring

- Restrict unnecessary services
- Review firewall rules
- Limit administrative services to trusted hosts
- Investigate unexpected open ports such as PostgreSQL if not required
- Monitor one host connecting to many ports in a short time window
