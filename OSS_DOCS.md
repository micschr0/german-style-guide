# OSS Docs — Aufbereitung für die öffentliche Veröffentlichung

Stand dieser Pass: Doku und Metadaten. Kein CI, kein Refactor des Skill-Inhalts.

## Was dieser Pass geändert hat

| Datei | Aktion |
|-------|--------|
| `README.md` | überarbeitet: Schnellstart, "Lokal prüfen", Mitwirken, weitere Doku; Regelzählung korrigiert |
| `CONTRIBUTING.md` | neu: Beitragsarten, Regelschema, Commit-Konventionen, PR-Weg |
| `SECURITY.md` | neu: Meldeweg, unterstützte Versionen, was als Problem zählt |
| `CHANGELOG.md` | neu: Keep-a-Changelog-Skelett mit [Unveröffentlicht] und [1.0.0] |
| `CITATION.cff` | neu: Software-Zitation (Quellen, Lizenz, Version) |
| `docs/FAQ.md` | neu: häufige Fragen zu Nutzung, Modi, Beiträgen |

## README-Checkliste

- [x] Was das Projekt tut (erster Satz)
- [x] Schnellstart (Installation in Claude Code)
- [x] Lokale Verifikation (Evals, manuell)
- [x] Einstieg zum Mitwirken (Verweis auf CONTRIBUTING.md)
- [x] Wo die tiefere Doku liegt (referenz.md, docs/, CHANGELOG, SECURITY)
- [x] Lizenz genannt
- [n/a] Zitation/Reproduktion von Ergebnissen — kein Paper, kein Datensatz

## Architektur-Notiz

Das Repo ist ein Claude-Code-Plugin ohne Programmiersprachen-Stack. Reine Inhalts- und Metadaten-Dateien.

```
.claude-plugin/
  plugin.json        Plugin-Manifest (Name, Version, Skill-Pfad)
  marketplace.json   Marketplace-Eintrag
skills/german-style-guide/
  SKILL.md           Einstieg: Modi, 6 Prinzipien, wann referenz.md laden
  referenz.md        Vollständige Regeln mit Beispielen (Quelle der Wahrheit)
evals/
  evals.json         6 Testfälle mit Assertions
docs/
  FAQ.md             Häufige Fragen
  superpowers/       Plan und Design der Marketplace-Veröffentlichung
```

Kontrollfluss: Claude Code lädt `SKILL.md` bei deutschem Text. `SKILL.md` lädt `referenz.md` nur bei aktivem Lektorat oder mehr als drei gleichzeitigen Regeln.

## Lizenz, Zitation, Reproduzierbarkeit

- **Lizenz:** MIT, bereits vorhanden (`LICENSE`). Keine Änderung nötig.
- **Zitation:** `CITATION.cff` neu hinzugefügt. Datum offen, siehe unten.
- **Reproduzierbarkeit:** Keine externen Daten oder Modelle. Die Evals sind selbsttragend; sie laufen gegen den installierten Skill.

## Offene Maintainer-Entscheidungen (Release-Blocker prüfen)

1. **Lücke in der Regelnummerierung.** Es gibt 70 Regeln, nummeriert bis R76. **R65–R70 fehlen.** Die Überschrift "Denglisch-Verbfallen (R61–R70)" in `referenz.md` und die alte README behaupteten 76 Regeln. Entscheide:
   - R71–R76 zu R65–R70 umnummerieren (durchgehende Folge), **oder**
   - die fehlenden Regeln R65–R70 ergänzen, **oder**
   - die Lücke bewusst dokumentieren.
   Bis dahin nennt die README nur Kategorie-Zählungen, nicht die Rxx-Spannen.
2. **`SKILL.md` veraltet.** Der Inline-Auszug nennt "~60 Regeln (R1–R60)" und ordnet P5/P6 falsch (R26–R30 statt R28–R32). Die Quelle der Wahrheit ist `referenz.md`. `SKILL.md` an die echte Struktur angleichen. (Bewusst nicht in diesem Doku-Pass geändert — Produktinhalt.)
3. **Sicherheitskontakt.** `SECURITY.md` nennt `micschr0@mailbox.org` als Platzhalter. Bestätigen oder ersetzen; Private Vulnerability Reporting im Repo aktivieren.
4. **Release-Datum.** `CHANGELOG.md` und `CITATION.cff` enthalten TODO-Marker für das 1.0.0-Datum. Beim Taggen eintragen.

## Bewusst zurückgestellt

- **CI** — gewünschter Scope war nur Doku. Sinnvoll wäre später ein Markdown-Lint und eine JSON-Schema-Prüfung für `evals.json`.
- **Automatischer Eval-Runner** — die Evals laufen aktuell manuell.
- **CODE_OF_CONDUCT.md** — optional; bei wachsender Beteiligung nachrüsten.
