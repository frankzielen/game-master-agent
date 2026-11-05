# GMA – Einführung

Mit GMA baut dir ein KI-Agent eine Ablage für deine Rollenspiel-Welt und deine Abenteuer auf und pflegt sie: Plot, Szenen, Figuren, Orte, Fraktionen, Gegenstände, Helden und Spielabende. Du erzählst, der Agent sortiert ein, prüft auf Widersprüche und baut dir auf Wunsch zwei Websites, eine für die Spielleitung und eine Heldenversion für die Spieler. Mit Ordnern und Dateien musst du dich nicht beschäftigen.

## Was du brauchst

Einen KI-Agenten, der **dauerhaft in einem Ordner** arbeiten darf. Nur dann bleibt alles erhalten.

| | Claude-Projekt | Claude Code | ChatGPT mit Codex |
|---|---|---|---|
| Wo liegt alles? | im Projektordner bei Claude (Cloud) | lokaler Ordner oder GitHub-Repository in der Cloud | lokaler Ordner oder GitHub-Repository in der Cloud |
| Womit arbeitest du? | Claude-App oder claude.ai, auch am Handy | Claude-App (Bereich „Code“), VS Code oder Terminal | ChatGPT-App im Codex-Modus, VS Code oder Terminal |

Normale Chats ohne Ordnerzugriff sind nicht geeignet. Python 3 für die Websites prüft der Agent selbst und hilft bei Bedarf bei der Installation.

## Einrichten

1. Lade GMA als ZIP herunter (oder lege mit „Use this template“ eine eigene Kopie auf GitHub an).
2. Häng das ZIP an die erste Nachricht an deinen Agenten und schreib: **„Richte GMA ein und folge START.md im angehängten ZIP.“** Mit einer GitHub-Kopie oder einem geöffneten Ordner reicht: „Richte GMA ein und folge START.md.“
3. Der Agent richtet alles ein und fragt dich Schritt für Schritt nach Titel, Welt, Mitspielern, Regelsystem, Abenteuern und Helden. Was du noch nicht weißt, beantwortest du mit „später“.

Mac-Hinweis: Safari entpackt ZIPs nach dem Herunterladen automatisch. Für ein Claude-Projekt den Ordner per Rechtsklick → „… komprimieren“ wieder zum ZIP machen.

## So arbeitest du mit dem Agenten

- **Ideen:** einfach erzählen oder einsprechen, gern in Bruchstücken. Bei Widersprüchen fragt der Agent nach und schlägt Lösungen vor.
- **Nach einem Spielabend:** erzählen, was passiert ist. Der Agent schreibt das Protokoll und bringt Helden und Welt auf den neuesten Stand.
- **Material:** Bilder, Karten, Handouts, Statblöcke, Musik einfach schicken und sagen, wozu sie gehören.
- **Websites:** Nach Änderungen bietet der Agent „Websites neu bauen“ an und danach die beiden Seiten zum Öffnen. Sie laufen offline und lassen sich weitergeben.

## Die Grundideen

- **Eine Welt, viele Abenteuer:** Figuren, Orte und Gegenstände gibt es nur einmal, jedes Abenteuer hat nur seinen Plot und seine Sitzungen. Die Spielleitung darf wechseln.
- **Entwicklung über die Abenteuer:** Jeder Welt-Eintrag zeigt das Zeitlose, den aktuellen Stand und was im jeweiligen Abenteuer geschah.
- **Geheimnisse:** Was nur die Spielleitung wissen darf, ist in den Daten gekennzeichnet und fehlt in der Heldenversion automatisch.
- **Jedes Regelsystem:** Mitgeliefert sind „Ohne Regelsystem“ und „D&D 5e“, für andere Systeme legt der Agent mit dir ein Profil an.

Die Regeln für den Agenten stehen in `kampagne/AGENTS.md`. Soll etwas anders laufen, sag es dem Agenten, er passt die Regeln an.
