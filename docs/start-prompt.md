# Start-Prompt

Diesen Text komplett kopieren und als erste Nachricht an den KI-Assistenten schicken. Er funktioniert mit **ChatGPT** (am besten im Codex-Modus) und mit **Claude** (in einem Claude-Projekt mit Projektordner oder mit Claude Code). Das ZIP `rollenspiel-starterkit.zip` an dieselbe Nachricht anhängen. Falls der Chat keine ZIP-Anhänge annimmt, das ZIP einfach im Download-Ordner lassen.

---

```
Du richtest für mich eine strukturierte Ablage für meine Pen-&-Paper-Kampagne ein. Alles Nötige steckt im ZIP „rollenspiel-starterkit.zip“: Ordnerstruktur, Vorlagen, Regeln und Werkzeuge. Der Prompt ist für verschiedene KI-Assistenten geschrieben (ChatGPT/Codex, Claude); wende ihn sinngemäß auf deine Werkzeuge an. Bitte erledige die Einrichtung vollständig selbst, ich möchte keine Ordner oder Dateien von Hand anlegen.

Schritt 1 – ZIP finden und entpacken
- Nimm die an diese Nachricht angehängte Datei „rollenspiel-starterkit.zip“. Ist nichts angehängt, suche sie im aktuellen Arbeitsordner und in meinem Download-Ordner. Findest du sie nicht, frag mich nach dem Pfad.
- Entpacke es in einen temporären Unterordner.

Schritt 2 – Struktur anlegen
- Arbeitsordner ist dein dauerhafter Ordner: der Projektordner (z. B. in einem Claude-Projekt in der Cloud) oder der Ordner auf meinem Rechner, in dem du arbeiten darfst.
- Lege im Arbeitsordner selbst einen neuen Ordner „rollenspiel-kampagne“ an. Das ist ab jetzt der Kampagnenordner. Ist der Arbeitsordner leer, kannst du stattdessen direkt ihn verwenden.
- Kopiere den GESAMTEN Inhalt des Ordners „kampagne/“ aus dem ZIP (inklusive AGENTS.md, CLAUDE.md, README.md, offene-punkte.md, _vorlagen/, abenteuer/, welt/, werkzeuge/) in den Kampagnenordner, sodass AGENTS.md und README.md dort auf oberster Ebene liegen. Vorhandene Dateien nicht überschreiben, sondern mich fragen.
- Lösche danach den temporären Entpack-Ordner.
- Sag mir den vollständigen Pfad des Kampagnenordners und dass ich künftig genau diesen Ordner öffnen soll (in Codex bzw. Claude), damit die Regeln automatisch gelesen werden: Codex liest AGENTS.md, Claude Code liest CLAUDE.md, die auf AGENTS.md verweist. In einem Claude-Projekt erinnere mich daran, in die Projektanweisungen zu schreiben, dass du vor jeder Aufgabe AGENTS.md liest, und nenne mir dafür den genauen Pfad.

Schritt 3 – Regeln übernehmen
- Lies AGENTS.md vollständig (CLAUDE.md verweist nur darauf). Das ist ab jetzt deine verbindliche Arbeitsanweisung für diesen Ordner, in dieser und allen künftigen Sitzungen.

Schritt 4 – Kampagne einrichten
Stelle mir diese Fragen in EINER Nachricht und warte auf die Antwort:
  1. Wie heißt die Kampagne (Titel für die Startseite)?
  2. Wie heißt die Welt bzw. die Startregion?
  3. Wer spielt mit (Namen, gern mit Spitznamen)?
  4. Gibt es schon Abenteuer? Wenn ja: Titel, Spielleitung, Status (gespielt / in Arbeit / geplant), in Spielreihenfolge.
  5. Welches Regelsystem spielt ihr? Mitgeliefert sind „Ohne Regelsystem“ und „D&D 5e“ (Ordner systeme/). Für jedes andere System legen wir zusammen ein Profil an.
  6. Gibt es schon Spielercharaktere? Wenn ja: Name, Spieler und was das Regelsystem dazu braucht (bei D&D z. B. Volk, Klasse, Stufe).
Wenn ich etwas nicht weiß, lass den Platzhalter stehen.

Schritt 5 – Befüllen
- Trage die Antworten in README.md ein (Titel, Welt, Spieler).
- Trage das gewählte Regelsystem in einstellungen.json unter "system" ein (Ordnername aus systeme/). Für ein System, das noch nicht dabei ist, lege mit mir systeme/<name>/profil.md und statblock.md an, wie in systeme/README.md beschrieben (nur Feldnamen und Begriffe, keine Regeltexte).
- Lege für jedes genannte Abenteuer den Ordner abenteuer/NN-titel/ an, genau wie in AGENTS.md beschrieben: README.md (aus _vorlagen/abenteuer-readme.md), ideen-eingang.md (aus _vorlagen/ideen-eingang.md), plot/hauptplot.md (aus _vorlagen/hauptplot.md, Spielleitung eintragen), plot/quests/ und sitzungen/. Trage alle Abenteuer in abenteuer/README.md ein.
- Lege für jeden genannten Spielercharakter welt/spielercharaktere/<name>/<name>.md aus der Vorlage an und trage ihn in welt/spielercharaktere/README.md ein.

Schritt 6 – Prüfen und melden
- Prüfe, ob Python 3 verfügbar ist („python3 --version“, unter Windows „python --version“). Falls nicht, erkläre mir in einfachen Schritten, wie ich es installiere (python.org oder unter Windows der Microsoft Store), und mach danach weiter.
- Führe „python3 werkzeuge/links-pruefen.py“ aus (unter Windows ggf. „python“) und repariere tote Links.
- Zeige mir zum Schluss die angelegte Ordnerstruktur als Baum und erkläre in drei Sätzen, wie ich ab jetzt mit dir arbeite (Ideen einsprechen, Widersprüche klären, Spielberichte einpflegen).

Falls du KEINEN Zugriff auf mein lokales Dateisystem hast (z. B. normaler Chat im Browser ohne Ordnerzugriff): Führe alle Schritte in deiner eigenen Arbeitsumgebung aus, packe das Ergebnis als „kampagne.zip“ und gib mir den Download-Link. Sag mir dann, dass ich das ZIP einmal in einen Ordner meiner Wahl entpacken muss, und liefere mir künftig neue oder geänderte Dateien jeweils mit ihrem Pfad zum Herunterladen.
```
