---
name: sitzung-erfassen
description: Einen Spielabend in einem GMA-Almanach erfassen, aus Diktat, Notizen oder Mitschrift. Verwenden nach einer gespielten Sitzung.
---

# Sitzung erfassen

Grundlage ist `AGENTS.md`, Abschnitt 6.

1. **Quelle sichern:** Diktat oder Notizen zuerst unverändert als `abenteuer/NN-titel/_quelle/diktat-sitzung-NN.md` ablegen (anderes Material ebenfalls unverändert in `_quelle/`).
2. **Protokoll:** `sitzungen/sitzung-NN-JJJJ-MM-TT.md` aus `_vorlagen/sitzung.md` anlegen: Anwesende, was passiert ist, Entscheidungen, Beute und Erfahrung (Begriffe laut Systemprofil), Zeile „Quelle:“ mit Link.
3. **Plot:** gespielte Szenen und Kapitel auf `status: gespielt` setzen; ab dann nicht mehr umschreiben; bewusste Änderungen der Geschichte als „Retcon: …“ vermerken, Erfassungsfehler direkt korrigieren.
4. **Welt:** betroffene Objekte aktualisieren: „Aktueller Stand“ und der Abschnitt des Abenteuers unter „Entwicklung über die Abenteuer“, `auftritte:` ergänzen, neue Objekte aus `_vorlagen/` anlegen. Schreibweisen aus den Dateien verwenden.
5. Unklares nicht raten, sondern in `offene-punkte.md` und als Rückfrage festhalten.
6. `python3 werkzeuge/links-pruefen.py` ausführen.
7. **Melden:** kurze Zusammenfassung, geänderte Dateien, offene Fragen.
