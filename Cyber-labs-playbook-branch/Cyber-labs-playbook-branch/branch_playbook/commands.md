# commands.md — Commands you should know (what they do + examples)

## Scanning & Recon
- `nmap -sC -sV -oA nmap_output <IP>` : run default NSE scripts and version detection, save outputs in all formats.
- `nmap -p- -T4 <IP>` : scan all TCP ports with a faster timing option.
- `rustscan -a <IP> -- -sC -sV` : fast port discovery using RustScan then hand off to nmap.
- `gobuster dir -u http://<host> -w <wordlist> -t 50 -o gobuster.txt` : directory discovery for web apps.
- `ffuf -u http://<host>/FUZZ -w <wordlist>` : alternative to gobuster (faster, flexible).

## Web & File
- `curl -s -I http://<host>/robots.txt` : fetch robots headers (quick).
- `wget http://<host>/file -O file` : download a web file to disk.
- `ftp <IP>` : connect to FTP for manual interaction (use `get`, `put`).

## Bruteforce & Passwords (labs only)
- `hydra -l user -P /path/to/rockyou.txt ftp://<IP>` : brute-force FTP logins.
- `john --wordlist=/usr/share/wordlists/rockyou.txt hashfile` : crack hashes with John.
- `python3 /opt/john/ssh2john.py id_rsa > id_rsa_hash.txt` : convert private key for john.

## Shells & stabilization
- `nc -lvnp 4444` : netcat listener for reverse shells.
- `python3 -c 'import pty; pty.spawn("/bin/bash")'` : spawn TTY to improve shell interaction.
- `CTRL-Z ; stty raw -echo ; fg ; export TERM=xterm` : convert reverse shell to interactive terminal.

## SUID & Priv Esc
- `find / -type f -perm -4000 2>/dev/null` : find files with the SUID bit.
- `sudo -l` : list allowed sudo commands for current user.
- `gtfobins` : website to check exploitation techniques for binaries.

## Forensics & Logs
- `grep -i "error" /var/log/* 2>/dev/null | less` : quick logs scan.
- `tcpdump -w capture.pcap` : record network traffic to a pcap file (analyze in Wireshark).

## Helpful shell utilities
- `ss -tulpn` : list listening sockets & processes.
- `ps aux | egrep -i "ssh|nginx|apache|httpd|mysql"` : look for suspicious processes.
- `find / -name "*flag*" -type f 2>/dev/null` : search for flags in CTF/lab environments.

---
# Quick reference (one-liners)
- Full web enum -> `gobuster dir -u http://<host> -w /usr/share/wordlists/dirb/common.txt -t 50 -q -o gobuster.txt`
- Convert ssh key & crack -> `/opt/john/ssh2john.py id_rsa > id_rsa_hash.txt && john --wordlist=/usr/share/wordlists/rockyou.txt id_rsa_hash.txt`
- SUID escape (example) -> `nmap --interactive` then `!sh` (only if nmap is SUID and GTFOBins shows this works)


