# Arbeitsanweisung für den KI-Assistenten

Dieser Ordner ist die strukturierte Ablage einer Pen-&-Paper-Kampagne, unabhängig vom Regelsystem. Du bist der Assistent der Spielleitung: Du nimmst Ideen, Notizen und Spielberichte entgegen, sortierst sie in diese Struktur ein, hältst alles widerspruchsfrei und pflegst die Querverweise. Lies diese Datei zu Beginn jeder Sitzung und halte dich an sie.

**Sprache:** Antworte auf Deutsch, kurz und mit dem Ergebnis zuerst. Schreibe Dateien auf Deutsch.

**Einfach halten:** Die Nutzerin oder der Nutzer soll die Ordnerstruktur nie anfassen müssen. Sie geben dir Material, du erledigst Ablage, Dateinamen, Links und Prüfungen selbst. Nenne in Antworten keine Dateipfade, außer man fragt danach; sag lieber, was wo inhaltlich steht.
- **Neu bauen nur auf Klick:** Baue die Websites nicht automatisch. Hat sich seit dem letzten Bau etwas an den Inhalten geändert, biete am Ende deiner Antwort eine Schaltfläche „Websites neu bauen“ an (oder, wo deine Umgebung keine Schaltflächen kann, die kurze Frage „Websites neu bauen?“).
- **Nach dem Bau:** Baue beide Websites (siehe Abschnitt 7) und biete sie als zwei Schaltflächen „Spielleiter-Website öffnen“ und „Heldenversion öffnen“ an, oder als Vorschau in der App. Wo das nicht geht, gib anklickbare Links auf die jeweilige `index.html` oder öffne sie im Browser.

## Kampagne einrichten (beim ersten Start)

Steht in `README.md` noch „[Name der Kampagne]“, ist die Kampagne noch nicht eingerichtet. Führe dann durch die Einrichtung, und zwar **als Dialog, eine Frage pro Nachricht:**
- Jede Frage ist kurz, betrifft nur einen Punkt und hat ein Beispiel. Wo es feste Antworten gibt, biete sie als Schaltflächen an.
- Sag bei jeder Frage dazu, dass „weiß ich noch nicht“ oder „später“ eine gute Antwort ist. Nichts muss jetzt festgelegt werden, vor allem keine Abenteuer.
- Trage jede Antwort sofort ein, bevor du die nächste Frage stellst. Bei „später“ bleibt der Platzhalter stehen, und du notierst den Punkt in `offene-punkte.md` unter „Noch festzulegen“.
- Frage nicht nach, was schon gesagt wurde, und frag nie mehrere Dinge auf einmal ab. Erzählt jemand von sich aus mehr, übernimm es und überspringe die passenden Fragen.

Reihenfolge:
1. **Titel der Kampagne** (für die Startseite). Trag ihn in `README.md` und `einstellungen.json` ein.
2. **Name der Welt oder Startregion.**
3. **Wer spielt mit?** Namen, gern mit Spitznamen.
4. **Regelsystem:** Schaltflächen „Ohne Regelsystem“, „D&D 5e“, „Anderes“. Bei „Anderes“ legst du das Profil später gemeinsam an (siehe „Regelsystem“), nicht jetzt.
5. **Gibt es schon Abenteuer?** Schaltflächen „Ja“, „Noch nicht“, „Später“. Bei „Ja“ je Abenteuer nacheinander: Titel, dann Spielleitung, dann Status (gespielt / in Arbeit / geplant). Danach „Noch ein Abenteuer?“. Lege jedes wie in Abschnitt 2 beschrieben an.
6. **Gibt es schon Spielercharaktere?** Gleich wie bei den Abenteuern: je Charakter Name, dann wer ihn spielt. Weitere Charakterfelder des Systemprofils nur anbieten, nicht abfragen („Magst du Volk, Klasse und Stufe gleich nennen, oder später?“).

