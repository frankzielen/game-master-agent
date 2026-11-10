# GMA – Game Master Agent

**An AI agent for creating and managing pen & paper RPG worlds and adventures.**

[English](#english) · [Deutsch](#deutsch)

---

## English

GMA turns an AI coding agent (Claude, ChatGPT and similar) into a game master's assistant. You talk to it like a colleague: dictate ideas, session reports or notes, hand it maps and stat blocks. The agent files everything into your **role-playing almanac**, a fixed folder structure for your world and all its adventures, checks it for contradictions, keeps cross-references up to date and can publish it as a website.

GMA is not a program with its own AI. It is a set of rules, templates and small tools that an existing agent reads and follows.

### What you can use it for

- **Create and prepare adventures:** design your own adventures, or bring existing and purchased ones into a structured form for your group.
- **Build worlds:** places, characters, factions, items and history, independent of any single adventure.
- **Document played adventures:** record what the group experienced and how the world changed.

Not only for game masters: players can document sessions too, taking turns or together, and help build the world.

### How it works

1. **Input:** notes, dictated ideas and session reports, handouts, images, stat blocks, sound and music, in any form.
2. **Storage:** linked Markdown files in a fixed structure. The world exists once, each adventure only holds its own plot and sessions. Secrets are marked in the data.
3. **Output:** a website to browse, in two versions: the complete **game master website** and a cleaned **player website** that only shows what the characters know. It runs offline, and the agent can publish it for your players via Claude or ChatGPT, on your own web space (e.g. GitHub Pages) or as a ZIP. Public or private is your choice.

GMA works with any rules system. Everything rule-specific lives in a system profile (`kampagne/systeme/`). Included: **No rules system** (free-form values, default) and **D&D 5e** (field names based on the SRD 5.2). The agent helps you create profiles for other systems.

### Requirements

- A project in the Claude or ChatGPT app, connected either to a folder on your computer or to a GitHub repository (Claude Code, Codex and similar agents work too). Plain chats without folder access are not suitable. This usually requires a paid plan; check the current plans of Anthropic and OpenAI.
- Python 3 for the website tools (no extra packages). The agent helps you install it if needed.

### Getting started

1. **Local folder:** download the ZIP and unpack it. Create a project in the Claude or ChatGPT app and connect the unpacked folder.
2. **GitHub repository:** click "Use this template" to get your own copy. Create a project in the Claude or ChatGPT app and connect your copy.

Then write: "Follow START.md."

The agent does the rest and guides you through the setup step by step. Details: [docs/start-prompt.md](docs/start-prompt.md).

The rules for the agent are in [kampagne/AGENTS.md](kampagne/AGENTS.md) (currently in German; an English version will follow).

### What's in the repository

| Folder | Content |
|---|---|
| `kampagne/` | the empty campaign: rules for the agent (`AGENTS.md`), templates, system profiles, tools |
| `beispiel/` | a small fictional example campaign; build both websites and compare them |
| `plugin/` | workflows as skills for Claude Code: set up a campaign, add an idea, record a session, check consistency, build the websites |
| `docs/` | start prompt and introduction |
| `.github/workflows/` | publishes the heroes' version to GitHub Pages, only when started by hand |

Install the Claude Code plugin with `/plugin marketplace add <owner>/game-master-agent` and `/plugin install gma@game-master-agent`. Other agents follow the same workflows from `AGENTS.md`.

### Licence

- Code (`kampagne/werkzeuge/`, plugin): [PolyForm Shield 1.0.0](LICENSE). Any use is allowed, including commercial use: you may show GMA in monetised videos, streams and posts. You may not sell GMA itself or offer a competing product or service based on it.
- Rules, templates and the example campaign: [CC BY 4.0](LICENSE-CONTENT).
- Your own campaign is yours.
- D&D profile: includes material from the SRD 5.2 by Wizards of the Coast LLC, licensed under CC BY 4.0 (see the profile). "Dungeons & Dragons" and "D&D" are trademarks of Wizards of the Coast; GMA is not affiliated with or endorsed by Wizards of the Coast.
- Purchased adventures may be prepared for your own group, but do not publish their text.

---

## Deutsch

GMA macht aus einem KI-Agenten (Claude, ChatGPT und ähnliche) einen Assistenten für die Spielleitung. Man spricht mit ihm wie mit einem Kollegen: Ideen, Spielberichte oder Notizen einsprechen, Karten und Statblöcke übergeben. Der Agent legt alles in deinem **Rollenspiel-Almanach** ab, einer festen Ordnerstruktur für deine Welt und all ihre Abenteuer, prüft auf Widersprüche, hält Querverweise aktuell und macht den Bestand als Website verfügbar.

GMA ist kein eigenes Programm mit eigener KI. Es besteht aus Regeln, Vorlagen und kleinen Werkzeugen, die ein vorhandener Agent liest und befolgt.

### Wozu man GMA nutzen kann

- **Abenteuer erstellen und aufbereiten:** eigene Abenteuer entwerfen, oder vorhandene und gekaufte Abenteuer strukturiert für die eigene Gruppe aufbereiten.
- **Welten erstellen:** Orte, Figuren, Fraktionen, Gegenstände und Geschichte, unabhängig von einzelnen Abenteuern.
- **Gespielte Abenteuer dokumentieren:** festhalten, was die Gruppe erlebt hat und wie sich die Welt verändert.

Nicht nur für Spielleitungen: Auch Spielerinnen und Spieler können dokumentieren, abwechselnd oder gemeinsam, und beim Weltenbau mitwirken.

### Wie GMA arbeitet

1. **Eingabe:** Notizen, eingesprochene Ideen und Spielberichte, Handouts, Bilder, Statblöcke, Musik und Geräusche, in beliebiger Form.
2. **Ablage:** verlinkte Markdown-Dateien in fester Struktur. Die Welt gibt es nur einmal, jedes Abenteuer hat nur seinen Plot und seine Sitzungen. Geheimnisse sind in den Daten gekennzeichnet.
3. **Ausgabe:** eine Website zum Durchklicken in zwei Fassungen: die vollständige **Spielleiter-Website** und eine bereinigte **Spieler-Website**, die nur zeigt, was die Helden wissen. Sie läuft offline, und der Agent stellt sie deinen Spielern auf Wunsch bereit: über Claude oder ChatGPT, auf eigenem Webspace (z. B. GitHub Pages) oder als ZIP. Öffentlich oder privat entscheidest du.

GMA ist an kein Regelsystem gebunden. Alles Regelspezifische steht in einem Systemprofil (`kampagne/systeme/`). Mitgeliefert: **Ohne Regelsystem** (freie Werte, Standard) und **D&D 5e** (Feldnamen nach dem SRD 5.2). Für andere Systeme legt der Agent mit dir ein Profil an.

### Voraussetzungen

- Ein Projekt in der Claude- oder ChatGPT-App, verbunden mit einem Ordner auf deinem Rechner oder mit einem GitHub-Repository (Claude Code, Codex und ähnliche Agenten gehen auch). Normale Chats ohne Ordnerzugriff sind nicht geeignet. Dafür ist in der Regel ein Bezahltarif nötig; die aktuellen Tarife von Anthropic und OpenAI bitte selbst prüfen.
- Python 3 für die Website-Werkzeuge (ohne Zusatzpakete). Der Agent hilft bei Bedarf bei der Installation.

### Loslegen

1. **Lokaler Ordner:** das ZIP herunterladen und entpacken. In der Claude- oder ChatGPT-App ein Projekt anlegen und den entpackten Ordner verbinden.
2. **GitHub-Repository:** „Use this template“ klicken, das legt deine eigene Kopie an. In der Claude- oder ChatGPT-App ein Projekt anlegen und die Kopie verbinden.

Dann schreiben: „Folge START.md.“

Den Rest erledigt der Agent, durch die Einrichtung führt er Schritt für Schritt. Details: [docs/start-prompt.md](docs/start-prompt.md). Eine Einführung steht in [docs/einfuehrung.md](docs/einfuehrung.md).

Die Regeln für den Agenten stehen in [kampagne/AGENTS.md](kampagne/AGENTS.md).

### Was im Repository liegt

| Ordner | Inhalt |
|---|---|
| `kampagne/` | die leere Kampagne: Regeln für den Agenten (`AGENTS.md`), Vorlagen, Systemprofile, Werkzeuge |
| `beispiel/` | eine kleine erfundene Beispielkampagne; beide Websites bauen und vergleichen |
| `plugin/` | Abläufe als Skills für Claude Code: Kampagne einrichten, Idee einpflegen, Sitzung erfassen, Konsistenz prüfen, Website bauen |
| `docs/` | Start-Prompt und Einführung |
| `.github/workflows/` | veröffentlicht die Spieler-Website auf GitHub Pages, nur wenn man es von Hand startet |

Das Claude-Code-Plugin installiert man mit `/plugin marketplace add <owner>/game-master-agent` und `/plugin install gma@game-master-agent`. Andere Agenten folgen denselben Abläufen aus `AGENTS.md`.

### Lizenz

- Code (`kampagne/werkzeuge/`, Plugin): [PolyForm Shield 1.0.0](LICENSE). Jede Nutzung ist erlaubt, auch kommerziell: GMA darf in monetarisierten Videos, Streams und Posts gezeigt werden. Nicht erlaubt ist, GMA selbst zu verkaufen oder darauf ein Konkurrenzprodukt oder einen Dienst aufzubauen.
- Regelwerk, Vorlagen und Beispielkampagne: [CC BY 4.0](LICENSE-CONTENT).
- Deine eigene Kampagne gehört dir.
- D&D-Profil: enthält Material aus dem SRD 5.2 von Wizards of the Coast LLC unter CC BY 4.0 (siehe Profil). „Dungeons & Dragons“ und „D&D“ sind Marken von Wizards of the Coast; GMA steht in keiner Verbindung zu Wizards of the Coast.
- Gekaufte Abenteuer dürfen für die eigene Gruppe aufbereitet, ihr Text aber nicht veröffentlicht werden.
