#!/usr/bin/env python3
"""Baut die spoilerfreie Spieler-Website aus dem Almanach.
Aufruf (im Hauptordner des Almanachs): python3 werkzeuge/almanach-html-spieler.py [ausgabe-ordner] [markdown-export-ordner]
Ohne Angabe entsteht _site/spieler/spieler.html (dazu index.html als Weiterleitung), Bilder und Medien werden daneben kopiert.
Mit zweitem Argument zusätzlich Markdown-Export: alle Seiten mit Bildern als Ordner plus spielerseite.md in Lesereihenfolge.

Was hinein kommt, steuert der Spielstand, nicht ein fester Pfad:
- Ein Abenteuer abenteuer/NN-*/ ist freigegeben, sobald es gespielt ist oder läuft: README „**Status:** gespielt“
  mit Kapiteln, oder mindestens eine erfasste Sitzung (sitzungen/sitzung-*/). Abenteuer ohne Sitzung
  bleiben ganz draußen, auch jeder Link und jede Erwähnung als „NN · Titel“.
- Plot-Dateien nur mit Frontmatter „status: gespielt“ oder ohne Status (Übersichten, Sitzungen); Vorlagen bleiben draußen.
- Welt-Dateien nur, wenn „auftritte:“ ein freigegebenes Abenteuer enthält; die Kopfzeile zeigt nur diese Nummern.
- In jeder Datei fallen SL-Abschnitte weg (Geheim, Planung, offene Fäden, Aufhänger …) und Abschnitte
  zu nicht freigegebenen Abenteuern. Stat-Blöcke, Ideen-Eingänge, _quelle/ und _vorlagen/ sind nie dabei.
- Links auf Ausgelassenes werden zu Text; Links in nicht freigegebene Abenteuer und auf ausgelassene
  Welt-Einträge verschwinden samt Text.
- „Erwähnt in“ wird nur aus den Seiten der Spieler-Website berechnet.
- Einzelne Zeilen mit „(nur SL)“ fallen weg. Es gibt bewusst keine Ausnahmelisten im Code oder in Einstellungen:
  Was nicht für die Spieler ist, wird in den Daten gekennzeichnet.
- einstellungen.json liefert nur Titel, Untertitel, Titelbild und Einleitung der Startseite."""
import os, re, sys, json, posixpath, urllib.parse, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gma_basis import ROOT, IMG, einstellungen, template, schreibe_seite
MEDIEN = ('.mp3',)
E = einstellungen()
SP = E['spielerseite']

# Ganze Abschnitte (## Überschrift), die nie auf die Spieler-Website gehören
DROP_SECTIONS = {
    'Geheim (nur SL)', 'Aufhänger und Gerüchte', 'Konventionen', 'Hinweise zur Quelle',
    'Mögliche Enden', 'Handlungsstränge und Abzweigungen', 'Abzweigungen', 'Offene Ideen', 'Treibende Kräfte',
    'Verbindung zu früheren Abenteuern', 'Proben, Kampf, Hindernisse', 'Für nächstes Mal vorbereiten', 'Musik und Geräusche',
}
DROP_PREFIX = ('Offene Fäden', 'Persönliche Aufhänger', 'Stand zu Beginn', 'Bereits angelegte Welt-Einträge')
# Einzelne Zeilen (SL-Arbeitsnotizen, Quellenhinweise, Stat-Blöcke, Vorlagenhinweise)
DROP_LINES = [re.compile(p) for p in (
    r'^\*\*Stat-Block:\*\*', r'_quelle', r'_vorlagen', r'^>\s*Hinweis:', r'^_Gilt für alle Abenteuer',
    r'SL-Wissen', r'siehe Geheim', r'nur SL', r'\(Planung', r'Parallelhandlung', r'^\*\*Quelle:\*\*')]

def lies(p): return open(p, encoding='utf-8').read()
def kopf(text):
    m = re.match(r'^---\n(.*?)\n---\n?', text, re.S)
    return m.group(1) if m else ''
def feld(text, name):
    s = re.search(rf'^{name}:\s*(.*)$', kopf(text), re.M)
    return s.group(1).strip() if s else None

