#!/usr/bin/env python3
import sys, ipaddress

def print_info(net):
    print("Network:", net.network_address)
    print("Netmask:", net.netmask)
    print("Broadcast:", net.broadcast_address)
    if net.num_addresses >= 2:
        print("Hosts/usable:", net.num_addresses - 2)
        hosts = list(net.hosts())
        print("First host:", hosts[0])
        print("Last host:", hosts[-1])
    else:
        print("Hosts/usable:", net.num_addresses)

def main():
    if len(sys.argv) < 2:
        print("Usage: subnet_calc.py <network/cidr> or <network> <netmask>")
        sys.exit(1)
    if '/' in sys.argv[1]:
        net = ipaddress.ip_network(sys.argv[1], strict=False)
    else:
        if len(sys.argv) < 3:
            print("Provide netmask as second argument if not using CIDR.")
            sys.exit(1)
        net = ipaddress.ip_network(sys.argv[1] + '/' + sys.argv[2], strict=False)
    print_info(net)

if __name__ == '__main__':
    main()
