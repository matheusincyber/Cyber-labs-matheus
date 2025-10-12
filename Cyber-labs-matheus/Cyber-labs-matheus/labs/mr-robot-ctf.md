# Mr Robot CTF — TryHackMe (cleaned write-up)

> Lab: Mr Robot CTF — privilege escalation practice (Beginner → Intermediate).
> **Only use these steps in authorized lab environments (TryHackMe / HTB / VMs you own).**

## TL;DR / Objective
Root the Mr Robot VM and find three keys hidden on the machine. This write-up documents enumeration, initial access, and privilege escalation.

**Keys found**
- Key 1: 073403c8a58a1f80d943455fb30724b9
- Key 2: 822c73956184f694993bede3eb39f959
- Key 3: 04787ddef27c3dee1ee161b21670b4e4

## Summary steps (high-level)
1. nmap to find HTTP/HTTPS.
2. gobuster to find hidden files (robots, fsocity.dic, key-1-of-3.txt).
3. Decode base64 license -> credentials; login to WP as elliot.
4. Edit theme template (404.php) to include PHP reverse shell; start nc listener.
5. Stabilize shell with `python3 -c 'import pty; pty.spawn("/bin/bash")'`.
6. Find user secrets; crack an md5 secret with john.
7. Switch user (su robot) and find SUID `nmap`.
8. Use `nmap --interactive` -> `!sh` to get root and read final key.

## Defensive takeaways
- Prevent file-editing via CMS if not necessary.
- Monitor outbound connections from web servers.
- Avoid SUID on interactive tools; use least privilege.
