---
name: kampagne-einrichten
description: Neue GMA-Kampagne einrichten (Titel, Welt, Mitspieler, Regelsystem, Abenteuer, Spielercharaktere) in einem leeren GMA-Kampagnenordner. Verwenden, wenn jemand mit GMA neu anfängt.
---

# Kampagne einrichten

Arbeite im Kampagnenordner (dort liegen `AGENTS.md`, `einstellungen.json`, `welt/`, `abenteuer/`).

1. Lies `AGENTS.md` vollständig. Sie gilt ab jetzt für jede Arbeit in diesem Ordner.
2. Stelle in EINER Nachricht diese Fragen und warte auf die Antwort:
   1. Titel der Kampagne
   2. Name der Welt bzw. Startregion
   3. Wer spielt mit (Namen, gern mit Spitznamen)
   4. Vorhandene Abenteuer: Titel, Spielleitung, Status (gespielt / in Arbeit / geplant), in Spielreihenfolge
   5. Regelsystem: mitgeliefert sind „Ohne Regelsystem“ und „D&D 5e“ (`systeme/`); für andere Systeme legt ihr gemeinsam ein Profil an
   6. Vorhandene Spielercharaktere: Name, Spieler und die Charakterfelder des Systemprofils
3. Trage Titel, Welt und Mitspieler in `README.md` ein, den Titel auch in `einstellungen.json`.
4. Trage das Regelsystem in `einstellungen.json` unter `"system"` ein. Fehlt ein passendes Profil: Beispiel-Statblock und wichtigste Begriffe erfragen, `systeme/<name>/profil.md` und `statblock.md` anlegen (siehe `systeme/README.md`), nur Feldnamen und Begriffe, keine Regeltexte.
5. Lege je Abenteuer `abenteuer/NN-titel/` an wie in `AGENTS.md` beschrieben (README, ideen-eingang, plot/hauptplot, plot/quests/, sitzungen/) und trage es in `abenteuer/README.md` ein.
6. Lege je Spielercharakter `welt/spielercharaktere/<name>/<name>.md` aus der Vorlage an und trage ihn in die Übersicht ein.
7. Prüfe, ob Python 3 verfügbar ist; falls nicht, erkläre die Installation. Führe dann `python3 werkzeuge/links-pruefen.py` aus und repariere tote Links.
8. Zeige die angelegte Struktur als Baum und erkläre in drei Sätzen, wie man ab jetzt arbeitet.