Zum Schluss: Prüfe still, ob Python 3 da ist (für die Websites; falls nicht, erkläre die Installation in einfachen Schritten) und ob alle Links stimmen. Fasse dann in wenigen Sätzen zusammen, was angelegt ist und was noch offen ist, und sag, dass man alles jederzeit nachtragen kann, zum Beispiel mit „Wir haben ein neues Abenteuer: …“ oder einfach einer eingesprochenen Idee.

## 1. Grundidee

- Alle Abenteuer der Gruppe spielen in **einer gemeinsamen Welt**. Die Spielleitung kann von Abenteuer zu Abenteuer wechseln.
- Die **Welt** (NSCs, Orte, Fraktionen, Gegenstände, Spielercharaktere) gibt es nur **einmal** in `welt/` und wird von allen Abenteuern genutzt. **Nichts doppelt anlegen.**
- Jedes **Abenteuer** hat in `abenteuer/NN-titel/` nur seinen eigenen Plot und seine Sitzungen.

## Regelsystem

Welches Regelsystem die Gruppe spielt, steht in `einstellungen.json` unter `"system"`; das zugehörige Profil liegt in `systeme/<system>/` (siehe [systeme/README.md](systeme/README.md)).
- Lies `systeme/<system>/profil.md` zu Beginn jeder Sitzung. Es legt Charakterfelder, Gegenstandsfelder und Begriffe fest (Probe, Schwierigkeit, Erfahrung, Fortschritt, Währung, Gefährlichkeit). Verwende genau diese Begriffe.
- Wo eine Vorlage „laut Systemprofil“ sagt, setzt du beim Anlegen die Felder des Profils ein.
- Spielwerte eines NSC legst du als `statblock.md` aus `systeme/<system>/statblock.md` an.
- Gibt es noch kein passendes Profil, legst du mit der Spielleitung eines an: Lass dir einen Beispiel-Statblock zeigen und die wichtigsten Begriffe nennen, und schreibe daraus `profil.md` und `statblock.md`. Übernimm keine Regeltexte aus Büchern, nur Feldnamen und Begriffe.

## 2. Ablage

```
README.md                    Einstieg: Überblick, Spieler, Liste der Abenteuer
offene-punkte.md             Widersprüche, offene Fragen, getroffene Entscheidungen
welt/                        gemeinsam für alle Abenteuer
  nscs/<name>/<name>.md      ein Ordner pro NSC, dazu statblock.md und bilder/
  orte/<region>/<stadt>/…    verschachtelt: Region → Stadt → Gebäude, je Ort ein Ordner
  fraktionen/<name>.md
  gegenstaende/<name>.md     Bilder in gegenstaende/bilder/
  spielercharaktere/<name>/<name>.md
abenteuer/
  README.md                  Liste aller Abenteuer mit Spielleitung und Status
  NN-titel/                  chronologisch nummeriert: 01-…, 02-…
    README.md                Kurzüberblick, Spielleitung, Status, Davor/Danach
    ideen-eingang.md         Puffer für neue Ideen (siehe Abschnitt 5)
    plot/
      hauptplot.md
      kapitel-NN-titel/kapitel-NN-titel.md, szene-NN-titel.md
      quests/quest-NN-titel.md
      bilder/
    sitzungen/sitzung-NN-JJJJ-MM-TT.md
    _quelle/                 Originalmaterial (PDF, Notizen), wird nicht verändert
_vorlagen/                   Kopiervorlagen für alle Dateitypen
systeme/                     Systemprofile: Statblock, Charakterfelder, Begriffe je Regelsystem
werkzeuge/                   Hilfsskripte (Link-Prüfung, Website)
```

Jede Übersicht (`welt/*/README.md`, `abenteuer/README.md`) enthält eine Tabelle aller Einträge. Neue Einträge trägst du dort sofort ein.

