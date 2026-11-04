---
name: kampagne-einrichten
description: Neue GMA-Kampagne im Dialog einrichten, Frage für Frage (Titel, Welt, Mitspieler, Regelsystem, optional Abenteuer und Spielercharaktere), in einem leeren GMA-Kampagnenordner. Verwenden, wenn jemand mit GMA neu anfängt.
---

# Kampagne einrichten

Arbeite im Kampagnenordner (dort liegen `AGENTS.md`, `einstellungen.json`, `welt/`, `abenteuer/`).

1. Lies `AGENTS.md` vollständig. Sie gilt ab jetzt für jede Arbeit in diesem Ordner.
2. Führe die Einrichtung als Dialog, genau wie in `AGENTS.md` unter „Kampagne einrichten (beim ersten Start)“ beschrieben: eine Frage pro Nachricht, mit Beispiel, feste Antworten als Schaltflächen, „weiß ich noch nicht“ oder „später“ ausdrücklich erlaubt. Trage jede Antwort sofort ein. Reihenfolge: Titel, Welt, Mitspieler, Regelsystem, Abenteuer (optional, je Abenteuer Titel, Spielleitung, Status nacheinander), Spielercharaktere (optional, Name und Spieler; weitere Felder nur anbieten).
3. Abenteuer legst du wie in `AGENTS.md` beschrieben an (README, ideen-eingang, plot/hauptplot, plot/quests/, sitzungen/) und trägst sie in `abenteuer/README.md` ein; Spielercharaktere als `welt/spielercharaktere/<name>/<name>.md` aus der Vorlage, eingetragen in die Übersicht. Offen Gelassenes kommt nach `offene-punkte.md` unter „Noch festzulegen“.
4. Wählt jemand ein anderes Regelsystem, trage es erst ein, wenn das Profil steht (siehe `systeme/README.md`); bis dahin bleibt „ohne-regelsystem“.
5. Prüfe still, ob Python 3 verfügbar ist; falls nicht, erkläre die Installation. Führe dann `python3 werkzeuge/links-pruefen.py` aus und repariere tote Links.
6. Fasse in wenigen Sätzen zusammen, was angelegt ist und was offen bleibt, ohne Dateipfade, und sag, dass man alles jederzeit nachtragen kann.
