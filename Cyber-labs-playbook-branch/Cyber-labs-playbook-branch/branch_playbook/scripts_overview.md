# scripts_overview.md — Scripts included & why they matter

This branch contains safe, educational scripts and template helpers. They do NOT perform attacks automatically.

## Included scripts (why you'll use them)
- `nmap_parse.py` — Parse `nmap` XML output into a CSV summary of hosts/ports/services. Useful to transform scan output for reports.
- `hash_check.py` — Compute SHA256/MD5 of files (evidence verification).
- `recon_generator.py` — Generates copy/paste command templates for recon (nmap/gobuster/rustscan) for consistent workflows.
- `john_helper.sh` — wrapper that prints the exact `ssh2john` + `john` commands to use (doesn't run them; you run locally).

## How to use
- Keep scripts in `scripts/` and mark executable. Use them to standardize outputs and accelerate report writing.