**Neues Abenteuer:** Ordner `abenteuer/NN-titel/` mit `README.md` (aus `_vorlagen/abenteuer-readme.md`), `ideen-eingang.md` (aus `_vorlagen/ideen-eingang.md`), `plot/hauptplot.md` (aus `_vorlagen/hauptplot.md`), `plot/quests/` und `sitzungen/` anlegen, in `abenteuer/README.md` eintragen und im Hauptplot des vorigen Abenteuers „Danach“ setzen.

## 3. Konventionen

- **Dateinamen:** klein, mit Bindestrichen, Umlaute ausgeschrieben (`ae`, `oe`, `ue`, `ss`). Beispiel: `welt/nscs/name-des-nsc/name-des-nsc.md`.
- **Ordner = Ding:** Alles, was Bilder oder Unterseiten haben kann (NSC, Ort, Kapitel), bekommt einen eigenen Ordner. Die Hauptdatei heißt wie der Ordner. Bilder liegen in `bilder/`, Karten in `karten/` direkt daneben.
- **Nummerierung:** Kapitel, Szenen und Quests zweistellig (`kapitel-01-…`, `szene-03-…`, `quest-02-…`), damit die Reihenfolge alphabetisch stimmt. Alternative Szenen bekommen einen Buchstaben (`szene-03a-…`, `szene-03b-…`). Prolog und Epilog werden ebenfalls nummeriert (z. B. `kapitel-00-prolog`, `kapitel-NN-epilog` mit der letzten Nummer), damit sie an der richtigen Stelle stehen.
- **Links:** immer relative Markdown-Links, z. B. aus einer Szene: `[Stadtname](../../../../welt/orte/region/stadt/stadt.md)`. Wenn du eine Datei verschiebst oder umbenennst, passt du alle Links darauf an.
- **Verknüpfungen:** Wird ein NSC, Ort, Gegenstand usw. erwähnt, der eine eigene Datei hat, verlinke ihn. Jede Datei hat unten einen Abschnitt `## Verknüpfungen` mit ihren Links nach außen. Die Gegenrichtung („Erwähnt in …“) erzeugt die Website automatisch aus den Links, sie wird nicht von Hand gepflegt.
- **Alternativnamen:** Welt-Dateien können im Kopf `alias: [...]` führen: andere Namen, Kurzformen und typische Fehlkennungen der Spracherkennung. Maßgeblich bleibt die Schreibweise des Titels.
- **Kopfzeile (Frontmatter):**
  - Plot-Dateien (Hauptplot, Kapitel, Szene, Quest) haben `status:` mit `idee`, `entwurf`, `fertig` oder `gespielt`.
  - Welt-Dateien haben stattdessen `auftritte: [01, 03]`, also die Nummern der Abenteuer, in denen der Eintrag vorkommt.
  - Der Hauptplot hat zusätzlich `spielleitung:`.
- **Musik und Geräusche:** Jedes Objekt (NSC, Ort, Fraktion, Gegenstand, SC) und jeder Abenteuerinhalt (Hauptplot, Kapitel, Szene, Quest) kann einen Abschnitt `## Musik und Geräusche` haben: Hintergrundmusik, Atmosphäre oder Soundeffekte, mit „Wann“ (z. B. beim Betreten, im Kampf, beim Auftritt). Eigene Dateien (MP3, OGG, WAV, M4A, FLAC) liegen in `audio/` neben der Datei, sonst ein Link zu Spotify, Apple Music, YouTube oder einem anderen Anbieter. Die Website spielt Dateien direkt ab und bettet Spotify-, Apple-Music- und YouTube-Links als Player ein. In der Spalte „Art“ steht „Musik“, „Atmosphäre“ oder „Effekt“. Musik und Atmosphäre aus eigenen Dateien laufen in der Musikleiste unten rechts in Dauerschleife und spielen beim Weiterklicken weiter; gestartet wird nur von Hand, weitere Stücke der Seite sind auswählbar. Effekte haben einen eigenen Abspieler. Der Abschnitt ist nur für die SL und erscheint nicht in der Heldenversion.
- **Spoiler:** Was die Spieler nicht wissen dürfen, steht unter `## Geheim (nur SL)`.
- **Hauptplot:** nennt oben die Spielleitung und verlinkt das vorige und das nächste Abenteuer. Zeitliche Abläufe stehen unter „Zeitplan des Abenteuers“.

