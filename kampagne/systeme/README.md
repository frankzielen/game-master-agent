# Systemprofile

GMA ist an kein Regelsystem gebunden. Alles Regelspezifische steht in einem Systemprofil. Welches gilt, steht in `einstellungen.json` unter `"system"` (Ordnername).

| Profil | Ordner | Wofür |
|---|---|---|
| Ohne Regelsystem | [ohne-regelsystem/](ohne-regelsystem/profil.md) | Eigenbau-Regeln, regelleichtes Spiel, reiner Weltenbau oder Dokumentation ohne Spielwerte |
| D&D 5e | [dnd-5e/](dnd-5e/profil.md) | Dungeons & Dragons, 5. Edition (Feldnamen nach dem SRD 5.2) |

Jedes Profil hat zwei Dateien:
- `profil.md`: Charakterfelder, Gegenstandsfelder und Begriffe (Probe, Schwierigkeit, Erfahrung, Fortschritt, Währung), dazu auf Wunsch Hausregeln.
- `statblock.md`: Vorlage für die Spielwerte eines NSC oder Monsters.

**Eigenes Profil:** Ordner `systeme/<name>/` mit denselben zwei Dateien anlegen. Der Agent hilft dabei: Man zeigt ihm einen Beispiel-Statblock und nennt die wichtigsten Begriffe. Ein Profil enthält nur Feldnamen und Begriffe, keine Regeltexte aus Büchern.
