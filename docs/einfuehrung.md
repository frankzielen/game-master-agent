# Rollenspiel-Starterkit – Einführung

Mit diesem Paket baut dir ein KI-Assistent (**ChatGPT** oder **Claude**) eine strukturierte Ablage für deine Kampagne auf: Plot, Kapitel und Szenen, NSCs, Orte, Fraktionen, Gegenstände und Spielercharaktere, alles als verlinkte Markdown-Dateien. Danach pflegt die KI die Ablage für dich. Du erzählst deine Ideen, und sie sortiert sie ein, prüft sie auf Widersprüche und hält die Querverweise aktuell.

## Was du brauchst

Wichtig ist, dass die KI in einem **dauerhaften Ordner** arbeiten darf. Nur dann bleibt die Ablage erhalten. Ein normaler Chat ohne Ordner vergisst seine Arbeitsdateien nach einiger Zeit. Der dauerhafte Ordner liegt je nach Werkzeug auf deinem Rechner oder in der Cloud:

| | ChatGPT mit Codex | Claude-Projekt (Cloud) | Claude Code |
|---|---|---|---|
| Wo liegt die Ablage? | Ordner auf deinem Rechner | im Projektordner in der Cloud, kein Ordner auf dem Rechner nötig | Ordner auf deinem Rechner |
| Womit arbeitest du? | ChatGPT-Desktop-App im Codex-Modus, Codex-Erweiterung für VS Code oder Codex CLI | Claude-App oder claude.ai, auch am Handy | Claude-Desktop-App (Bereich „Code“), Claude-Erweiterung für VS Code oder Terminal |
| Wie kennt die KI die Regeln? | liest `AGENTS.md` automatisch | über die Projektanweisung (siehe unten) | liest `CLAUDE.md` automatisch, die auf `AGENTS.md` verweist |

Die Regeln stehen in allen Fällen nur einmal in `AGENTS.md`. Mit Codex und Claude Code kannst du sogar auf demselben Ordner zwischen ChatGPT und Claude wechseln.

**Am bequemsten ist ein Claude-Projekt:** Die Ablage liegt in der Cloud, du brauchst keinen Ordner auf dem Rechner und kannst von jedem Gerät aus weiterarbeiten. Ob Projekte mit eigenem Projektordner bei dir verfügbar sind, siehst du in der Claude-App. Wenn ja, ist das die einfachste Variante.

Außerdem:
- Optional Python 3 für die Link-Prüfung und die Website (auf Mac und Linux meist vorhanden, unter Windows bei Bedarf installieren).
- Zum Lesen der Dateien VS Code (Vorschau mit Strg/Cmd+Shift+V) oder Obsidian.

## Einrichtung im Claude-Projekt (Cloud)

1. Lege in der Claude-App ein neues Projekt an, z. B. „Meine Kampagne“.
2. Häng im Projekt-Chat `rollenspiel-starterkit.zip` an, füge den Text aus `START-PROMPT.md` ein und schicke beides ab. Beantworte die Rückfragen.
3. Claude entpackt das ZIP in den Projektordner, baut dort die Struktur auf und nennt dir zum Schluss den genauen Pfad von `AGENTS.md`. Trage dann in die Projektanweisungen ein: „Lies vor jeder Aufgabe AGENTS.md (Pfad: …) und halte dich an diese Regeln.“ So gelten die Regeln in jedem neuen Chat des Projekts.

Du findest alle Dateien in der Bibliothek bzw. der Dateiansicht des Projekts.

## Einrichtung mit Codex oder Claude Code (Ordner auf dem Rechner)

1. Öffne **Codex** bzw. **Claude Code**. Das Werkzeug fragt, in welchem Ordner es arbeiten darf. Wähle einfach einen Ort, z. B. „Dokumente“. Einen Ordner anlegen musst du nicht.
2. Häng `rollenspiel-starterkit.zip` an den Chat an, füge den Text aus `START-PROMPT.md` ein und schicke beides ab. Falls der Chat keine ZIP-Datei annimmt, lass sie im Download-Ordner, die KI findet sie dort.
3. Beantworte die Rückfragen (Kampagnenname, Welt, Spieler, vorhandene Abenteuer und Charaktere). Wenn die KI um Erlaubnis bittet, Ordner anzulegen oder Befehle auszuführen, stimme zu.