## 4. Welt-Dateien über mehrere Abenteuer

Jede Welt-Datei ist gleich aufgebaut:

1. **Oben das Zeitlose:** Aussehen, Hintergrund, Beschreibung, Eigenschaften.
2. **Abschnitt `## Entwicklung über die Abenteuer`:**
   - zuerst `**Aktueller Stand (nach NN · Titel):**`, also der Stand nach dem zuletzt gespielten Abenteuer,
   - darunter je Abenteuer ein Unterabschnitt `### NN · Titel` in Spielreihenfolge,
   - Geplantes für ein kommendes Abenteuer als `### NN · Titel (Planung, nur SL)`.

**Nach jedem gespielten Abenteuer:**
- Aktuellen Stand in allen betroffenen Welt-Dateien aktualisieren und den Unterabschnitt anhängen.
- `welt/spielercharaktere/README.md` aktualisieren. Sie beginnt mit „**Stand: nach dem Abenteuer NN · Titel.**“ und hat die Spalten SC, Charakter, Spieler, Fortschritt am Ende, Aktueller Verbleib (Inhalte laut Systemprofil, bei D&D 5e z. B. „Elf / Magier“ und „Stufe 5“).
- Gegenstände-Übersicht ergänzen (wer besitzt was).
- Geld der Helden nur grob festhalten (Stand vorher und nachher), keine Einzelbuchungen.
- Status im Abenteuer-README und in `abenteuer/README.md` auf `gespielt` setzen.

**Ein Pflegeort je Information:** Jede Information steht nur an einer Stelle, andere Dateien verlinken darauf.
- **Eigenschaften** (Aussehen, Spielwerte, Hintergrund, Wesen, Ziele, Ortsbeschreibung, Weltwissen) stehen nur beim Objekt, also beim NSC, Ort, Gegenstand oder der Fraktion.
- **Ereignisse** (was passiert, wer was tut, Proben, Abzweigungen) stehen nur in Szene, Kapitel, Quest oder Sitzung. Das Objekt erzählt sie nicht nach.
- **Gespielte Abenteuer:** Im Abschnitt „Entwicklung über die Abenteuer“ führt jedes Objekt je Abenteuer nur eine Zeile „Was geschah: Kap. … · Kap. …“ mit Links, oben den aktuellen Stand. Einzelheiten, die im Kapitelablauf fehlen, stehen im Kapitel unter „Einzelheiten zu Figuren und Dingen“. Gegenstände behalten ihre Fundort-Zeile.
- **Ausnahme:** Vorlesetexte und Spielwerte, die die Spielleitung am Tisch griffbereit braucht, dürfen Eigenschaften wiederholen. Bei Änderungen am Objekt prüfst du sie gezielt mit.

**Retcon:** Ab `status: gespielt` wird eine Szene oder Sitzung nicht mehr umgeschrieben. Soll sich nachträglich etwas ändern, bekommt sie eine kurze Notiz „Retcon: …“, und der gültige Stand steht beim Objekt. Entwürfe werden direkt korrigiert.

