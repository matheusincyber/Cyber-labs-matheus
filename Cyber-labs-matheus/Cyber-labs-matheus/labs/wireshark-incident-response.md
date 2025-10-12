# Wireshark — Incident Response / Packet Analysis (cleaned lab)

## Summary of the capture
The PCAP shows an FTP brute-force (hydra) against user 'jenny', a successful login, upload of `shell.php`, retrieval of pentestmonkey reverse-shell URL, and subsequent shell stabilization and root actions (sudo, downloads).

## Key findings (answers)
1. Service targeted: FTP (port 21)
2. Tool: hydra
3. Username: jenny
4. Password found in capture: password123
5. FTP working dir after login: /var/www/html
6. Backdoor filename: shell.php
7. Backdoor URL: http://pentestmonkey.net/tools/php-reverse-shell
8. Post-shell command: whoami
9. Hostname: wir3
10. TTY spawn command: python3 -c 'import pty; pty.spawn("/bin/bash")'
11. Root escalation: sudo su
12. GitHub project downloaded: Reptile
13. Backdoor type: Rootkit

## Remediation suggestions
- Disable anonymous FTP / enforce secure authentication.
- Restrict CMS file editing and audit theme edits.
- Monitor and block unauthorized outbound connections.
