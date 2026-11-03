# Orte

Verschachtelt wie in der Welt: Region → Stadt → Gebäude. Jeder Ort hat einen eigenen Ordner, die Hauptdatei heißt wie der Ordner. Karten liegen in `karten/`, Bilder in `bilder/`. Vorlage: [_vorlagen/ort.md](../../_vorlagen/ort.md).

```
orte/
  region/
    region.md
    stadt/
      stadt.md
      gebaeude/
        gebaeude.md
```

| Ort | Typ | Liegt in | Kurz |
|---|---|---|---|
| [Salzmarsch](salzmarsch/salzmarsch.md) | Region | – | Küstenland |
| [Graufurt](salzmarsch/graufurt/graufurt.md) | Dorf | Salzmarsch | Fischerdorf mit Leuchtturm |
