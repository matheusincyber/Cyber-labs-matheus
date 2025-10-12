#!/bin/bash
# john_helper.sh - prints recommended commands to convert an SSH key for john and run it.
if [ "$#" -ne 1 ]; then
  echo "Usage: john_helper.sh <path_to_id_rsa>"
  exit 1
fi
key="$1"
echo "# Convert key for john:"
echo "python3 /opt/john/ssh2john.py $key > ${key}_hash.txt"
echo "# Then crack with john (rockyou example):"
echo "john --wordlist=/usr/share/wordlists/rockyou.txt ${key}_hash.txt"
echo "# If you prefer hashcat, use appropriate hash mode after identifying the format."
