#!/usr/bin/env python3
"""Compute SHA256 and MD5 for a file."""
import hashlib, sys

def hash_file(path):
    h_sha256 = hashlib.sha256()
    h_md5 = hashlib.md5()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h_sha256.update(chunk); h_md5.update(chunk)
    return h_sha256.hexdigest(), h_md5.hexdigest()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: hash_check.py <file>'); sys.exit(1)
    sha256, md5 = hash_file(sys.argv[1])
    print('SHA256:', sha256)
    print('MD5:   ', md5)
