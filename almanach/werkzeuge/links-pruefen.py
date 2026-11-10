#!/usr/bin/env python3
"""Prüft alle relativen Markdown-Links des Almanachs und meldet tote Links.
Aufruf (im Hauptordner des Almanachs): python3 werkzeuge/links-pruefen.py"""
import os, re, sys
from urllib.parse import unquote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUSLASSEN = {'_vorlagen', 'systeme', 'werkzeuge', '.git'}
tot, anzahl = [], 0
for dp, dn, fn in os.walk(ROOT):
    dn[:] = [d for d in dn if d not in AUSLASSEN]
    for f in fn:
        if not f.endswith('.md'):
            continue
        p = os.path.join(dp, f)
        text = open(p, encoding='utf-8').read()
        text = re.sub(r'```.*?```', '', text, flags=re.S)  # Codeblöcke und
        text = re.sub(r'`[^`\n]*`', '', text)                # Inline-Code sind Beispiele, keine Links
        for ziel in re.findall(r'\]\(([^)\s]+)', text):
            if re.match(r'^[a-z]+:', ziel) or ziel.startswith('#'):
                continue
            pfad = ziel.split('#')[0]
            if not pfad:
                continue
            anzahl += 1
            if not os.path.exists(os.path.normpath(os.path.join(dp, unquote(pfad)))):
                tot.append(f'{os.path.relpath(p, ROOT)} -> {ziel}')
print('\n'.join(tot))
print(f'{anzahl} Links geprüft, {len(tot)} tot.')
sys.exit(1 if tot else 0)
