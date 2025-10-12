#!/usr/bin/env python3
"""Simple Nmap XML parser to CSV.

Usage: python3 nmap_parse.py nmap_output.xml out.csv
"""
import sys
import xml.etree.ElementTree as ET
import csv

def parse_nmap(xmlfile, csvfile):
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    with open(csvfile, 'w', newline='') as fh:
        writer = csv.writer(fh)
        writer.writerow(['host','port','protocol','state','service','version'])
        for host in root.findall('host'):
            addr = host.find('address').get('addr') if host.find('address') is not None else 'unknown'
            for port in host.findall('.//port'):
                p = port.get('portid')
                proto = port.get('protocol')
                state = port.find('state').get('state')
                svc = port.find('service')
                svcname = svc.get('name') if svc is not None else ''
                version = svc.get('version') if svc is not None and 'version' in svc.keys() else ''
                writer.writerow([addr,p,proto,state,svcname,version])
    print('Wrote', csvfile)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('Usage: nmap_parse.py nmap_output.xml out.csv'); sys.exit(1)
    parse_nmap(sys.argv[1], sys.argv[2])
