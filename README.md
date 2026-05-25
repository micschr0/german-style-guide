# german-style-guide

Ein Claude Code Skill mit destillierten deutschen Stilregeln für technische Texte — für DevOps, Entwickler und Architekten.

## Was der Skill tut

Der Skill wendet 76 Stilregeln automatisch an, wenn Claude auf Deutsch schreibt oder lektoriert:

- **Schreibmodus:** Regeln still anwenden, kein Kommentar
- **Lektüremodus:** Explizite Anmerkungen mit Regelreferenz (z. B. `[R12] Nominalstil → Verb`)

Die Regeln basieren auf Engel (1911), Schneider, tekom-Leitlinie und dem Hamburger Verständlichkeitsmodell.

## Installation

1. Repository klonen:

   ```bash
   git clone https://github.com/micschr0/german-style-guide.git
   ```

2. Skill-Dateien in den Claude Code Plugins-Pfad kopieren:

   ```bash
   mkdir -p ~/.claude/plugins/german-style-guide/skills/german-style-guide
   cp german-style-guide/SKILL.md ~/.claude/plugins/german-style-guide/skills/german-style-guide/
   cp german-style-guide/referenz.md ~/.claude/plugins/german-style-guide/skills/german-style-guide/
   ```

3. Claude Code neu starten.

Claude aktiviert den Skill automatisch beim Schreiben und Lektorieren auf Deutsch.

## Verwendung

**Schreibmodus** — Claude wendet die Regeln still an:

> Schreib eine kurze E-Mail: Das Deployment heute Nacht ist verschoben.

**Lektüremodus** — Claude kommentiert mit Regelreferenzen:

> Lektoriere diesen Text: [Text einfügen]

## Regeln

`referenz.md` enthält alle 76 Regeln (R1–R76) mit Schema: Regel · Warum · Wann nicht · ❌ → ✓

Kategorien:

| Bereich | Regeln |
|---------|--------|
| P1 Kürze | R1–R5 |
| P2 Einfachheit | R6–R10 |
| P3 Aktivität | R11–R15 |
| P4 Konkretheit | R16–R20 |
| P5 Gliederung | R21–R27 |
| P6 Konsistenz | R28–R32 |
| Grammatik | R33–R47 |
| Technische Texte | R48–R55 |
| Fehlermeldungen | R56–R60 |
| Denglisch-Fallen | R61–R70 |
| Zeitform und Person | R71–R74 |
| Artikel und Komposita | R75–R76 |

## Evals

`evals/evals.json` enthält 6 Testfälle:

| ID | Name |
|----|------|
| 1 | Incident-Report lektorieren |
| 2 | README schreiben |
| 3 | Fehlermeldungen verbessern |
| 4 | Schreibmodus (still) |
| 5 | Lektüremodus bei ambiger Anfrage |
| 6 | Langer Text mit Subagent |

## Lizenz

MIT — siehe [LICENSE](LICENSE)
