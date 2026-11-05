# Start-Prompt

Diesen Text komplett kopieren und als erste Nachricht an den KI-Assistenten schicken. Er funktioniert mit **ChatGPT** (am besten im Codex-Modus) und mit **Claude** (in einem Claude-Projekt mit Projektordner oder mit Claude Code). Das GMA-ZIP an dieselbe Nachricht anhängen (aus den Releases oder auf GitHub unter „Code“ → „Download ZIP“, Name z. B. `game-master-agent-main.zip`). Falls der Chat keine ZIP-Anhänge annimmt, das ZIP einfach im Download-Ordner lassen.

---

```
Du richtest für mich eine strukturierte Ablage für meine Pen-&-Paper-Kampagne ein. Alles Nötige steckt im angehängten GMA-ZIP (Name beginnt mit „game-master-agent“): Ordnerstruktur, Vorlagen, Regeln und Werkzeuge. Der Prompt ist für verschiedene KI-Assistenten geschrieben (ChatGPT/Codex, Claude); wende ihn sinngemäß auf deine Werkzeuge an. Bitte erledige die Einrichtung vollständig selbst, ich möchte keine Ordner oder Dateien von Hand anlegen.

Schritt 1 – ZIP finden und entpacken
- Nimm das an diese Nachricht angehängte ZIP. Ist nichts angehängt, suche im aktuellen Arbeitsordner und in meinem Download-Ordner nach einer Datei „game-master-agent*.zip“. Findest du sie nicht, frag mich nach dem Pfad.
- Entpacke es in einen temporären Unterordner.

Schritt 2 – Struktur anlegen
- Arbeitsordner ist dein dauerhafter Ordner: der Projektordner (z. B. in einem Claude-Projekt in der Cloud) oder der Ordner auf meinem Rechner, in dem du arbeiten darfst.
- Lege im Arbeitsordner selbst einen neuen Ordner „rollenspiel-kampagne“ an. Das ist ab jetzt der Kampagnenordner. Ist der Arbeitsordner leer, kannst du stattdessen direkt ihn verwenden.
- Kopiere den GESAMTEN Inhalt des Ordners „kampagne/“ aus dem ZIP (er liegt dort ggf. unter einem Oberordner wie „game-master-agent-main/“; inklusive AGENTS.md, CLAUDE.md, README.md, einstellungen.json, offene-punkte.md, _vorlagen/, abenteuer/, welt/, systeme/, werkzeuge/) in den Kampagnenordner, sodass AGENTS.md und README.md dort auf oberster Ebene liegen. Vorhandene Dateien nicht überschreiben, sondern mich fragen.
- Lösche danach den temporären Entpack-Ordner.
- Sag mir den vollständigen Pfad des Kampagnenordners und dass ich künftig genau diesen Ordner öffnen soll (in Codex bzw. Claude), damit die Regeln automatisch gelesen werden: Codex liest AGENTS.md, Claude Code liest CLAUDE.md, die auf AGENTS.md verweist. In einem Claude-Projekt erinnere mich daran, in die Projektanweisungen zu schreiben, dass du vor jeder Aufgabe AGENTS.md liest, und nenne mir dafür den genauen Pfad.

Schritt 3 – Regeln übernehmen
- Lies AGENTS.md vollständig (CLAUDE.md verweist nur darauf). Das ist ab jetzt deine verbindliche Arbeitsanweisung für diesen Ordner, in dieser und allen künftigen Sitzungen.

Schritt 4 – Kampagne einrichten
Führe mich im Dialog durch die Einrichtung, wie in AGENTS.md unter „Kampagne einrichten (beim ersten Start)“ beschrieben: immer nur eine Frage pro Nachricht, und ich darf jederzeit „weiß ich noch nicht“ oder „später“ sagen. Trage jede Antwort sofort ein.

Schritt 5 – Prüfen und melden
- Prüfe, ob Python 3 verfügbar ist („python3 --version“, unter Windows „python --version“). Falls nicht, erkläre mir in einfachen Schritten, wie ich es installiere (python.org oder unter Windows der Microsoft Store), und mach danach weiter.
- Führe „python3 werkzeuge/links-pruefen.py“ aus (unter Windows ggf. „python“) und repariere tote Links.
- Fasse zum Schluss in wenigen Sätzen zusammen, was angelegt ist und was noch offen ist, und erkläre, wie ich ab jetzt mit dir arbeite (Ideen einsprechen, Widersprüche klären, Spielberichte einpflegen).

Falls du KEINEN Zugriff auf mein lokales Dateisystem hast (z. B. normaler Chat im Browser ohne Ordnerzugriff): Führe alle Schritte in deiner eigenen Arbeitsumgebung aus, packe das Ergebnis als „kampagne.zip“ und gib mir den Download-Link. Sag mir dann, dass ich das ZIP einmal in einen Ordner meiner Wahl entpacken muss, und liefere mir künftig neue oder geänderte Dateien jeweils mit ihrem Pfad zum Herunterladen.
```
