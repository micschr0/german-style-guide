---
name: skill-library
description: >
  Router für das ECC-Skill-Verzeichnis dieses Repos. Erklärt, welche Skills
  hier standardmäßig laden (DAILY) und welche nur bei Bedarf über die
  Skill-Suche geholt werden (LIBRARY). AKTIVIEREN, wenn unklar ist, ob für eine
  Aufgabe schon ein Skill existiert, oder wenn ein stack-fremder Skill gebraucht
  wird ("gibt es einen Skill für …", "welcher Skill für …"). NICHT aktivieren
  für die eigentliche Schreib-/Lektorierarbeit — dafür greift direkt
  german-style-guide.
---

# Skill-Library (Router)

Dieses Repo ist ein **Plugin-/Content-Projekt** (Markdown + JSON, kein
Programmiersprachen-Stack). Darum lädt nur eine schmale DAILY-Menge automatisch;
der große Rest des ECC-Bestands (~240 Skills) bleibt **erreichbar, ohne zu
laden**.

## DAILY vs. LIBRARY

- **DAILY** — lädt jede Session, weil es zum tatsächlichen Stack dieses Repos
  passt: deutsche Prosa, Skill-Authoring, Evals, Git/GitHub, Planung.
- **LIBRARY** — sinnvoll zu behalten, aber nicht pro Session laden. Über die
  Skill-Suche oder gezielten Aufruf reichbar. **LIBRARY heißt nicht gelöscht.**

## DAILY-Skills (aktiv in diesem Repo)

| Skill | Wofür |
|-------|-------|
| `german-style-guide` | Deutscher Schreibstil — Kern des Repos, Qualitätsmaßstab der Doku |
| `writing-clearly-and-concisely` | Englische Specs/Plans in `docs/superpowers/` |
| `ecc:skill-create` | `skills/german-style-guide/SKILL.md` erzeugen/pflegen |
| `ecc:skill-comply` | Konformität der Skill-Definition prüfen |
| `ecc:eval-harness` | `evals/evals.json` pflegen und ausführen |
| `ecc:git-workflow` | Git, Conventional Commits |
| `ecc:github-ops`, `ecc:pr` | Marketplace-Publishing, PRs |
| `ecc:plan` | Plan-/Spec-getriebene Arbeit in `docs/superpowers/` |

## LIBRARY — nach Bedarf über Skill-Suche holen

Die folgenden Gruppen laden **nicht** automatisch. Bei Bedarf mit den
Trigger-Stichworten suchen.

### Sprach- und Framework-Stacks (~120)
Trigger: `rust`, `go`, `python`, `java`, `cpp`, `swift`, `kotlin`, `react`,
`flutter`, `django`, `laravel`, `spring`, `nextjs`, `vue`, `angular`, `nestjs`,
`fastapi` · plus zugehörige `*-patterns`, `*-testing`, `*-security`.

### Build-Resolver und Test-Runner (~40)
Trigger: `build`, `build-fix`, `*-build`, `*-test`, `*-review` je Sprache.
Hier irrelevant — kein Build-/Test-System im Repo.

### Domänen-Skills (~50)
Trigger: `healthcare`, `finance`, `billing`, `trading`, `network`, `homelab`,
`scientific`, `web3`/`evm`/`defi`, `logistics`, `seo`, `marketing`,
`investor`, `customs`.

### Agent- und Harness-Ops (~20)
Trigger: `autonomous`, `loop`, `gan`, `multi-model`, `council`, `harness`,
`enterprise-agent-ops`, `benchmark`.

### Harness- und Config-Tools (~10)
Trigger: `update-config`, `keybindings`, `claude-md`, `security-scan`,
`skill-health`, `instinct`.

## Wo die vollständigen Definitionen liegen

Alle Skill-Bodies bleiben im installierten ECC-Plugin-Cache und sind über die
normale Skill-Suche auffindbar. Dieser Router **dupliziert keine Skill-Inhalte**
— er sagt nur, was DAILY ist und mit welchen Stichworten der Rest gefunden wird.

## Pflege

Ändert sich der Stack dieses Repos (z. B. echtes Tooling kommt dazu), die
DAILY-Tabelle hier aktualisieren oder `ecc:agent-sort` erneut laufen lassen.
Für Dubletten-/Overlap-Bereinigung im Gesamtbestand: `ecc:skill-stocktake`.
