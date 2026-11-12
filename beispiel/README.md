# Beispiel: Die Salzmarsch

![Ilka, Bren und Hedda über der Salzmarsch](bilder/cover.jpg)
_Quelle: KI-generiert mit ChatGPT_

Einstiegspunkt für alle Abenteuer unserer Gruppe. Alle Abenteuer spielen in derselben Welt (die Salzmarsch), die Spielleitung kann wechseln.
Die **Welt** (NSCs, Orte, Fraktionen, Gegenstände, Spielercharaktere) gibt es nur einmal und wird von allen Abenteuern genutzt. Jedes **Abenteuer** hat nur seinen eigenen Plot und seine Sitzungen.

**Spieler:** Alex, Sam, Robin
**Regelsystem:** D&D 5e ([Systemprofil](systeme/dnd-5e/profil.md)). NSCs und Spielercharaktere haben je einen Statblock.

> Dieser Beispiel-Almanach ist frei erfunden. Er zeigt, was ein Almanach kann: zwei gespielte Abenteuer mit wechselnder Spielleitung, Sitzungen mit Diktat als Quelle, eine nacherzählte Geschichte, Quests, eine Fraktion, Figuren und Orte, die sich über mehrere Abenteuer entwickeln, ein geplantes drittes Abenteuer, Geheimnisse und „(nur SL)“-Zeilen. Baue beide Websites und vergleiche: Die Spieler-Website zeigt nur, was die Helden wissen.

```
welt/                        gemeinsam für alle Abenteuer
  nscs/                      ein Ordner pro NSC: name.md, statblock.md, bilder/
  orte/                      Region → Stadt → Gebäude
  fraktionen/
  gegenstaende/
  spielercharaktere/         ein Ordner pro SC: name.md, statblock.md, bilder/
abenteuer/                   chronologisch nummeriert, jeweils plot/ (mit quests/) und sitzungen/
systeme/                     Systemprofile (Regelsystem): Charakterfelder, Begriffe, Statblock-Vorlage
_vorlagen/                   Kopiervorlagen für alle Dateitypen (regelneutral)
werkzeuge/                   Links prüfen, Spielleiter-Website und Spieler-Website erzeugen
einstellungen.json           gewähltes Regelsystem, Titel, Startseite der Spieler-Website
offene-punkte.md             Widersprüche, offene Fragen, getroffene Entscheidungen
AGENTS.md                    Arbeitsanweisung für den KI-Assistenten
CLAUDE.md                    Verweis auf AGENTS.md (wird von Claude automatisch gelesen)
```

| Bereich | Einstieg |
|---|---|
| Alle Abenteuer mit Spielleitung | [abenteuer/README.md](abenteuer/README.md) |
| NSCs | [welt/nscs/](welt/nscs/README.md) |
| Orte | [welt/orte/](welt/orte/README.md) |
| Fraktionen | [welt/fraktionen/](welt/fraktionen/README.md) |
| Gegenstände | [welt/gegenstaende/](welt/gegenstaende/README.md) |
| Spielercharaktere | [welt/spielercharaktere/](welt/spielercharaktere/README.md) |
| Offene Punkte | [offene-punkte.md](offene-punkte.md) |

## So wird gearbeitet

Die Spielleitung brainstormt, der KI-Assistent sortiert die Ideen in diese Struktur ein, prüft sie auf Widersprüche und pflegt die Querverweise. Die genauen Regeln stehen in [AGENTS.md](AGENTS.md).

## Tipp

Den ganzen Ordner kann man in VS Code (Vorschau: Strg/Cmd+Shift+V) oder als Obsidian-Vault öffnen. Links und Bilder funktionieren dort ohne Umbau.
