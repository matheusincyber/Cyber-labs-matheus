# Detection: Failed Login Attempts

## Objective

Detect failed authentication attempts using Windows Security logs in Splunk.

## Windows Event ID

| Event ID | Description |
|---:|---|
| 4625 | Failed logon |

## Log Source

```text
WinEventLog:Security
```

## Detection Query

```spl
source="WinEventLog:Security" EventCode=4625
```

## Aggregation Query

```spl
source="WinEventLog:Security" EventCode=4625
| stats count by Account_Name, Source_Network_Address, host
| sort -count
```

## Test Command From Kali

```bash
smbclient -L //192.168.56.1 -U fakeuser
```

Then enter an incorrect password.

## Evidence

- Kali SMB failed login attempt: `../screenshots/06-failed-logins/01-kali-smbclient-failed-login.png`
- Splunk failed login overview: `../screenshots/06-failed-logins/02-splunk-4625-failed-login-overview.png`
- Expanded Splunk EventCode 4625 details: `../screenshots/06-failed-logins/03-failed-login-event-details-kali-source.png`

The expanded 4625 event shows the attempted username `fakeuser`, source address `192.168.56.1`, workstation name `KALI`, and failure reason `Unknown user name or bad password`.

## MITRE ATT&CK Mapping

| Technique | Name |
|---|---|
| T1110 | Brute Force |

## Recommended Remediation / Monitoring

- Monitor repeated failed logins
- Enforce account lockout policies
- Use strong password policies
- Investigate repeated failures from the same source host
- Disable or restrict unnecessary SMB exposure
