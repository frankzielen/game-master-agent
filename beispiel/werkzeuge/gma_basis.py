"""Gemeinsame Hilfen für die Website-Generatoren (SL-Website und Spielerseite)."""
import os, sys, json, re, shutil, base64, mimetypes

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.dirname(os.path.abspath(__file__))
IMG = ('.jpg', '.jpeg', '.png', '.webp', '.gif', '.svg')

# --eine-datei: Bilder in die HTML-Datei einbetten (zum Anhängen im Chat, wo Dateien daneben fehlen)
EINE_DATEI = '--eine-datei' in sys.argv
if EINE_DATEI:
    sys.argv.remove('--eine-datei')


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


def schreibe_seite(ausgabe, tpl, data, dateien, name):
    """Schreibt <name>.html nach <ausgabe>/ und kopiert Bilder und Medien (Pfade relativ zur Kampagne) daneben.
    Dazu eine kleine index.html, die auf <name>.html weiterleitet (für Hoster wie GitHub Pages).
    Mit --eine-datei stecken die Bilder in der HTML-Datei selbst (zum Anhängen im Chat)."""
    os.makedirs(ausgabe, exist_ok=True)
    if EINE_DATEI:
        for rel in list(data.get('imgs', {})):
            typ = mimetypes.guess_type(rel)[0] or 'application/octet-stream'
            roh = open(os.path.join(ROOT, rel), 'rb').read()
            data['imgs'][rel] = f'data:{typ};base64,' + base64.b64encode(roh).decode()
        dateien = [d for d in dateien if d not in data.get('imgs', {})]
    blob = json.dumps(data, ensure_ascii=False).replace('</', '<\\/')
    datei = name + '.html'
    open(os.path.join(ausgabe, datei), 'w', encoding='utf-8').write(tpl.replace('/*__DATA__*/null', blob))
    open(os.path.join(ausgabe, 'index.html'), 'w', encoding='utf-8').write(
        f'<!DOCTYPE html>\n<meta charset="utf-8">\n<meta http-equiv="refresh" content="0; url={datei}">\n'
        f'<title>Weiterleitung</title>\n<a href="{datei}">{datei} öffnen</a>\n')
    for rel in dateien:
        ziel = os.path.join(ausgabe, rel)
        os.makedirs(os.path.dirname(ziel), exist_ok=True)
        shutil.copy2(os.path.join(ROOT, rel), ziel)
    return os.path.join(ausgabe, datei)


def template(titel, untertitel):
    tpl = open(os.path.join(HERE, 'kampagne-html.template.html'), encoding='utf-8').read()
    tpl = re.sub(r'<title>[^<]*</title>', f'<title>{esc(titel)}</title>', tpl, count=1)
    tpl = re.sub(r'<div class="brand"><h1>[^<]*</h1><p>[^<]*</p>',
                 lambda m: f'<div class="brand"><h1>{esc(titel)}</h1><p>{esc(untertitel)}</p>', tpl, count=1)
    # Markdown-Leser (marked, MIT-Lizenz) direkt einbetten, damit die Seite auch ohne Internet funktioniert
    js = open(os.path.join(HERE, 'marked.min.js'), encoding='utf-8').read().replace('</script', '<\\/script')
    tpl = re.sub(r'<script src="[^"]*marked\.min\.js"></script>', lambda m: '<script>' + js + '</script>', tpl, count=1)
    return tpl
