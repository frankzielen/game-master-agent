# GMA einrichten – Anleitung für den KI-Agenten

Diese Datei richtet sich an dich, den KI-Agenten. Die Nutzerin oder der Nutzer hat dir das GMA-Paket gegeben (als ZIP, als Ordner oder als GitHub-Repository) und möchte loslegen. Erledige alles selbst. Die Person soll keine Ordner oder Dateien von Hand anlegen und keine Dateipfade kennen müssen. Antworte in ihrer Sprache, kurz und freundlich.

## Schritt 1 – Paket finden

Das GMA-Paket ist das, was dir mit dieser Datei gegeben wurde: ein angehängtes ZIP (der Name ist egal), ein entpackter Ordner oder ein GitHub-Repository. Ist es ein ZIP, entpacke es in einen temporären Ordner. Im Paket liegt der Ordner `almanach/`, eventuell unter einem Oberordner. Das ist der leere Almanach.

## Schritt 2 – Almanach-Ordner festlegen

- **GitHub-Repository, geöffneter Ordner oder ein Ordner auf dem Rechner der Person, auf den du schreiben darfst:** `almanach/` bleibt, wo er ist, und ist der Almanach-Ordner. Arbeite direkt darin und kopiere nichts, auch nicht in eine Projektablage.
- **Sonst** (nur ein angehängtes ZIP): Kopiere den gesamten Inhalt von `almanach/` in deinen dauerhaften Arbeitsordner. Ist er leer, nimm ihn direkt, sonst lege darin `rollenspiel-almanach/` an. Vorhandene Dateien nie überschreiben, sondern fragen. Lösche danach den temporären Ordner.

Erzähl der Person nichts über Dateinamen, Pfade oder Zwischenschritte. Ein Satz genügt, etwa „GMA ist eingerichtet.“

## Schritt 2b – Regeln dauerhaft machen

Die Regeln in `AGENTS.md` müssen in jeder künftigen Unterhaltung gelten.
- Manche Umgebungen lesen `AGENTS.md` oder `CLAUDE.md` im geöffneten Ordner automatisch (z. B. Claude Code, Codex). Dann ist nichts zu tun.
- Wenn deine Umgebung dauerhafte Anweisungen hat, die zu Beginn jeder Unterhaltung gelten (z. B. Projektanweisungen, benutzerdefinierte Anweisungen), trag dort ein: „Lies vor jeder Aufgabe AGENTS.md im Almanach-Ordner (Pfad: …) und halte dich daran.“ Wenn du sie nicht selbst ändern kannst, gib der Person genau diesen Satz zum Kopieren und sag in einem Satz, wo sie ihn einträgt.

## Schritt 3 – Regeln lesen

Lies `AGENTS.md` im Almanach-Ordner vollständig. Sie ist ab jetzt deine verbindliche Arbeitsanweisung, in dieser und allen künftigen Sitzungen.

## Schritt 4 – Almanach einrichten

Deine erste Frage an die Person ist immer, ob sie zuerst das Beispiel sehen oder gleich einrichten möchte (Schaltflächen „Erst das Beispiel ansehen“ und „Gleich einrichten“). Erst danach folgt die Frage nach dem Namen des Almanachs.

Führe die Person dann durch die Einrichtung, genau wie in `AGENTS.md` unter „Almanach einrichten (beim ersten Start)“ beschrieben: eine Frage pro Nachricht, und „weiß ich noch nicht“ oder „später“ ist jederzeit erlaubt.

## Kein dauerhafter Ordner?

Hast du keinen dauerhaften Ordner (normaler Chat ohne Dateizugriff), sag das gleich zu Beginn ehrlich: GMA braucht einen Agenten, der dauerhaft in einem Ordner arbeiten darf, zum Beispiel ein Claude-Projekt, Claude Code oder ein ChatGPT-Projekt mit Ordner oder GitHub-Repository. Richte dann nichts halb ein.
