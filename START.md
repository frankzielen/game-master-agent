# GMA einrichten – Anleitung für den KI-Agenten

Diese Datei richtet sich an dich, den KI-Agenten. Die Nutzerin oder der Nutzer hat dir das GMA-Paket gegeben (als ZIP, als Ordner oder als GitHub-Repository) und möchte loslegen. Erledige alles selbst. Die Person soll keine Ordner oder Dateien von Hand anlegen und keine Dateipfade kennen müssen. Antworte in ihrer Sprache, kurz und freundlich.

## Schritt 1 – Paket finden

Das GMA-Paket ist das, was dir mit dieser Datei gegeben wurde: ein angehängtes ZIP (der Name ist egal), ein entpackter Ordner oder ein GitHub-Repository. Ist es ein ZIP, entpacke es in einen temporären Ordner. Im Paket liegt der Ordner `kampagne/`, eventuell unter einem Oberordner. Das ist die leere Kampagne.

## Schritt 2 – Kampagnenordner festlegen

- **GitHub-Repository oder geöffneter Ordner:** `kampagne/` bleibt, wo er ist, und ist der Kampagnenordner. Kopiere nichts.
- **Sonst** (z. B. Claude-Projekt oder ChatGPT): Kopiere den gesamten Inhalt von `kampagne/` in deinen dauerhaften Arbeitsordner. Ist er leer, nimm ihn direkt, sonst lege darin `rollenspiel-kampagne/` an. Vorhandene Dateien nie überschreiben, sondern fragen. Lösche danach den temporären Ordner.

Erzähl der Person nichts über Dateinamen, Pfade oder Zwischenschritte. Ein Satz genügt, etwa „GMA ist eingerichtet.“

## Schritt 2b – Regeln dauerhaft machen

Die Regeln in `AGENTS.md` müssen in jeder künftigen Unterhaltung gelten.
- Liest deine Umgebung `AGENTS.md` oder `CLAUDE.md` im geöffneten Ordner von selbst (z. B. Claude Code, Codex), ist nichts zu tun.
- Hat deine Umgebung dauerhafte Anweisungen, die zu Beginn jeder Unterhaltung gelten (z. B. Projektanweisungen, benutzerdefinierte Anweisungen), trag dort ein: „Lies vor jeder Aufgabe AGENTS.md im Kampagnenordner (Pfad: …) und halte dich daran.“ Kannst du sie nicht selbst ändern, gib der Person genau diesen Satz zum Kopieren und sag in einem Satz, wo sie ihn einträgt.

## Schritt 3 – Regeln lesen

Lies `AGENTS.md` im Kampagnenordner vollständig. Sie ist ab jetzt deine verbindliche Arbeitsanweisung, in dieser und allen künftigen Sitzungen.

## Schritt 4 – Kampagne einrichten

Führe die Person durch die Einrichtung, genau wie in `AGENTS.md` unter „Kampagne einrichten (beim ersten Start)“ beschrieben: eine Frage pro Nachricht, und „weiß ich noch nicht“ oder „später“ ist jederzeit erlaubt.

## Kein dauerhafter Ordner?

Hast du keinen dauerhaften Ordner (normaler Chat ohne Dateizugriff), sag das gleich zu Beginn ehrlich: GMA braucht einen Agenten, der dauerhaft in einem Ordner arbeiten darf, zum Beispiel ein Claude-Projekt, Claude Code oder ChatGPT mit Codex. Richte dann nichts halb ein.
