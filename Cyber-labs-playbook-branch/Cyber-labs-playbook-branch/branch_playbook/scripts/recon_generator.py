#!/usr/bin/env python3
"""Recon command generator - prints safe command templates for you to copy/paste into a terminal.
It does NOT run network scans by design (safer for interview prep).
Usage: python3 recon_generator.py <target_ip_or_domain>
"""
import sys
if len(sys.argv) != 2:
    print('Usage: recon_generator.py <target>'); sys.exit(1)
target = sys.argv[1]
print(f"# Nmap quick scan:\nnmap -sC -sV -oA nmap_{target} {target}\n")
print(f"# Rustscan fast discovery then nmap:\nrustscan -a {target} -- -sC -sV\n")
print(f"# Gobuster common directories:\ngobuster dir -u http://{target}/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -t 50 -o gobuster_{target}.txt\n")
print(f"# FFUF example (alternative):\nffuf -u http://{target}/FUZZ -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -t 50\n")
print('# Save outputs into a directory: mkdir -p ~/labs/{target} && mv nmap_* gobuster_* ~/labs/{target}/')