# --- Abenteuer: freigegeben = gespielt mit Material, oder mindestens eine erfasste Sitzung
abenteuer, gesperrt = [], []
ab_root = os.path.join(ROOT, 'abenteuer')
for d in sorted(os.listdir(ab_root)) if os.path.isdir(ab_root) else []:
    readme = os.path.join(ab_root, d, 'README.md')
    if not os.path.isfile(readme): continue
    txt = lies(readme)
    m = re.search(r'^#\s+(\d+)\s*·\s*(.+)$', txt, re.M)
    nr, titel = (m.group(1).zfill(2), m.group(2).strip()) if m else (d[:2], d)
    name = re.sub(r'\s*\(.*\)\s*$', '', titel)
    plot, sitz = os.path.join(ab_root, d, 'plot'), os.path.join(ab_root, d, 'sitzungen')
    kapitel = os.path.isdir(plot) and any(x.startswith('kapitel-') for x in os.listdir(plot))
    sitzungen = os.path.isdir(sitz) and any(x.startswith('sitzung-') for x in os.listdir(sitz))
    gespielt = re.search(r'\*\*Status:\*\*\s*gespielt', txt) is not None
    eintrag = {'ordner': d, 'nr': nr, 'name': name, 'titel': titel, 'laeuft': not gespielt}
    (abenteuer if (gespielt and kapitel) or sitzungen else gesperrt).append(eintrag)
frei_nrs = {a['nr'] for a in abenteuer}
frei_namen = [a['name'] for a in abenteuer]
# Woran man ein nicht freigegebenes Abenteuer im Text erkennt: „04 · Titel“, Ordnername, Überschriften mit dem Titel
gesperrt_marken = [f"{a['nr']} · {a['name']}" for a in gesperrt] + [a['ordner'] for a in gesperrt]
gesperrt_namen = [a['name'] for a in gesperrt]

def auftritte(text):
    a = re.search(r'^auftritte:\s*\[([^\]]*)\]', kopf(text), re.M)
    return None if not a else [x.strip().zfill(2) for x in a.group(1).split(',') if x.strip()]

docs, imgs, verborgen = {}, {}, set()
def sammle(start, welt):
    for dp, dn, fn in os.walk(start):
        dn[:] = [x for x in dn if not x.startswith('_')]
        for f in fn:
            full = os.path.join(dp, f); rel = os.path.relpath(full, ROOT).replace(os.sep, '/')
            if f.endswith('.md'):
                t = lies(full)
                # Statblocks von NSCs bleiben SL-Wissen, die der Spielercharaktere sehen die Spieler
                ok = f != 'ideen-eingang.md' and (f != 'statblock.md' or rel.startswith('welt/spielercharaktere/'))
                if welt:
                    au = auftritte(t)
                    ok = ok and (au is None or any(x in frei_nrs for x in au))
                else:
                    ok = ok and feld(t, 'status') in (None, 'gespielt')
                if ok: docs[rel] = t
                else: verborgen.add(rel)
            elif f.lower().endswith(IMG):
                imgs[rel] = urllib.parse.quote(rel)
for a in abenteuer: sammle(os.path.join(ab_root, a['ordner']), False)
sammle(os.path.join(ROOT, 'welt'), True)
# Leere Übersichten (Quests ohne Quest-Dateien) weglassen
for rel in list(docs):
    if rel.endswith('/quests/README.md') and not any(d.startswith(posixpath.dirname(rel) + '/quest-') for d in docs):
        del docs[rel]; verborgen.add(rel)

# Ordner ausgelassener Welt-Einträge (für Verzeichnisbäume in Übersichten), nur wenn darin nichts gezeigt wird
verborgen_ordner = set()
for rel in verborgen:
    if rel.startswith('welt/'):
        for o in posixpath.dirname(rel).split('/')[1:]:
            if not any(d.startswith('welt/') and f'/{o}/' in d for d in docs): verborgen_ordner.add(o)

def abschnitt_weg(titel):
    if titel in DROP_SECTIONS or titel.startswith(DROP_PREFIX) or any(w in titel for w in ('nur SL', 'Planung', 'Parallelhandlung')): return True
    if re.match(r'(In|Neu in)\s', titel):   # „In 03 · Titel“, „Neu in „Titel““
        return not any(n in titel for n in frei_namen) or any(n in titel for n in gesperrt_namen)
    return any(n in titel for n in gesperrt_marken)

