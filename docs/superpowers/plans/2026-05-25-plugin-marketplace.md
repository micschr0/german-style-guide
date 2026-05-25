# Plugin-Marketplace-Infrastruktur Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Das Repo mit Plugin-Marketplace-Infrastruktur ausstatten, sodass die Installation auf zwei Claude Code Befehle reduziert wird.

**Architecture:** Zwei JSON-Konfigurationsdateien in `.claude-plugin/` machen das Repo zu einem selbstständigen Marketplace. `SKILL.md` und `referenz.md` werden in das Unterverzeichnis `skills/german-style-guide/` verschoben, auf das `plugin.json` zeigt. Das README bekommt den neuen Installationsabschnitt.

**Tech Stack:** JSON, Markdown, Git

---

## Datei-Übersicht

| Aktion | Pfad |
|--------|------|
| Erstellen | `.claude-plugin/plugin.json` |
| Erstellen | `.claude-plugin/marketplace.json` |
| Verschieben | `SKILL.md` → `skills/german-style-guide/SKILL.md` |
| Verschieben | `referenz.md` → `skills/german-style-guide/referenz.md` |
| Ändern | `README.md` (Installationsabschnitt) |

---

### Task 1: `.claude-plugin/plugin.json` erstellen

**Files:**
- Create: `.claude-plugin/plugin.json`

- [ ] **Schritt 1: Verzeichnis und Datei erstellen**

```bash
mkdir -p .claude-plugin
```

Inhalt von `.claude-plugin/plugin.json`:

```json
{
  "name": "german-style-guide",
  "description": "Deutsche Stilregeln für technische Texte — DevOps, Entwickler, Architekten",
  "version": "1.0.0",
  "author": { "name": "micschr0" },
  "license": "MIT",
  "skills": ["./skills/german-style-guide"]
}
```

- [ ] **Schritt 2: JSON-Syntax prüfen**

```bash
python3 -c "import json; json.load(open('.claude-plugin/plugin.json')); print('OK')"
```

Erwartete Ausgabe: `OK`

- [ ] **Schritt 3: Committen**

```bash
git add .claude-plugin/plugin.json
git commit -m "feat: add plugin.json for Claude Code plugin system"
```

---

### Task 2: `.claude-plugin/marketplace.json` erstellen

**Files:**
- Create: `.claude-plugin/marketplace.json`

- [ ] **Schritt 1: Datei erstellen**

Inhalt von `.claude-plugin/marketplace.json`:

```json
{
  "name": "german-style-guide",
  "owner": { "name": "micschr0" },
  "plugins": [
    {
      "name": "german-style-guide",
      "source": "./",
      "description": "Deutsche Stilregeln für technische Texte — DevOps, Entwickler, Architekten",
      "version": "1.0.0",
      "author": { "name": "micschr0" }
    }
  ]
}
```

- [ ] **Schritt 2: JSON-Syntax prüfen**

```bash
python3 -c "import json; json.load(open('.claude-plugin/marketplace.json')); print('OK')"
```

Erwartete Ausgabe: `OK`

- [ ] **Schritt 3: Committen**

```bash
git add .claude-plugin/marketplace.json
git commit -m "feat: add marketplace.json for self-hosted plugin marketplace"
```

---

### Task 3: Skill-Dateien in Unterverzeichnis verschieben

**Files:**
- Create: `skills/german-style-guide/` (Verzeichnis)
- Move: `SKILL.md` → `skills/german-style-guide/SKILL.md`
- Move: `referenz.md` → `skills/german-style-guide/referenz.md`

- [ ] **Schritt 1: Verzeichnis erstellen und Dateien mit git mv verschieben**

```bash
mkdir -p skills/german-style-guide
git mv SKILL.md skills/german-style-guide/SKILL.md
git mv referenz.md skills/german-style-guide/referenz.md
```

- [ ] **Schritt 2: Dateien am neuen Ort prüfen**

```bash
ls skills/german-style-guide/
```

Erwartete Ausgabe:
```
referenz.md
SKILL.md
```

- [ ] **Schritt 3: Committen**

```bash
git add skills/
git commit -m "refactor: move skill files to skills/german-style-guide/ subdirectory"
```

---

### Task 4: README.md Installationsabschnitt aktualisieren

**Files:**
- Modify: `README.md`

- [ ] **Schritt 1: Installationsabschnitt ersetzen**

Den kompletten `## Installation`-Block in `README.md` (von `## Installation` bis zur Zeile `Claude aktiviert den Skill automatisch beim Schreiben...`) mit folgendem ersetzen:

```markdown
## Installation

In Claude Code:

```
/plugin marketplace add micschr0/german-style-guide
/plugin install german-style-guide@german-style-guide
```

Claude Code lädt den Skill automatisch — kein Neustart nötig.
```

- [ ] **Schritt 2: Prüfen, dass der alte manuelle Installationstext weg ist**

```bash
grep -n "mkdir -p ~/.claude" README.md
```

Erwartete Ausgabe: keine Ausgabe (Zeile nicht mehr vorhanden)

- [ ] **Schritt 3: Committen**

```bash
git add README.md
git commit -m "docs: update installation instructions to use plugin marketplace"
```

---

## Abschluss-Check

Nach allen Tasks:

```bash
git log --oneline -5
```

Erwartete Ausgabe (4 neue Commits seit dem letzten Stand):
```
<sha> docs: update installation instructions to use plugin marketplace
<sha> refactor: move skill files to skills/german-style-guide/ subdirectory
<sha> feat: add marketplace.json for self-hosted plugin marketplace
<sha> feat: add plugin.json for Claude Code plugin system
```

```bash
find .claude-plugin skills -type f
```

Erwartete Ausgabe:
```
.claude-plugin/marketplace.json
.claude-plugin/plugin.json
skills/german-style-guide/SKILL.md
skills/german-style-guide/referenz.md
```
