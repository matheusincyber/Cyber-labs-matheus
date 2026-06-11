# 🔒 Cyber Labs — Matheus Carvalho

Hands-on cybersecurity labs, SOC notes, write-ups and small tools.

This repo is where I organize my learning from TryHackMe, Ironhack, Security+, home labs and personal cybersecurity projects.

The goal is to keep everything clean enough for recruiters, but still real enough to show the work behind it.

![Repo ready](https://img.shields.io/badge/repo-ready-brightgreen)
![Focus](https://img.shields.io/badge/focus-SOC%20%7C%20Blue%20Team%20%7C%20IR-blue)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

## Latest updates

✅ Added Mini SOC Lab with Splunk, Sysmon, Windows and Kali
✅ Added failed login detection using Windows Security Event ID 4625
✅ Added PowerShell execution detection using Sysmon Event ID 1
✅ Added Nmap scan simulation from Kali against a monitored Windows host
✅ Added cleaned Security+ study notes on CIA Triad and Access Controls
✅ Added sanitized TryHackMe Mr Robot walkthrough
✅ Added helper scripts for parsing, subnetting and basic enumeration

Coming soon:

✅ DNS Security Dashboard with ad blocking, DNS visibility and client monitoring
✅ Active Directory attack and defense lab
✅ Threat Intelligence lab with Python and IOC reporting
✅ More forensic walkthroughs and incident notes

## About me

I’m Matheus Carvalho.

I’m transitioning from production operations into cybersecurity, with a focus on SOC analysis, threat intelligence and incident response.

My background includes operational monitoring, incident escalation, process control, documentation and working under pressure in high-volume environments.

I’m using this repo to show practical progress, not just certificates or course names.

## Featured project: Mini SOC Lab

Path:

```text
labs/blue-team/mini-soc-lab/
```

This is a small SOC lab built with Windows, Kali Linux, Sysmon and Splunk.

The lab simulates basic suspicious activity and shows how it can be detected and investigated using logs.

Tools used:

```text
Windows
Kali Linux
Splunk
Sysmon
Windows Security logs
PowerShell
Nmap
SMB testing
MITRE ATT&CK
```

What it covers:

```text
Splunk log collection
Sysmon process monitoring
Windows authentication logs
PowerShell execution detection
Failed login detection
Nmap scan simulation
Incident reports
Detection notes
Screenshots
MITRE ATT&CK mapping
```

Detection examples:

| Scenario             | Log source                     | What it shows                               |
| -------------------- | ------------------------------ | ------------------------------------------- |
| PowerShell execution | Sysmon Event ID 1              | Process creation and command activity       |
| Failed login attempt | Windows Security Event ID 4625 | Bad username or password from Kali SMB test |
| Nmap scan simulation | Kali and Windows logs          | Basic reconnaissance against the lab host   |

Related folders:

```text
labs/blue-team/mini-soc-lab/detections/
labs/blue-team/mini-soc-lab/incident-reports/
labs/blue-team/mini-soc-lab/splunk-queries/
labs/blue-team/mini-soc-lab/screenshots/
```

## Coming soon: DNS Security Dashboard

Path:

```text
labs/blue-team/dns-security-dashboard/
```

This will be a home network project focused on DNS filtering, ad blocking and network visibility.

The idea is to build more than a basic adblocker. I want a dashboard that shows what is being blocked, which devices are active and which domains are being requested the most.

Planned features:

```text
Network-wide DNS filtering with Pi-hole or AdGuard Home
Blocked vs allowed DNS queries
Top blocked domains
Top allowed domains
Most active client IPs
Blocked requests per device
Recent suspicious domains
Query trends over time
Optional Grafana dashboard
Optional Python parser for custom reports
Possible traffic visibility later with router stats or ntopng
```

Skills this should show:

```text
DNS monitoring
Network visibility
Dashboarding
Log parsing
Python scripting
Home network hardening
Basic threat visibility
Privacy and tracker reduction
```

## Repo structure

```text
docs/
  Security+ notes
  networking notes
  SIEM notes
  forensics notes
  web security notes

labs/
  blue-team/
    mini-soc-lab/
    dns-security-dashboard/        coming soon

  tryhackme/
    mr-robot/
    wireshark-incident-response/
    basic-pentesting/

scripts/
  nmap_xml_to_md.py
  subnet_calc.py
  http_enum.py

tools/
  cheatsheet.md
```

## Why this repo exists

I want this repo to show how I learn and how I investigate.

For each serious lab, I try to include:

```text
The goal of the lab
The tools used
The commands or process followed
Screenshots
Detection logic
Incident notes
Defensive takeaways
Lessons learned
```

That is more useful than just saying “I know Splunk” or “I’m passionate about cybersecurity,” which everyone writes until LinkedIn turns into soup.

## Lab write-up policy

All write-ups are cleaned and sanitized.

I do not include private credentials, real public IPs, unauthorized targets or platform flags.

The focus is methodology, investigation process and defensive learning.

## Quick links

Docs: [`docs/`](docs/)
Labs: [`labs/`](labs/)
Blue Team Labs: [`labs/blue-team/`](labs/blue-team/)
Scripts: [`scripts/`](scripts/)
Cheatsheet: [`tools/cheatsheet.md`](tools/cheatsheet.md)
License: [`LICENSE`](LICENSE)

## Contact

Matheus Carvalho
Cybersecurity learner focused on SOC analysis, threat intelligence and incident response.

LinkedIn: https://www.linkedin.com/in/matheusincyber
Email: [matheusincyber@gmail.com](mailto:matheusincyber@gmail.com)