def filtern(text):
    out, skip, sub_skip = [], False, False
    for line in text.split('\n'):
        m = re.match(r'^(#{1,4})\s+(.*\S)\s*$', line)
        if m and len(m.group(1)) <= 2:
            skip = len(m.group(1)) == 2 and abschnitt_weg(m.group(2))
            sub_skip = False
        elif m and not skip:
            # „### NN · Titel“ in „Entwicklung über die Abenteuer“: nur freigegebene Abenteuer zeigen
            nr = re.match(r'^(\d\d)\b', m.group(2))
            sub_skip = (bool(nr) and nr.group(1) not in frei_nrs) or abschnitt_weg(m.group(2))
        stand = re.match(r'^\*\*Aktueller Stand \((\w+) (\d\d)\b', line)
        if stand and (stand.group(1) != 'nach' or stand.group(2) not in frei_nrs or 'noch nicht zusammengefasst' in line):
            continue
        if skip or sub_skip or any(p.search(line) for p in DROP_LINES) or any(n in line for n in gesperrt_marken):
            continue
        # Verzeichnisbaum in Übersichten: Zeilen zu ausgelassenen Welt-Ordnern
        if re.match(r'^\s+[\w-]+/\s', line) and re.match(r'^\s+([\w-]+)/', line).group(1) in verborgen_ordner:
            continue
        out.append(line)
    return re.sub(r'\n{3,}', '\n\n', '\n'.join(out)).rstrip() + '\n'

def kopf_bereinigen(text):
    k = kopf(text)
    if not k: return text
    zeilen = []
    for z in k.split('\n'):
        if z.startswith('auftritte:'):
            z = 'auftritte: [' + ', '.join(x for x in auftritte(text) if x in frei_nrs) + ']'
        elif z.startswith('tags:'):
            weg = {a['ordner'][3:] for a in gesperrt} | {'statblock', 'planung'}
            tags = [t.strip() for t in z[5:].strip().strip('[]').split(',') if t.strip() and t.strip() not in weg]
            z = 'tags: [' + ', '.join(tags) + ']'
        elif z.startswith('status:') and z.split(':', 1)[1].strip() != 'gespielt':
            continue
        elif z.startswith('alias:'):
            # nur Namen behalten, die auf der Spieler-Website ohnehin im Text stehen (sonst verrät der Suchbegriff mehr)
            rumpf = text[len(k):]
            namen = [n.strip() for n in z[6:].strip().strip('[]').split(',') if n.strip() and n.strip() in rumpf]
            if not namen: continue
            z = 'alias: [' + ', '.join(namen) + ']'
        zeilen.append(z)
    return '---\n' + '\n'.join(zeilen) + '\n---\n' + text[len(re.match(r'^---\n.*?\n---\n?', text, re.S).group(0)):]

# --- Startseite und Abenteuer-Übersicht für Spieler
def einstieg(a):
    h = f"abenteuer/{a['ordner']}/plot/hauptplot.md"
    return h if h in docs else f"abenteuer/{a['ordner']}/README.md"
zeilen = '\n'.join(f"| {a['nr']} | [{a['name']}]({einstieg(a)}) | {'läuft' if a['laeuft'] else 'gespielt'} |" for a in abenteuer)
cover = SP.get('cover', '')
if cover and os.path.isfile(os.path.join(ROOT, cover)):
    imgs[cover] = urllib.parse.quote(cover)
    quelle = SP.get('cover_quelle', '')
    cover_md = f"![{SP.get('titel', 'Spieler-Website')}]({cover})\n" + (f"_Quelle: {quelle}_\n" if quelle else '') + "\n"
else:
    cover_md = ''
stand = datetime.date.today().strftime('%d.%m.%Y')
TITEL = SP.get('titel') or 'Heldentagebuch'
docs['README.md'] = f"""# {TITEL}

{cover_md}{SP.get('einleitung', '')}
Links öffnen die jeweilige Seite, oben links könnt ihr suchen. Stand: {stand}.

## Abenteuer
| # | Abenteuer | |
|---|---|---|
{zeilen}

## Die Welt
| Bereich | Einstieg |
|---|---|
| Eure Helden | [Spielercharaktere](welt/spielercharaktere/README.md) |
| Wer ist wer | [NSCs](welt/nscs/README.md) |
| Wo war das? | [Orte und Karten](welt/orte/README.md) |
| Mächte der Welt | [Fraktionen](welt/fraktionen/README.md) |
| Beute | [Gegenstände](welt/gegenstaende/README.md) |
"""
docs['abenteuer/README.md'] = "# Abenteuer\n\nAlle Abenteuer der Heldengruppe, der Reihe nach.\n\n| # | Abenteuer | |\n|---|---|---|\n" + \
    '\n'.join(f"| {a['nr']} | [{a['titel']}]({a['ordner']}/README.md) | {'läuft' if a['laeuft'] else 'gespielt'} |" for a in abenteuer) + '\n'

