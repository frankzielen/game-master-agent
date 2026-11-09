---
name: konsistenz-pruefen
description: Gründliche Prüfrunde einer GMA-Kampagne auf Widersprüche, Lücken, Doppelungen und Spoiler, für ein Kapitel, ein Abenteuer oder die Welt. Nur auf ausdrücklichen Wunsch, z. B. vor einem Spielabend.
---

# Konsistenz prüfen (Stufe 2)

1. Umfang klären: Kapitel, Abenteuer oder Weltbereich.
2. Alle Dateien im Umfang und alle Objekte, auf die sie verlinken, lesen.
3. Prüfen auf:
   - Widersprüche zwischen Plot, Szenen und Welt-Einträgen (Namen, Orte, Zeiten, wer weiß was)
   - Doppelungen gegen die Pflegeort-Regel (Eigenschaften nur beim Objekt, Ereignisse nur in Szene/Kapitel)
   - fehlende Verknüpfungen, `auftritte:`, README-Einträge
   - abweichende Schreibweisen (direkt auf die gültige Schreibweise korrigieren)
   - SL-Wissen ohne Kennzeichnung in Einträgen, die die Spieler schon kennen
   - Begriffe, die nicht zum Systemprofil passen
4. `python3 werkzeuge/links-pruefen.py` ausführen.
5. Ergebnis als Liste melden, je Punkt mit Vorschlag und Empfehlung; Offenes in `offene-punkte.md`. Nichts ohne Zustimmung umschreiben, außer eindeutigen Tippfehlern und toten Links.
