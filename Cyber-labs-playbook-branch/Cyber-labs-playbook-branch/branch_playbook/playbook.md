# Playbook — Practical Pentest & SOC Prep (branch: playbook)
**Purpose:** step-by-step, exam-ready methodology integrating your bootcamp PDFs and lab notes (Mr Robot, Wireshark, Basic Pentesting). Use in authorized lab environments only.

---
## Quick orientation (how to use this playbook)
1. Read this playbook sequentially before any practical test.  
2. Practice the commands in a disposable VM or TryHackMe lab.  
3. Keep `notes/raw_notes.md` open for your original observations and examples.  
4. Use `commands.md` as a quick reference during practice.  
5. Use the `scripts/` utilities to parse outputs or generate command scaffolds — they do not perform attacks automatically.

---
## High-level stages (repeat for each target)
1. **Preparation & OPSEC**
   - Confirm authorization. Use an isolated attack lab VM. Snapshot before/after.
   - Set up your tools: Kali/Parrot VM, Python, John, Nmap, Gobuster, Hydra, Wireshark, Netcat.
   - Start logging: create a directory `~/labs/<machine>/` for outputs (nmap/, gobuster/, pcaps/, notes/).

2. **Passive Recon (OSINT)**
   - Domain lookup, Google dorking, subdomain lists, public repos, LinkedIn for usernames.
   - Save findings to `notes/osint.md` (who, what, scope).

3. **Active Recon / Scanning**
   - Fast port discovery (RustScan) or Nmap top ports: `nmap -sC -sV -oA nmap_output <IP>`
   - Full TCP scan if needed: `nmap -p- -T4 <IP>` then targeted service scans on open ports.
   - Web discovery: `gobuster dir -u http://<host> -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 50 -o gobuster.txt`
   - Save all outputs: XML/JSON for parsing later.

4. **Service Enumeration (per service)**
   - **HTTP/HTTPS**: check robots.txt, sitemap, JS files, hidden folders, login pages.
   - **FTP/SMB**: test anonymous login, list/share enumeration (`smbclient -L //<IP> -N`), download interesting files.
   - **SSH**: check banner, try valid creds, inspect public files for keys.
   - **Databases / other**: follow service-specific workflows (MySQL, Redis, etc.).

5. **Initial Access**
   - Use weak creds, file uploads, RCE via vulnerable components (only in labs). Example: WordPress file edit -> upload PHP reverse shell (in lab only).
   - For brute-force: use Hydra carefully and only in lab contexts. Example: `hydra -l jenny -P /usr/share/wordlists/rockyou.txt ftp://<IP>`
   - If you get a web shell, set up listener (`nc -lvnp 4444`) and trigger the payload.

6. **Stabilize shell & gather**
   - Stabilize: `python3 -c 'import pty; pty.spawn("/bin/bash")'`, `export TERM=xterm`
   - Enumerate: `id`, `whoami`, `hostname`, `ip a`, `ps aux`, `ss -tulpn`, `mount`, `df -h`
   - Look for credentials: `/home/*/.ssh/*`, `/etc/passwd`, `find / -type f -name "*pass*" -o -name "*key*"`

7. **Privilege Escalation**
   - Sudo checks: `sudo -l`
   - SUID discovery: `find / -perm -4000 2>/dev/null`
   - Check GTFOBins for SUID exploitation patterns.
   - Check for exposed SSH keys and crack passphrases via `ssh2john.py` + `john`.

8. **Post-Exploitation & Evidence**
   - Capture `root.txt` or flags (lab only). Collect forensic traces: `/var/log/*`, `~/.bash_history` (note potential clearing by attacker).
   - Create a clean report with commands, timestamps, screenshots, and remediation.

9. **Cleanup & Reporting**
   - Do not leave backdoors in real systems. In lab, document actions and revert VMs.
   - Write a post-mortem with indicators of compromise (IOCs).

---
## Test-day strategy (time-boxed)
- First 10 minutes: scope, scope limitations, and host reachability. Write a short plan.  
- Next 30 minutes: fast nmap + web enumeration (identify 1–2 promising vectors).  
- Next 45 minutes: attempt initial access methods prioritized: creds, file uploads, RCE.  
- Final hour: privilege escalation, capture artifacts, and write concise report (commands + outputs).

---
## Where your notes live in this branch
- `notes/raw_notes.md` — your original lab notes (verbatim excerpts & cleaned snippets). Keep adding.  
- `docs/` — cleaned weekly materials (from PDFs).

---
## Ethical reminder
This playbook is oriented to labs and authorized testing only. Never attempt these techniques on unapproved targets.