def ziel(basis, href):
    p = posixpath.normpath(posixpath.join(basis, urllib.parse.unquote(href.split('#')[0]))).rstrip('/')
    return p
def ziel_da(basis, href):
    p = ziel(basis, href)
    if p in docs or p in imgs: return True
    if p.lower().endswith(MEDIEN) and '_quelle' not in p and not geheim_ziel(basis, href) and os.path.isfile(os.path.join(ROOT, p)): return True
    if p + '/README.md' in docs or f'{p}/{p.split("/")[-1]}.md' in docs: return True
    return any(d.startswith(p + '/') for d in docs)
def geheim_ziel(basis, href):
    # Links in nicht freigegebene Abenteuer oder auf ausgelassene Welt-Einträge: samt Text entfernen
    p = ziel(basis, href)
    if any(p.startswith(f"abenteuer/{a['ordner']}") for a in gesperrt): return True
    return p.startswith('welt/') and (p in verborgen or p + '/' + p.split('/')[-1] + '.md' in verborgen)

LINK = re.compile(r'(!?)\[([^\]]*)\]\(([^)\s]+)\)')
def extern(href): return re.match(r'^(https?:|#|mailto:)', href)
def links(rel, text):
    basis = posixpath.dirname(rel)
    def weg(m):
        bild, txt, href = m.groups()
        return not bild and not extern(href) and not ziel_da(basis, href)
    zeilen = []
    for line in text.split('\n'):
        ls = list(LINK.finditer(line))
        if line.startswith('|') and ls and weg(ls[0]):
            continue   # Tabellenzeile, deren Eintrag (erster Link) nicht auf der Spieler-Website ist
        if ls and any(not m.group(1) and not extern(m.group(3)) and geheim_ziel(basis, m.group(3)) for m in ls):
            line = LINK.sub(lambda m: '' if (not m.group(1) and not extern(m.group(3)) and geheim_ziel(basis, m.group(3))) else m.group(0), line)
            line = re.sub(r'\s*·\s*(Danach|Davor):\s*(?=·|$)', '', line)
            line = re.sub(r'(\s*[,·]\s*)+(?=\s*[,·]|\s*$)', '', re.sub(r':\*\*\s*[,·]\s*', ':** ', line)).rstrip()
            line = re.sub(r'(\(\s*\)|\[\s*\])', '', line).rstrip()
            if re.match(r'^\s*-\s*(\*\*[^*]+:\*\*)?\s*$', line) or re.match(r'^\s*\*\*[^*]+:\*\*\s*$', line): continue
        if re.match(r'^\s*- \*\*[^*]+:\*\*', line) and ls:
            line = LINK.sub(lambda m: '' if weg(m) else m.group(0), line)
            line = re.sub(r'(\s*[,·]\s*)+(?=\s*[,·]|\s*$)', '', re.sub(r':\*\*\s*[,·]\s*', ':** ', line)).rstrip()
            if not LINK.search(line): continue
        zeilen.append(line)
    text = '\n'.join(zeilen)
    def ersetze(m):
        bild, txt, href = m.groups()
        if extern(href) or ziel_da(basis, href): return m.group(0)
        return '' if bild else txt
    return LINK.sub(ersetze, text)

for rel in list(docs):
    if rel not in ('README.md', 'abenteuer/README.md'):
        docs[rel] = kopf_bereinigen(filtern(docs[rel]))
    docs[rel] = links(rel, docs[rel])

# Abenteuer-Übersichten für Spieler neutral formulieren
for a in abenteuer:
    r = f"abenteuer/{a['ordner']}/README.md"
    if r not in docs: continue
    t = docs[r]
    if a['laeuft']:
        t = re.sub(r'\*\*Status:\*\*\s*\S+( \S+)?(?= ·|$)', '**Status:** läuft', t, count=1, flags=re.M)
    t = '\n'.join(l for l in t.split('\n') if not l.startswith('| Quelle |'))
    docs[r] = re.sub(r'\n{3,}', '\n\n', t)

