"""„Erwähnt in“ ordnen: ohne Übersichtsseiten (README.md), ohne Seiten, auf die der Eintrag selbst schon verlinkt,
und nach Art gruppiert. Wird von beiden Website-Generatoren benutzt."""
import re

GRUPPEN = [
    ('Sitzungen', re.compile(r'^abenteuer/[^/]+/sitzungen/')),
    ('Kapitel, Szenen und Quests', re.compile(r'^abenteuer/[^/]+/plot/')),
    ('Figuren', re.compile(r'^welt/(nscs|spielercharaktere)/')),
    ('Orte', re.compile(r'^welt/orte/')),
    ('Fraktionen', re.compile(r'^welt/fraktionen/')),
    ('Gegenstände', re.compile(r'^welt/gegenstaende/')),
]


def ordnen(rueck):
    """rueck: {ziel: Menge der Seiten, die auf ziel verlinken} -> {ziel: [[Gruppe, [Seiten]], ...]}"""
    vor = {}
    for z, quellen in rueck.items():
        for q in quellen: vor.setdefault(q, set()).add(z)
    out = {}
    for z, quellen in rueck.items():
        eigene = vor.get(z, set())
        rest = [q for q in sorted(quellen) if not q.endswith('README.md') and q not in eigene]
        gruppen = []
        for name, muster in GRUPPEN:
            g = [q for q in rest if muster.match(q)]
            if g: gruppen.append([name, g])
        sonst = [q for q in rest if not any(m.match(q) for _, m in GRUPPEN)]
        if sonst: gruppen.append(['Sonstiges', sonst])
        if gruppen: out[z] = gruppen
    return out
