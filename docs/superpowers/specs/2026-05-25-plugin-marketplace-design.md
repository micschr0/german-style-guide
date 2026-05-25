# Design: Plugin-Marketplace-Infrastruktur

**Datum:** 2026-05-25  
**Ziel:** Installation von 4 manuellen Schritten auf 2 Befehle reduzieren

## Problem

Die bisherige Installation erfordert:
1. `git clone`
2. `mkdir -p ~/.claude/plugins/german-style-guide/skills/german-style-guide`
3. Zwei `cp`-Befehle
4. Claude Code neu starten

## Lösung

Das Repo bekommt Plugin-Marketplace-Infrastruktur. Nutzer installieren mit:

```
/plugin marketplace add micschr0/german-style-guide
/plugin install german-style-guide@german-style-guide
```

## Neue Verzeichnisstruktur

```
german-style-guide/
├── .claude-plugin/
│   ├── plugin.json
│   └── marketplace.json
├── skills/
│   └── german-style-guide/
│       ├── SKILL.md        (verschoben von root)
│       └── referenz.md     (verschoben von root)
├── evals/
├── README.md
├── LICENSE
└── .gitignore
```

## Dateien

### `.claude-plugin/plugin.json`

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

### `.claude-plugin/marketplace.json`

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

## Änderungen

1. `.claude-plugin/plugin.json` erstellen
2. `.claude-plugin/marketplace.json` erstellen
3. `skills/german-style-guide/` Verzeichnis erstellen
4. `SKILL.md` und `referenz.md` nach `skills/german-style-guide/` verschieben
5. `README.md` Installationsabschnitt aktualisieren (alte Schritte ersetzen)

## Nicht geändert

- Skill-Inhalt (SKILL.md, referenz.md) bleibt unverändert
- Evals bleiben an ihrem Ort
- Keine Änderungen an Lizenz, .gitignore