# Nur Bilder und Medien behalten, die eine gezeigte Seite auch einbindet oder verlinkt
benutzt = set()
for rel, t in docs.items():
    for m in LINK.finditer(t):
        if not extern(m.group(3)): benutzt.add(ziel(posixpath.dirname(rel), m.group(3)))
imgs = {k: v for k, v in imgs.items() if k in benutzt}
medien = sorted(p for p in benutzt if p.lower().endswith(MEDIEN) and os.path.isfile(os.path.join(ROOT, p)))

# „Erwähnt in“ nur aus Seiten der Spieler-Website
def ziel_doc(p):
    if p in docs: return p
    for c in (p + '/README.md', p + '/' + p.split('/')[-1] + '.md'):
        if c in docs: return c
rueck = {}
for rel, t in docs.items():
    for m in LINK.finditer(t):
        if m.group(1) or extern(m.group(3)): continue
        z = ziel_doc(ziel(posixpath.dirname(rel), m.group(3)))
        if z and z != rel: rueck.setdefault(z, set()).add(rel)
rueck = {k: sorted(v) for k, v in rueck.items()}

namen = ''.join(f", '{a['ordner']}': '{a['nr']} · {a['name']}'" for a in abenteuer)
tpl = template(TITEL, SP.get('untertitel') or ' · '.join(frei_namen))
tpl = tpl.replace("const NAMEN = { 'README.md': 'Übersicht',", "const NAMEN = { 'README.md': 'Übersicht'" + namen + ",", 1)
top = [t for t in ['README.md', 'abenteuer', 'welt'] if any(d == t or d.startswith(t + '/') for d in docs)]
ausgabe = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, '_site', 'spieler')
datei = schreibe_seite(ausgabe, tpl, {'docs': docs, 'imgs': imgs, 'top': top, 'medien': medien, 'rueck': rueck}, list(imgs) + medien, 'spieler')
print('Freigegeben:', ', '.join(f"{a['nr']} {a['name']}" + (' (läuft)' if a['laeuft'] else '') for a in abenteuer) or '–',
      '| ausgelassen:', ', '.join(f"{a['nr']} {a['name']}" for a in gesperrt) or '–')
print(f'Spieler-Website: {len(docs)} Dokumente, {len(imgs)} Bilder, {len(medien)} Medien -> {datei}')

# --- optional: Markdown-Export
if len(sys.argv) > 2:
    import shutil
    out = sys.argv[2]
    shutil.rmtree(out, ignore_errors=True)
    for rel, t in docs.items():
        z = os.path.join(out, rel); os.makedirs(os.path.dirname(z), exist_ok=True)
        open(z, 'w', encoding='utf-8').write(t)
    for rel in list(imgs) + medien:
        z = os.path.join(out, rel); os.makedirs(os.path.dirname(z), exist_ok=True)
        shutil.copy(os.path.join(ROOT, rel), z)
    def reihenfolge(rel):
        teile = rel.split('/'); name = teile[-1]
        bereich = 0 if rel == 'README.md' else 1 if teile[0] == 'abenteuer' else 2
        rang = 0 if name == 'README.md' else 1 if name == 'hauptplot.md' else 2
        return (bereich, teile[:-1], rang, name)
    teile = []
    for rel in sorted(docs, key=reihenfolge):
        t = re.sub(r'^---\n.*?\n---\n', '', docs[rel], flags=re.S)
        basis = posixpath.dirname(rel)
        def um(m):
            bild, txt, href = m.groups()
            if re.match(r'^(https?:|mailto:)', href): return m.group(0)
            if bild: return f'![{txt}]({posixpath.normpath(posixpath.join(basis, href))})'
            return txt
        t = LINK.sub(um, t)
        t = re.sub(r'^(#{1,5}) ', lambda m: '#' + m.group(1) + ' ', t, flags=re.M)  # eine Ebene tiefer
        teile.append(f'<!-- {rel} -->\n' + t.strip())
    open(os.path.join(out, 'spielerseite.md'), 'w', encoding='utf-8').write(
        f'# {TITEL}\n\n' + '\n\n---\n\n'.join(teile) + '\n')
    print('Markdown-Export:', out)
