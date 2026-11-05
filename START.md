# GMA einrichten – Anleitung für den KI-Agenten

Diese Datei richtet sich an dich, den KI-Agenten. Die Nutzerin oder der Nutzer hat dir das GMA-Paket gegeben (als ZIP, als Ordner oder als GitHub-Repository) und möchte loslegen. Erledige alles selbst. Die Person soll keine Ordner oder Dateien von Hand anlegen und keine Dateipfade kennen müssen. Antworte in ihrer Sprache, kurz und freundlich.

## Schritt 1 – Paket finden

- Liegt ein ZIP vor (angehängt oder im Arbeits- oder Download-Ordner, Name beginnt meist mit „game-master-agent“), entpacke es in einen temporären Ordner.
- Darin liegt der Ordner `kampagne/`, eventuell unter einem Oberordner wie `game-master-agent-main/`. Das ist die leere Kampagne.

## Schritt 2 – Kampagnenordner festlegen

- **GitHub-Repository oder geöffneter GMA-Ordner:** Der Ordner `kampagne/` bleibt, wo er ist. Er ist der Kampagnenordner, kopiere nichts.
- **Claude-Projekt, ChatGPT/Codex oder anderer dauerhafter Ordner:** Kopiere den gesamten Inhalt von `kampagne/` (mit `AGENTS.md`, `CLAUDE.md`, `README.md`, `einstellungen.json`, `offene-punkte.md`, `_vorlagen/`, `abenteuer/`, `welt/`, `systeme/`, `werkzeuge/`) in deinen dauerhaften Arbeitsordner. Ist der Ordner leer, nimm ihn direkt. Sonst lege darin einen Ordner `rollenspiel-kampagne` an. Vorhandene Dateien nie überschreiben, sondern fragen. Lösche danach den temporären Ordner.
- Damit die Regeln auch in späteren Sitzungen gelten: Claude Code liest `CLAUDE.md`, Codex liest `AGENTS.md` automatisch, wenn der Kampagnenordner geöffnet wird. In einem Claude-Projekt schlage der Person einen fertigen Satz für die Projektanweisungen vor („Lies vor jeder Aufgabe AGENTS.md im Ordner …“) und sag ihr genau, wo sie ihn einträgt.

## Schritt 3 – Regeln lesen

Lies `AGENTS.md` im Kampagnenordner vollständig. Sie ist ab jetzt deine verbindliche Arbeitsanweisung, in dieser und allen künftigen Sitzungen.

## Schritt 4 – Kampagne einrichten

Führe die Person durch die Einrichtung, genau wie in `AGENTS.md` unter „Kampagne einrichten (beim ersten Start)“ beschrieben: eine Frage pro Nachricht, und „weiß ich noch nicht“ oder „später“ ist jederzeit erlaubt.

## Kein dauerhafter Ordner?

Hast du keinen dauerhaften Ordner (normaler Chat ohne Dateizugriff), sag das gleich zu Beginn ehrlich: GMA braucht einen Agenten, der dauerhaft in einem Ordner arbeiten darf, zum Beispiel ein Claude-Projekt, Claude Code oder ChatGPT mit Codex. Richte dann nichts halb ein.
