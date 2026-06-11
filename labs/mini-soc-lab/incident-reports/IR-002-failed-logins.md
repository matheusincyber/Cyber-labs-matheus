# Incident Report: Multiple Failed Login Attempts

## Incident ID

IR-002

## Severity

Medium

## Summary

A failed SMB login attempt was simulated from Kali Linux against the Windows host using a nonexistent username. The goal was to detect failed authentication activity using Windows Security Event ID 4625 in Splunk.

## Detection Source

- Windows Security Logs
- Splunk

## Event ID

```text
4625 - Failed logon
```

## Detection Query

```spl
source="WinEventLog:Security" EventCode=4625
```

## Evidence

- `../screenshots/06-failed-logins/01-kali-smbclient-failed-login.png`
- `../screenshots/06-failed-logins/02-splunk-4625-failed-login-overview.png`
- `../screenshots/06-failed-logins/03-failed-login-event-details-kali-source.png`

## Key Findings

- The Kali command `smbclient -L //192.168.56.1 -U fakeuser` generated an SMB authentication failure.
- Windows logged the failed authentication as Security Event ID 4625.
- Splunk ingested and displayed the failed login event from `WinEventLog:Security`.
- The expanded event showed `Account_Name=fakeuser`, `Workstation_Name=KALI`, and `Failure_Reason=Unknown user name or bad password`.

## MITRE ATT&CK Mapping

- T1110 - Brute Force

## Analyst Assessment

Repeated failed login attempts may indicate password guessing, brute-force activity, misconfigured services, or user error. Source IP, username, logon type, and failure reason should be reviewed.

## Recommendations

- Monitor repeated failures by source IP and account
- Enable account lockout policies
- Enforce strong passwords
- Disable unnecessary exposed services
- Investigate successful logins following repeated failures
