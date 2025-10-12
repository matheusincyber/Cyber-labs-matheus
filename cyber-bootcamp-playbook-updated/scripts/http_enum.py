#!/usr/bin/env python3
"""http_enum.py — simple path enumerator using requests (lab-only small helper)
Usage:
  python3 http_enum.py http://10.10.132.130 /usr/share/wordlists/common.txt
"""
import sys, requests, time
from urllib.parse import urljoin

def main():
    if len(sys.argv) < 3:
        print('Usage: http_enum.py <base_url> <wordlist>')
        sys.exit(1)
    base = sys.argv[1].rstrip('/') + '/'
    wl = sys.argv[2]
    delay = 0.05
    with open(wl, 'r', errors='ignore') as f:
        for line in f:
            path = line.strip()
            if not path:
                continue
            url = urljoin(base, path)
            try:
                r = requests.get(url, timeout=5, allow_redirects=True)
                if r.status_code < 400:
                    print(f"{r.status_code} {url}")
            except Exception as e:
                print(f"ERR {url} {e}")
            time.sleep(delay)

if __name__ == '__main__':
    main()
