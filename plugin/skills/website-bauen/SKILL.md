---
name: website-bauen
description: Die Spielleiter-Website und die Spieler-Website eines GMA-Almanachs erzeugen und direkt zum Öffnen anbieten. Wenn die Nutzerin oder der Nutzer „Websites neu bauen“ wählt oder darum bittet.
---

# Website bauen

1. Links prüfen: `python3 werkzeuge/links-pruefen.py`, tote Links zuerst reparieren.
2. Bauen, je nach Wunsch:
   - Spielleiter-Website: `python3 werkzeuge/almanach-html.py` → `_site/sl/`
   - Spieler-Website: `python3 werkzeuge/almanach-html-spieler.py` → `_site/spieler/`
3. Nach dem Bau der Spieler-Website stichprobenartig prüfen, ob Begriffe aus ungespielten Abenteuern oder SL-Abschnitten darin stehen. Gefundenes in den Daten kennzeichnen (nie im Code ausnehmen) und neu bauen.
4. Für den Chat zusätzlich mit `--eine-datei` bauen (Bilder in der Datei) und beide Seiten so anhängen, nie als ZIP; wo möglich als Schaltflächen „Spielleiter-Website öffnen“ und „Spieler-Website öffnen“ oder als Vorschau. Nie die `index.html` ausliefern, sie leitet nur weiter.
5. Sind Websites veröffentlicht (`einstellungen.json`, `"veroeffentlicht"`) und hat die Person „online aktualisieren“ gewählt, dieselben Veröffentlichungen aktualisieren, damit die Links bleiben. Alles Weitere zur Weitergabe steht in `AGENTS.md` unter „Bereitstellung“.
