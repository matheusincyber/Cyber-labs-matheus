# ETHICAL HACKING FRAMEWORK — Cleaned & Expanded

> Lab-only / authorized testing. Use only in TryHackMe / HackTheBox / your VMs or systems with explicit permission.

---

## Overview — high level flow
1. **Information Gathering (Passive Recon)**  
2. **Enumeration & Scanning (Active Recon)**  
3. **Vulnerability Analysis & Prioritisation**  
4. **Exploitation (Lab-only, controlled & non-destructive)**  
5. **Post-Exploitation / Privilege Escalation**  
6. **Lateral Movement & Persistence (defense-focused)**  
7. **Cleanup, Reporting & Remediation**

---

## Step 1 — Information Gathering (Passive)
**Purpose:** build hypotheses without touching target systems.  
**Techniques / tools:** OSINT, Google Dorking, crt.sh, Shodan, public repos (GitHub), LinkedIn for target roles, public DNS records.  
**What to record:** domains, subdomains, exposed emails, potential admin pages, employee usernames, public certs (SNI).  
**Defender signal:** sudden increase in passive DNS lookups for unusual names; new external DNS queries.

**Quick passive checks (no direct traffic):**
- crt.sh / certificate transparency lookups
- GitHub search for `org:target password` (only in permitted contexts)
- `whois` / public DNS records

---

## Step 2 — Enumeration & Scanning (Active)
**Purpose:** discover live hosts, open ports, services, versions — non-aggressive first, then targeted.  
**Important nmap options explained (safe usage):**
- `-sC` = run default NSE scripts (useful, but be mindful of intrusiveness)  
- `-sV` = service/version detection  
- `-p-` = scan all TCP ports (more noisy)  
- `-Pn` = skip host discovery (useful on VMs that drop ICMP)  
- `-sU` = UDP scan (very slow/noisy)  
- `-F` = scan top 100 ports (less noisy)

**Interpretation of results:** treat open ports as a checklist:
- Which protocol client can I use? (ftp, ssh, smbclient, http)
- Is service on default or non-default port?
- Are management ports exposed (e.g., 8080, 8443, custom admin ports)?

**Webapp enumeration (safe examples):**
- `gobuster dir -u http://<url> -w <wordlist> -x .php,.html -t 50 -r`  
- `gobuster vhost -u http://<ip> --domain target.tld -w <wordlist> --append-domain`

**Wordlists (use responsibly):**
- `/usr/share/wordlists/rockyou.txt`
- `/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt`
- `SecLists/Discovery/DNS/subdomains-top1million-5000.txt`

**Logs / SIEM to check for active recon:**
- Many `SYN` entries from single IP → port scan alert
- Many 4xx responses / repeated paths → enumeration
- Uncommon UA strings or spikes in specific endpoints

---

## Step 3 — Vulnerability Analysis & Prioritisation
**Purpose:** map discovered services to plausible weaknesses (expose → exploitability → impact).  
**Action:** for each service, note its CVE history, default creds, and exposed interfaces. Prioritise:
- Public-facing services first
- Services with known high-severity CVEs
- Services exposing management pages or upload features

**Useful resources:** NVD, Exploit-DB (read-only to learn), vendor advisories, CVE details.

---

## Step 4 — Exploitation (Lab-only)
**Rules:** only in authorized labs. Do not run destructive payloads. Capture all evidence (pcap + logs + screenshots).  
**High-level actions to understand (do not weaponize):**
- What payloads would change on the wire? (long POST bodies, SQL errors, unusual headers)
- What logs will show exploitation attempts? (webserver 500s, DB errors, sudden file writes)
- How to prove concept without persistent changes — evidence-based: screenshots, response bodies, logs.

**Defender signals:** unusual POST/GET patterns, long URL-encoded strings, repeated parameter patterns, new files created on webroot.

---

## Step 5 — Post-Exploitation / Privilege Escalation
**Goal:** escalate to a higher-priv account *in lab CTF contexts only* and document. Focus on detection signals for defenders.

**Quick enumeration checklist (benign commands you should memorize):**
- `whoami` — current user
- `id` — uid/gid info
- `uname -a` — kernel & OS info
- `cat /etc/os-release` — distro
- `ps aux` — running processes
- `ss -tulwn` or `netstat -tulpen` — listening sockets
- `ls -la /home` and `ls -la /root` — check home dirs
- `cat /etc/passwd` and `cat /etc/group` — user lists
- `sudo -l` — allowed sudo commands (very important)

**SUID / Permission checks:**
- `find / -type f -perm -04000 2>/dev/null` — find SUID files  
  *Investigate SUID binaries via GTFOBins for possible escalation techniques (in lab only).*

**Files & creds to check:**
- `.bash_history`, `/home/*/.ssh`, `id_rsa` (private keys), config files, `.env` containing secrets
- `find / -name '*.env' -o -name '*.conf' -o -name '*.bak'` (be careful; only list, don’t exfiltrate)