Die KI legt den Kampagnenordner selbst an, entpackt das ZIP, baut die komplette Struktur auf, übernimmt die Regeln und befüllt die ersten Dateien. Zum Schluss nennt sie dir den Pfad des Ordners. Diesen Ordner öffnest du künftig in Codex bzw. Claude Code. Dann werden die Regeln bei jeder Sitzung automatisch gelesen. Die Dateien liegen auf deinem Rechner, du kannst sie jederzeit selbst ansehen oder sichern.

**Ohne dauerhaften Ordner** (normaler Chat ohne Projektordner, bei ChatGPT oder Claude): Lade das ZIP im Chat hoch und schicke denselben Start-Prompt. Die KI baut die Struktur dann in ihrer eigenen Umgebung und gibt dir ein fertiges `kampagne.zip` zurück, das du einmal entpackst. Spätere Änderungen musst du dann als Dateien herunterladen und selbst ablegen. Mit einem Claude-Projekt, Codex oder Claude Code entfällt das.

## Die Struktur

```
README.md                    Einstieg mit Überblick und Spielern
offene-punkte.md             Widersprüche, offene Fragen, Entscheidungen
AGENTS.md                    Regeln für die KI
CLAUDE.md                    Verweis auf AGENTS.md für Claude
welt/                        gemeinsam für alle Abenteuer
  nscs/  orte/  fraktionen/  gegenstaende/  spielercharaktere/
abenteuer/                   01-titel/, 02-titel/ …: je Plot, Quests, Sitzungen
_vorlagen/                   Kopiervorlagen für jeden Dateityp
werkzeuge/                   Link-Prüfung und Website-Generator
```

Die wichtigsten Ideen dahinter:

- **Eine Welt, viele Abenteuer:** NSCs, Orte und Gegenstände gibt es nur einmal. Jedes Abenteuer hat nur seinen Plot und seine Sitzungen. Die Spielleitung darf wechseln.
- **Entwicklung über die Abenteuer:** Jeder Welt-Eintrag zeigt oben das Zeitlose und darunter den aktuellen Stand sowie einen Abschnitt pro Abenteuer. So siehst du auf einen Blick, wie sich eine Figur entwickelt hat.
- **Orte verschachtelt:** Region → Stadt → Gebäude, jeweils mit eigenem Ordner für Karten und Bilder.
- **Plot:** Hauptplot mit Zeitplan, darunter Kapitel mit Szenen. Alternative Szenen bekommen einen Buchstaben (03a, 03b), Quests liegen unter `plot/quests/`.
- **Spoiler:** Was die Spieler nicht wissen dürfen, steht unter „Geheim (nur SL)“.

## So arbeitest du mit der KI

- **Ideen einsprechen:** Einfach drauflos erzählen, gern in Bruchstücken. Die KI puffert jede Idee im `ideen-eingang.md` des Abenteuers, prüft sie gegen alles Bestehende und fragt bei Widersprüchen nach, mit Lösungsvorschlägen und einer Empfehlung. Erst danach wird eingepflegt.
- **Nach einem Spielabend:** Erzähl, was passiert ist. Die KI legt die Sitzung an, setzt gespielte Szenen auf „gespielt“ und aktualisiert NSCs, Orte und Charaktere.
- **Nach einem Abenteuer:** Bitte die KI, den „Aktuellen Stand“ in der Welt nachzuziehen. Dazu gehören die Charakter-Übersicht mit Fortschritt (z. B. Stufe) und Verbleib sowie die Gegenstände.
- **Bilder:** Bild schicken und sagen, wozu es gehört. Die KI legt es im passenden `bilder/`-Ordner ab und bindet es ein.
- **Website:** „Bau die Website neu“ erzeugt `kampagnen-archiv.html`, eine einzelne Datei mit Ordnerbaum, Suche und Bildern zum Durchklicken im Browser.

Die Regeln kannst du jederzeit ändern. Sag der KI einfach, was anders laufen soll, dann passt sie `AGENTS.md` an.
