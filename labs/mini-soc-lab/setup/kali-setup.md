# Kali Setup

## Purpose

Kali Linux is used as the attacker/simulation machine in this lab.

## Network Setup

The lab uses a VirtualBox host-only network.

```text
Windows host-only IP: 192.168.56.1
Kali attacker VM: VirtualBox host-only network
```

## Tools Installed

```bash
sudo apt update
sudo apt install nmap smbclient hydra netcat-openbsd curl whois dnsutils -y
```

## IP Validation

```bash
ip a
```

## Nmap Scan Used

```bash
nmap -Pn -sV 192.168.56.1
```

## Evidence

- `../screenshots/05-nmap-scan/01-kali-nmap-results.png`
- `../screenshots/01-setup/03-windows-hostonly-ip.png`