**Password/Key cracking (lab):**
- Convert SSH private keys for cracking with `ssh2john.py` (John) — only for keys you found in the lab.  
- Always document the exact commands and files used; never publish leaked creds.

**Privilege escalation resources (read-only for study):**
- GTFOBins — patterns for common binaries
- LinPEAS / WinPEAS — automation scripts to enumerate possible escalation paths (do not blindly run on production)

**Defender signals to monitor for post-exploit:**
- New user accounts creation (check `/var/log/auth.log`, Windows Security logs)
- Unusual `sudo` activity
- Unexpected process creation or suspicious child processes (Sysmon process creation events)
- Large outbound connections or DNS beaconing

---

## Step 6 — Lateral Movement & Persistence (defense-focused)
**What attackers often try (know to detect):**
- Reuse of credentials to access other hosts (check repeated auth logs)
- SMB/Windows shares accessed from odd hosts (monitor SMB logs)
- Scheduled tasks / cron entries for persistence (`crontab -l`, `/etc/cron.*`)
- SSH agent forwarding abuse (detect via SSH logs or sudden key usage)

**Detection tips:**
- Correlate authentication logs across hosts for same username / source IP
- Monitor abnormal processes writing to unusual locations
- Watch for new services / listening ports after compromise

---

## Step 7 — Cleanup, Reporting & Remediation
**Always** document everything. A good report includes:
- Scope & preconditions
- Timeline of actions (UTC timestamps)
- Evidence: pcap files, log snippets, screenshots
- IOCs: IPs, domains, usernames, file paths
- Impact assessment & remediation steps (patch, rotate creds, harden configs)
- Detection tuning recommendations (SIEM rules to detect similar attempts)

**Quick one-page IR template (short):**
- Summary (1-2 lines)  
- Affected assets  
- Indicators of Compromise  
- Steps taken / recommended actions  
- Prevention & monitoring recommendations

---

## Extra: Useful Local/Enumeration Commands (Benign, memorize these)
- `ip a` / `ip addr show` — interfaces  
- `route -n` or `ip route` — routing table  
- `ss -tulwn` — listening sockets  
- `lsof -i` — open network files  
- `ps aux --sort=-%mem | head` — top processes  
- `df -h` — disk usage  
- `mount` — mounted filesystems  
- `grep -i 'password' -R /home 2>/dev/null` — quick search for possible credentials (lab only)

---

## SIEM / Detection Examples (study queries / patterns)
> Adapt these to Splunk/Elastic syntax in your lab

- **Failed logins by source IP (last 24h):** look for spikes and repeated failures.  
- **Port scan indicator:** many SYNs from single IP to many ports in short time window.  
- **Long POST bodies / base64 patterns:** indicate possible file upload or data exfil.  
- **Unusual user-agent or referrer spikes** hitting administrative endpoints.  
- **New SUID binary executions** or unusual commands executed by non-privileged users.

---

## Tools & Cheatsheet (recommended)
- Recon & scanning: `nmap`, `rustscan`, `masscan` (read only; masscan is very noisy)  
- Web enumeration: `gobuster`, `ffuf`  
- Wordlists: SecLists, rockyou, dirbuster lists  
- Cracking: `john`, `hashcat` (know the workflow to identify hash format)  
- Forensics: `Volatility`, `FTK Imager`  
- Malware analysis: `Procmon`, `strace`, sandboxing tools  
- PrivEsc helpers (study): `LinPEAS`, `WinPEAS`, `GTFOBins`  
- SIEM: Splunk / Elastic basics — ingestion, fields, queries

---

## Quick Ethics & Safety Reminder (put this at the top of your notes)
**Only perform scanning, enumeration, or exploitation in lab environments or against systems you own/have explicit written permission to test.** Unauthorized testing is illegal and unethical. Document permission and scope before any engagement.

---

## Further reading & practice (short list)
- OWASP Top 10 (web security fundamentals)  
- GTFOBins — common privilege escalation patterns  
- LinPEAS / WinPEAS walkthroughs (read the output and understand it)  
- TryHackMe rooms: Nmap, Web Fundamentals, OWASP, Linux Privesc  
- Books: “The Web Application Hacker’s Handbook” (use for learning, not attacking real sites)

---

## Final exam study tips (ADHD-friendly)
- Use short focused sessions (25–45 min) on one topic (e.g., nmap one session, gobuster another).  
- Keep a one-page printed checklist with the main workflow: Recon → Scan → Enum → Exploit (lab) → Post → Report.  
- After each lab, write a 5-minute one-paragraph summary (what you did, evidence, next steps). That reinforces memory and creates material for your GitHub.

---

**Notes:** I intentionally avoided step-by-step exploit payloads or dangerous copy/paste commands. If you want, I can now:
- produce a cleaned **markdown file** of this content ready to upload, and
- append SIEM-style example queries (Splunk/Elastic) that are safe and detection-focused.

Which do you prefer next?
