# John the Ripper & Hash Cracking

## Tools
- john (John the Ripper)
- ssh2john.py (convert SSH key to john format)
- hash-id.py (identify common hash types)

## Workflow
1. Identify the hash type:
   - `python3 hash-id.py` or `python3 hash-id.py <hashfile>`
   - or inspect with `john --list=formats` / `grep` for likely formats
2. Convert keys when needed:
   - `python3 /opt/john/ssh2john.py id_rsa > id_rsa_hash.txt`
3. Crack with the correct format:
   - `john --format=raw-md5 --wordlist=/usr/share/wordlists/rockyou.txt hash_to_crack.txt`
4. Check john's pot file for recovered entries: `~/.john/john.pot`

Notes: always verify and redact sensitive artifacts before sharing.
