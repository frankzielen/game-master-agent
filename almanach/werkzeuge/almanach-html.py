#!/usr/bin/env python3
"""Baut die SL-Website: alle Markdown-Dateien des Almanachs zum Durchklicken, mit Ordnerbaum, Suche, Bildern und „Erwähnt in“.
Aufruf (im Hauptordner des Almanachs): python3 werkzeuge/almanach-html.py [ausgabe-ordner]
Ohne Angabe entsteht _site/sl/spielleiter.html (dazu index.html als Weiterleitung). Bilder und Medien (PDF, MP3, TXT) werden als Dateien daneben kopiert. Quellen (_quelle/) sind enthalten, zählen aber nicht für „Erwähnt in“.
Die SL-Website enthält auch alle Geheimnisse: nicht öffentlich ins Netz stellen."""
import os, sys, re, posixpath, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gma_basis import ROOT, IMG, einstellungen, template, schreibe_seite

TOP = ['README.md', 'offene-punkte.md', 'abenteuer', 'welt', 'systeme', '_vorlagen']
MEDIEN = ('.pdf', '.mp3', '.ogg', '.wav', '.m4a', '.flac', '.txt')
docs, imgs = {}, {}
for t in TOP:
    p = os.path.join(ROOT, t)
    if not os.path.exists(p): continue
    walk = [(ROOT, [], [t])] if os.path.isfile(p) else os.walk(p)
    for dp, dn, fn in walk:
        for f in fn:
            full = os.path.join(dp, f); rel = os.path.relpath(full, ROOT).replace(os.sep, '/')
            if f.endswith('.md'):
                docs[rel] = open(full, encoding='utf-8').read()
            elif f.lower().endswith(IMG):
                imgs[rel] = urllib.parse.quote(rel)
TOP = [t for t in TOP if any(d == t or d.startswith(t + '/') for d in docs)]

# Verlinkte Medien (auch aus _quelle/, z. B. das Original-PDF)
medien = set()
for rel, txt in docs.items():
    for href in re.findall(r'\]\(([^)\s]+)', txt):
        if href.startswith(('http', '#')) or not href.lower().endswith(MEDIEN): continue
        z = posixpath.normpath(posixpath.join(posixpath.dirname(rel), urllib.parse.unquote(href)))
        if os.path.isfile(os.path.join(ROOT, z)): medien.add(z)
medien = sorted(medien)

# „Erwähnt in“ aus den Links (Ideen-Eingänge, Quellen und Vorlagen zählen nicht)
def ziel(p):
    if p in docs: return p
    p = p.rstrip('/')
    for c in (p + '/README.md', p + '/' + p.split('/')[-1] + '.md'):
        if c in docs: return c
rueck = {}
for rel, txt in docs.items():
    if rel.endswith('ideen-eingang.md') or rel.startswith(('_vorlagen/', 'systeme/')) or '/_quelle/' in rel: continue
    for href in re.findall(r'\]\(([^)\s]+)', txt):
        if href.startswith(('http', '#', 'mailto:')): continue
        z = ziel(posixpath.normpath(posixpath.join(posixpath.dirname(rel), urllib.parse.unquote(href.split('#')[0]))))
        if z and z != rel: rueck.setdefault(z, set()).add(rel)
rueck = {k: sorted(v) for k, v in rueck.items()}

e = einstellungen()
ausgabe = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, '_site', 'sl')
datei = schreibe_seite(ausgabe, template(e['titel'], e.get('untertitel', '')),
                       {'docs': docs, 'imgs': imgs, 'top': TOP, 'medien': medien, 'rueck': rueck}, list(imgs) + medien,
                       'spielleiter')
print(f'SL-Website: {len(docs)} Dokumente, {len(imgs)} Bilder, {len(medien)} Medien -> {datei}')
