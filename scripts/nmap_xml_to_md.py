#!/usr/bin/env python3
import sys
import xml.etree.ElementTree as ET

def parse_nmap(xmlfile):
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    hosts = []
    for host in root.findall('host'):
        addr_node = host.find('address')
        addr = addr_node.get('addr') if addr_node is not None else 'unknown'
        ports = []
        ports_node = host.find('ports')
        if ports_node is not None:
            for p in ports_node.findall('port'):
                portnum = p.get('portid')
                proto = p.get('protocol')
                state = p.find('state').get('state') if p.find('state') is not None else ''
                svc = p.find('service')
                svcname = svc.get('name') if svc is not None and 'name' in svc.attrib else ''
                version = svc.get('version') if svc is not None and 'version' in svc.attrib else ''
                ports.append({'port': portnum, 'proto': proto, 'state': state, 'service': svcname, 'version': version})
        hosts.append({'addr': addr, 'ports': ports})
    return hosts

def to_md(hosts):
    out = []
    for h in hosts:
        out.append(f"## Host: {h['addr']}\n\n")
        if not h['ports']:
            out.append("_No open ports found_\n\n")
            continue
        out.append("| Port | Proto | State | Service | Version |\n")
        out.append("|---|---:|---|---|---:|\n")
        for p in h['ports']:
            out.append(f"| {p['port']} | {p['proto']} | {p['state']} | {p['service']} | {p['version']} |\n")
        out.append("\n")
    return ''.join(out)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: nmap_xml_to_md.py <nmap.xml>')
        sys.exit(1)
    hosts = parse_nmap(sys.argv[1])
    print(to_md(hosts))
