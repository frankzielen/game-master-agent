# GMA – Einführung

Mit GMA baut dir ein KI-Agent deinen **Rollenspiel-Almanach** auf und pflegt ihn: eine Sammlung deiner Welt und all deiner Abenteuer mit Plot, Szenen, Figuren, Orten, Fraktionen, Gegenständen, Helden und Spielabenden. Du erzählst, der Agent sortiert ein, prüft auf Widersprüche und baut dir auf Wunsch zwei Websites, die Spielleiter-Website und die Spieler-Website. Mit Ordnern und Dateien musst du dich nicht beschäftigen.

## Was du brauchst

Ein Projekt in der Claude- oder ChatGPT-App, das **dauerhaft in einem Ordner** arbeiten darf. Nur dann bleibt alles erhalten. Es gibt zwei Wege:

| | Claude | ChatGPT |
|---|---|---|
| **1 Lokaler Ordner** auf deinem Rechner | 1a | 1b |
| **2 GitHub-Repository** in der Cloud | 2a | 2b |

Beim lokalen Ordner liegt alles bei dir auf dem Rechner. Beim GitHub-Repository liegt alles in deinem GitHub-Konto und du kannst von überall weiterarbeiten. Claude Code und Codex funktionieren ebenso. Normale Chats ohne Ordnerzugriff sind nicht geeignet. Python 3 für die Websites prüft der Agent selbst und hilft bei Bedarf bei der Installation.

## Einrichten

1. **Lokaler Ordner:** GMA als ZIP herunterladen und entpacken. In der App ein Projekt anlegen und den entpackten Ordner damit verbinden.
   **GitHub-Repository:** Auf GitHub mit „Use this template“ eine eigene Kopie anlegen. In der App ein Projekt anlegen und es mit dieser Kopie verbinden.
2. Im Projekt einen neuen Chat beginnen und schreiben: **„Folge START.md.“**
3. Der Agent richtet alles ein und fragt dich Schritt für Schritt nach Titel, Welt, Mitspielern, Regelsystem, Abenteuern und Helden. Was du noch nicht weißt, beantwortest du mit „später“.
4. Zum Schluss baut der Agent die beiden Websites und klärt mit dir, wie du und deine Spieler sie bekommt: über Claude bzw. ChatGPT veröffentlichen, auf eigenem Webspace (zum Beispiel GitHub Pages) oder offline als Datei.

## So arbeitest du mit dem Agenten

- **Ideen:** einfach erzählen oder einsprechen, gern in Bruchstücken. Bei Widersprüchen fragt der Agent nach und schlägt Lösungen vor.
- **Nach einem Spielabend:** erzählen, was passiert ist. Der Agent schreibt das Protokoll und bringt Helden und Welt auf den neuesten Stand.
- **Beispiel ansehen:** Sag „Zeig mir das Beispiel“, dann baut der Agent die beiden Websites des mitgelieferten Beispiel-Almanachs und du siehst, wie alles aussieht.
- **Material:** Bilder, Karten, Handouts, Statblöcke, Musik einfach schicken und sagen, wozu sie gehören.
- **Websites:** Nach Änderungen bietet der Agent an, die Websites neu zu bauen, nur für dich oder auch online. Danach kannst du beide direkt öffnen.

## Die Grundideen

- **Eine Welt, viele Abenteuer:** Figuren, Orte und Gegenstände gibt es nur einmal, jedes Abenteuer hat nur seinen Plot und seine Sitzungen. Die Spielleitung darf wechseln.
- **Entwicklung über die Abenteuer:** Jeder Welt-Eintrag zeigt das Zeitlose, den aktuellen Stand und was im jeweiligen Abenteuer geschah.
- **Geheimnisse:** Was nur die Spielleitung wissen darf, ist in den Daten gekennzeichnet und fehlt in der Spieler-Website automatisch.
- **Jedes Regelsystem:** Mitgeliefert sind „Ohne Regelsystem“ und „D&D 5e“, für andere Systeme legt der Agent mit dir ein Profil an.

Die Regeln für den Agenten stehen in `almanach/AGENTS.md`. Soll etwas anders laufen, sag es dem Agenten, er passt die Regeln an.
