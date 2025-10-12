# Gobuster & Web Enumeration

## Directory enumeration
gobuster dir -u http://10.10.132.130 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
gobuster dir -u http://10.10.132.130 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -r
gobuster dir -u http://10.10.132.130 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x .php,.js

# Small/common
gobuster dir -u http://www.offensivetools.thm -w /usr/share/wordlists/dirb/common.txt

## VHost & DNS
gobuster vhost -u "http://10.10.156.106" --domain www.offensivetools.thm -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt --append-domain --exclude-length 250-320

Notes:
- Use `-t` to tune threads; `-x` for extensions; `--append-domain` for full hostnames.
- Save results for reporting.
