# Ethical Hacking Framework

> WARNING: Use this framework only in authorized lab environments (TryHackMe, HackTheBox, CTF).

## Step 1 — Information Gathering (Passive / OSINT)
- OSINT: company names, emails, public assets.
- Google Dorking for discovery.

## Step 2 — Enumeration / Scanning (Active Recon)
- nmap scans:
  - `-p` select ports; `-p-` all ports; `-F` 100 most common
  - `-sU` UDP; `-sV` version detection; `-sC` default NSE scripts
  - `--script="script"` to run specific NSE scripts (e.g., ftp-anon)
- Interpret open ports as a checklist: how to access each (ftp, ssh, http, smb).
- Web discovery: gobuster/ffuf/dirb for directories, DNS, and vhosts.
- Wordlists: SecLists (subdomains), dirbuster lists, rockyou.

## Step 3 — Exploitation (Initial Access)
- Hydra for online password guessing (authorized only). Confirm form/endpoint.
- Web shells: upload only inside lab VMs; set listener; stabilize shell with `python3 -c 'import pty; pty.spawn("/bin/bash")'`.

## Step 4 — Post-Exploitation / Privilege Escalation
- `sudo -l`, check home directories, `.ssh`, `.bash_history`
- Check `/etc/passwd`, `/etc/group`, `/etc/shadow` (if readable)
- Find SUID binaries:
  - `find / -type f -perm -04000 2>/dev/null`
  - Ignore `/snap` and some lib dirs for noise
- Use GTFOBins to analyze SUID/sudoable binaries
- Cracking hashes: use John + hash-id to identify formats
