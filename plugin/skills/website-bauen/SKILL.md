---
name: website-bauen
description: Die Spielleiter-Website und die Heldenversion einer GMA-Kampagne erzeugen und direkt zum Öffnen anbieten. Wenn die Nutzerin oder der Nutzer „Websites neu bauen“ wählt oder darum bittet.
---

# Website bauen

1. Links prüfen: `python3 werkzeuge/links-pruefen.py`, tote Links zuerst reparieren.
2. Bauen, je nach Wunsch:
   - Spielleiter-Website: `python3 werkzeuge/kampagne-html.py` → `_site/sl/`
   - Heldenversion: `python3 werkzeuge/kampagne-html-spieler.py` → `_site/spieler/`
3. Nach dem Bau der Heldenversion stichprobenartig prüfen, ob Begriffe aus ungespielten Abenteuern oder SL-Abschnitten darin stehen. Gefundenes in den Daten kennzeichnen (nie im Code ausnehmen) und neu bauen.
4. Beide Seiten als zwei Schaltflächen „Spielleiter-Website öffnen“ und „Heldenversion öffnen“ anbieten (oder als Vorschau), wenn die Umgebung das kann, sonst als anklickbaren Link auf `spielleiter.html` bzw. `spieler.html` oder im Browser öffnen (nie die `index.html`, sie leitet nur weiter). Nur auf Nachfrage erklären: Ordner öffnen und die Datei im Browser starten (läuft offline), als ZIP weitergeben oder bei einem Hoster für statische Seiten hochladen. Öffentlich oder mit Zugriffsschutz entscheidet die Nutzerin oder der Nutzer. Hinweisen: GitHub Pages ist für jeden mit Link lesbar; Text aus gekauften Abenteuern gehört nicht öffentlich ins Netz.
