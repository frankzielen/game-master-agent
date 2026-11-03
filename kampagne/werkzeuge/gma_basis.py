"""Gemeinsame Hilfen für die Website-Generatoren (SL-Website und Spielerseite)."""
import os, json, re, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.dirname(os.path.abspath(__file__))
IMG = ('.jpg', '.jpeg', '.png', '.webp', '.gif', '.svg')


def einstellungen():
    p = os.path.join(ROOT, 'einstellungen.json')
    e = json.load(open(p, encoding='utf-8')) if os.path.isfile(p) else {}
    e.setdefault('spielerseite', {})
    if not e.get('titel'):
        try:
            m = re.search(r'^#\s+(.+)$', open(os.path.join(ROOT, 'README.md'), encoding='utf-8').read(), re.M)
            e['titel'] = m.group(1).strip() if m else 'Kampagne'
        except OSError:
            e['titel'] = 'Kampagne'
    return e


def esc(t):
    return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def schreibe_seite(ausgabe, tpl, data, dateien):
    """Schreibt index.html nach <ausgabe>/ und kopiert Bilder und Medien (Pfade relativ zur Kampagne) daneben."""
    os.makedirs(ausgabe, exist_ok=True)
    blob = json.dumps(data, ensure_ascii=False).replace('</', '<\\/')
    open(os.path.join(ausgabe, 'index.html'), 'w', encoding='utf-8').write(tpl.replace('/*__DATA__*/null', blob))
    for rel in dateien:
        ziel = os.path.join(ausgabe, rel)
        os.makedirs(os.path.dirname(ziel), exist_ok=True)
        shutil.copy2(os.path.join(ROOT, rel), ziel)


def template(titel, untertitel):
    tpl = open(os.path.join(HERE, 'kampagne-html.template.html'), encoding='utf-8').read()
    tpl = re.sub(r'<title>[^<]*</title>', f'<title>{esc(titel)}</title>', tpl, count=1)
    tpl = re.sub(r'<div class="brand"><h1>[^<]*</h1><p>[^<]*</p>',
                 lambda m: f'<div class="brand"><h1>{esc(titel)}</h1><p>{esc(untertitel)}</p>', tpl, count=1)
    # Markdown-Leser (marked, MIT-Lizenz) direkt einbetten, damit die Seite auch ohne Internet funktioniert
    js = open(os.path.join(HERE, 'marked.min.js'), encoding='utf-8').read().replace('</script', '<\\/script')
    tpl = re.sub(r'<script src="[^"]*marked\.min\.js"></script>', lambda m: '<script>' + js + '</script>', tpl, count=1)
    return tpl
