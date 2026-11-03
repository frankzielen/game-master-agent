---
name: idee-einpflegen
description: Eine neue Idee, ein Fragment oder eine Änderung zu Abenteuer oder Welt in einer GMA-Kampagne puffern, prüfen und einpflegen. Verwenden bei eingesprochenen oder getippten Ideen.
---

# Idee einpflegen

Grundlage ist `AGENTS.md`, Abschnitte 3 bis 5. Ablauf:

1. **Puffern:** Fragment mit Datum in `abenteuer/NN-titel/ideen-eingang.md` eintragen (bei reinen Weltideen im Abenteuer, um das es gerade geht, oder nachfragen).
2. **Schreibweisen:** Namen und Begriffe auf die schon vorhandene Schreibweise abbilden (auch über `alias:`), eingesprochene Abweichungen nicht übernehmen.
3. **Prüfen (Stufe 1):** nur gegen die Dateien der genannten Objekte und die Stellen, die auf sie verlinken. Widersprüche, Lücken, Doppelungen suchen.
4. **Konflikte zeigen:** je Konflikt eine kurze Frage mit zwei bis drei Lösungsvorschlägen und einer Empfehlung; zusätzlich in `offene-punkte.md` unter „Offen“.
5. **Einpflegen:** Widerspruchsfreies sofort, Geklärtes nach der Antwort. Pflegeort beachten: Eigenschaften beim Objekt, Ereignisse in Szene, Kapitel oder Quest, sonst nur verlinken. Neue Dateien aus `_vorlagen/`, Felder laut Systemprofil. SL-Wissen kennzeichnen (`## Geheim (nur SL)`, Planung, Zeilenende „(nur SL)“). Keine Änderungsvermerke im Text.
6. **Nachziehen:** README-Tabellen, Verknüpfungen, `auftritte:`; im Puffer „übernommen → Zieldatei“ vermerken.
7. `python3 werkzeuge/links-pruefen.py` ausführen.
8. **Melden:** kurz, was wo gelandet ist und was offen ist.
