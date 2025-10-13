#!/usr/bin/env python3
"""report_builder.py — combine findings into a simple markdown report.
Usage:
  python3 report_builder.py findings_snippets/*.md > findings.md
"""
import sys, glob
parts = []
for pattern in sys.argv[1:]:
    for p in glob.glob(pattern):
        with open(p,'r',encoding='utf-8') as f:
            parts.append(f.read())
print('\n\n---\n\n'.join(parts))
