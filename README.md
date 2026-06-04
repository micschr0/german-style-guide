# german-style-guide

76 deutsche Stilregeln für technische Texte — automatisch angewendet, sobald Claude auf Deutsch schreibt.

Der Skill verbessert deutsche README-Dateien, Commit-Messages, Fehlermeldungen, Incident Reports und technische Doku nach festen Regeln. Beim Schreiben wendet er die Regeln still an. Beim Lektorieren kommentiert er jede Änderung mit Regelreferenz.

## Schnellstart

Installiere den Skill in Claude Code:

```
/plugin marketplace add micschr0/german-style-guide
/plugin install german-style-guide@german-style-guide
```

Claude Code lädt den Skill automatisch — kein Neustart nötig. Schreib danach eine deutsche Anfrage, und die Regeln greifen.

## Die zwei Modi

**Schreibmodus** — der Skill wendet die Regeln still an, ohne Kommentar:

> Schreib eine kurze E-Mail: Das Deployment heute Nacht ist verschoben.

**Lektüremodus** — der Skill kommentiert jede Änderung mit Regelreferenz (z. B. `[R12] Nominalstil → Verb`):

> Lektoriere diesen Text: [Text einfügen]

Der Lektüremodus aktiviert sich, sobald du um Lektorat, Verbesserung oder Kritik bittest.

## Die Regeln

`skills/german-style-guide/referenz.md` enthält alle Regeln mit festem Schema: Regel · Warum · Wann nicht · Schlecht → Gut. Die Regeln stützen sich auf Engel (1911), Schneider, die tekom-Leitlinie und das Hamburger Verständlichkeitsmodell.

| Bereich | Regeln |
|---------|-------:|
| Kürze | 5 |
| Einfachheit | 5 |
| Aktivität | 5 |
| Konkretheit | 5 |
| Gliederung | 7 |
| Konsistenz | 5 |
| Grammatik | 15 |
| Technische Texte | 8 |
| Fehlermeldungen | 5 |
| Denglisch-Fallen | 10 |
| Zeitform und Person | 4 |
| Artikel und Komposita | 2 |

Bei Regelkonflikten gilt die Hierarchie **Verständlichkeit > Kürze > Konsistenz > Stil**.

## Lokal prüfen

`evals/evals.json` enthält sechs Testfälle mit Prompt, erwartetem Ergebnis und prüfbaren Assertions:

| ID | Testfall |
|----|----------|
| 1 | Incident-Report lektorieren |
| 2 | README schreiben |
| 3 | Fehlermeldungen verbessern |
| 4 | Schreibmodus (still) |
| 5 | Lektüremodus bei mehrdeutiger Anfrage |
| 6 | Langer Text mit Subagent |

So prüfst du eine Änderung: Installiere den Skill, gib den Prompt eines Testfalls an Claude, und vergleiche das Ergebnis mit den Assertions. Einen automatischen Runner gibt es noch nicht — die Prüfung läuft manuell.

## Mitwirken

Vorschläge für neue Regeln, Korrekturen und Beispiele sind willkommen. Lies [CONTRIBUTING.md](CONTRIBUTING.md), bevor du eine Änderung einreichst.

## Weitere Doku

- [`skills/german-style-guide/referenz.md`](skills/german-style-guide/referenz.md) — vollständige Regeln mit Beispielen
- [`docs/`](docs/) — Plan und Design der Marketplace-Veröffentlichung
- [CHANGELOG.md](CHANGELOG.md) — Versionshistorie
- [SECURITY.md](SECURITY.md) — Schwachstellen melden

## Lizenz

MIT — siehe [LICENSE](LICENSE).