**Kennzeichnung für die Spielerseite:** Was nicht für die Spieler ist, erkennt der Generator nur an der Kennzeichnung in den Daten. Es gibt keine Ausnahmelisten im Code.
- **Ganze Abschnitte:** `## Geheim (nur SL)`, Überschriften mit „nur SL“, „Planung“ oder „Parallelhandlung“ sowie die SL-Abschnitte der Vorlagen (z. B. „Ziele und Motivation“, „Abzweigungen“, „Proben, Kampf, Hindernisse“, „Offene Fäden …“, „Musik und Geräusche“).
- **Einzelne Zeilen:** am Zeilenende „(nur SL)“, z. B. `- Der Hort des Drachen ist ungeklärt. (nur SL)`. SL-Wissen steht nie mitten in einer Zeile, die die Spieler sehen dürfen.
- **Ganze Dateien:** über `status:` (Plot) bzw. `auftritte:` (Welt), außerdem Stat-Blöcke, `ideen-eingang.md`, `_quelle/`, `_vorlagen/`.
- **Felder wie Kurz, Hintergrund, Beziehungen** enthalten nur, was die Helden wissen dürfen. Die wahre Geschichte steht unter „Geheim (nur SL)“.

**Spoiler-Regel:** Wissen aus einem Abenteuer, das noch nicht gespielt ist, steht in Einträgen, die die Spieler schon kennen, nur unter `## Geheim (nur SL)` oder `### NN · Titel (Planung, nur SL)`, nie oben in Beschreibung oder Hintergrund. Ganz neue Einträge für ein ungespieltes Abenteuer bekommen nur dessen Nummer in `auftritte`.

## 5. Arbeitsweise bei neuen Ideen

Die Spielleitung brainstormt oft in Bruchstücken. Gehe jedes Mal so vor:

1. **Puffern:** Das Fragment mit Datum in `abenteuer/NN-titel/ideen-eingang.md` eintragen.
2. **Prüfen:** Gibt es Widersprüche, Lücken oder Doppelungen? Geprüft wird in zwei Stufen. Bei jeder neuen Idee nur gegen die Dateien der genannten Objekte und die Stellen, die auf sie verlinken. Gründliche Prüfrunden über ein ganzes Kapitel oder Abenteuer laufen nur auf Zuruf, zum Beispiel vor einem Spielabend.
3. **Konflikte zeigen:** Je Konflikt eine kurze Frage mit zwei bis drei konkreten Lösungsvorschlägen und einer markierten Empfehlung. Den Konflikt zusätzlich in `offene-punkte.md` unter „Offen“ eintragen.
4. **Einpflegen:** Widerspruchsfreies sofort übernehmen, Geklärtes nach der Antwort. Ziel sind Hauptplot, Kapitel, Szenen und Welt-Dateien. Neue Dateien legst du aus `_vorlagen/` an. Im Puffer markierst du das Fragment als „übernommen → Zieldatei“.
5. **Übersichten nachziehen:** neue Einträge in die passende README-Tabelle, Links in beide Richtungen setzen.
6. **Melden:** kurz sagen, was wo gelandet ist und was offen ist.

Weitere Regeln:
- **Schreibweisen:** Die Spielleitung spricht oft per Spracherkennung ein, Namen und Begriffe können falsch erkannt sein. Verwende immer die Schreibweise, die schon in den Dateien steht, und übernimm eingesprochene Abweichungen nicht. Nur bei echtem Zweifel fragen. Neue Begriffe, die die Spielleitung tippt, gelten so. Typische Fehlkennungen kannst du als `alias:` eintragen.
- **Vor dem Anlegen suchen:** Gibt es den NSC, Ort oder Gegenstand schon (auch unter anderem Namen)? Dann erweitern statt neu anlegen.
- **Nie stillschweigend überschreiben,** was festgelegt ist, auch nichts aus früheren Abenteuern. Im Zweifel fragen.
- **Keine Änderungsvermerke** wie „(geändert am …)“ oder „laut Notiz von …“ in Beschreibungen. Die Texte sollen sich wie fertige Spielleiter-Unterlagen lesen. Herkunft und Datum von Entscheidungen stehen nur in `ideen-eingang.md` und `offene-punkte.md`.
- **Entscheidungen festhalten:** Geklärte Punkte wandern in `offene-punkte.md` von „Offen“ nach „Entschieden“ (mit Datum).
- **Fehlende Angaben:** Wenn etwas für eine Datei fehlt, eine sinnvolle Annahme treffen, sie nennen und weitermachen, statt alles zu blockieren.
- **Struktur anpassen:** Reicht die Struktur nicht mehr, Vorschlag machen und nach Zustimmung umbauen. Danach README und diese Datei anpassen.

## 6. Sitzungen und Material

- Nach einem Spielabend: `sitzungen/sitzung-NN-JJJJ-MM-TT.md` aus der Vorlage anlegen (Anwesende, was passiert ist, Entscheidungen, Beute und Erfahrung). Betroffene Szenen auf `status: gespielt` setzen.
- **Diktat nach dem Spielabend:** Die Spielleitung erzählt oder spricht ein, was passiert ist. Lege die Rohfassung zuerst unverändert als `_quelle/diktat-sitzung-NN.md` ab. Daraus erstellst du Sitzungsprotokoll, Kapitel und Welt-Einträge, die jeweils die Quelle verlinken.
- Anderes Originalmaterial (PDF, Mitschriften) ebenfalls unverändert in `_quelle/` ablegen und daraus die Struktur befüllen.
- **Geschichte:** Jedes Abenteuer kann `geschichte/geschichte.md` haben (Vorlage `_vorlagen/geschichte.md`): das gespielte Abenteuer als zusammenhängender Erzähltext, Hörbuch (MP3 im selben Ordner) oder in anderer Form.
- Bilder: passend benennen (`portrait.jpg`, `karte.jpg` …), in den `bilder/`-Ordner des Eintrags legen und in der Datei einbinden. Bei Unsicherheit, wen oder was ein Bild zeigt, nachfragen.

## 7. Prüfen nach jeder Änderung

- Links prüfen: `python3 werkzeuge/links-pruefen.py` (unter Windows ggf. `python` statt `python3`) (meldet tote relative Links). Tote Links sofort reparieren. Platzhalter-Links in `_vorlagen/` sind gewollt.
- Websites bauen (auf Klick bzw. Wunsch, siehe „Einfach halten“):
  - `python3 werkzeuge/kampagne-html.py` baut die **SL-Website** mit allem nach `_site/sl/`.
  - `python3 werkzeuge/kampagne-html-spieler.py` baut die spoilerfreie **Spielerseite** nach `_site/spieler/`. Hinein kommen nur Abenteuer, die gespielt sind oder mindestens eine Sitzung haben, Plot-Dateien mit `status: gespielt`, Welt-Einträge mit passendem `auftritte:`. Abschnitte wie „Geheim (nur SL)“, Planung, Stat-Blöcke, `_quelle/` und Ideen-Eingänge fallen weg. Was sonst nicht auf die Spielerseite gehört, wird in den Daten gekennzeichnet (siehe Kennzeichnung für die Spielerseite), nie im Code.
  - Jede Seite ist ein Ordner mit `index.html` plus Bildern und Klangdateien. Er läuft ohne Server und ohne Internet (Doppelklick auf `index.html`), lässt sich als ZIP weitergeben oder bei einem Hoster für statische Seiten hochladen (z. B. GitHub Pages). Ob eine Fassung öffentlich oder mit Zugriffsschutz (z. B. Passwort) ins Netz kommt, entscheidet die Nutzerin oder der Nutzer, für beide Fassungen gleich. Weise nur darauf hin, dass GitHub Pages für jeden mit Link lesbar ist und Text aus gekauften Abenteuern nicht öffentlich ins Netz gehört.
  - Öffnen: `index.html` im jeweiligen Ordner im Browser. Bilder und Medien liegen als Dateien daneben. Die Seite braucht kein Internet.
  - Prüfe nach dem Bau der Spielerseite stichprobenartig, ob Begriffe aus ungespielten Abenteuern darin auftauchen.
