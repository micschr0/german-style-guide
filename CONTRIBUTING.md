# Mitwirken

Danke für dein Interesse. Dieses Repo pflegt einen Claude-Code-Skill mit deutschen Stilregeln. Beiträge verbessern Regeln, Beispiele und Testfälle.

## Was du beitragen kannst

- **Neue Regel** — eine Stilregel, die häufige Fehler in deutschen Tech-Texten behebt.
- **Korrektur** — ein falsches Beispiel, ein Tippfehler oder eine unklare Formulierung.
- **Besseres Beispiel** — ein konkreteres Schlecht-→-Gut-Paar für eine bestehende Regel.
- **Testfall** — ein neuer Eval in `evals/evals.json`, der eine Regel absichert.

## Aufbau des Repos

| Pfad | Inhalt |
|------|--------|
| `skills/german-style-guide/SKILL.md` | Einstieg: Modi, Prinzipien, wann die Referenz laden |
| `skills/german-style-guide/referenz.md` | Alle Regeln mit Schema und Beispielen |
| `evals/evals.json` | Testfälle mit Prompt, erwartetem Ergebnis und Assertions |
| `docs/` | Plan und Design der Veröffentlichung |

## Eine Regel hinzufügen

Halte das feste Schema aus `referenz.md` ein:

```markdown
### R<Nummer>: <Kurzer aktiver Titel>
Regel: <ein Satz, was zu tun ist>
Warum: <ein Satz Begründung>
Wann nicht: <Ausnahme, falls es eine gibt>
Schlecht → Gut: <konkretes Beispielpaar>
```

Trag die Regel in die passende Kategorie ein und ordne sie der Nummernfolge zu. Aktualisiere danach:

- die Kategorientabelle in [README.md](README.md),
- den Einstieg in `SKILL.md`, falls die Regel ein Prinzip betrifft,
- einen Eval in `evals/evals.json`, der die Regel prüft.

## Stil deiner Beiträge

Dieses Repo lebt von klarem Deutsch. Wende die eigenen Regeln auf deinen Beitrag an: kurze Sätze, Aktiv, Verben statt Substantivierungen, konkrete Beispiele. Der Skill selbst hilft dir dabei.

## Commits

Nutze Conventional Commits:

- `feat:` — neue Regel oder neues Feature
- `fix:` — Korrektur einer Regel, eines Beispiels oder eines Tippfehlers
- `docs:` — Änderung an README, Referenz oder anderer Doku
- `test:` — Änderung an Evals

Halte Commits klein und auf ein Thema beschränkt.

## Pull Request

1. Forke das Repo und erstelle einen Branch.
2. Nimm deine Änderung vor und prüfe sie gegen die Evals (siehe [README.md](README.md), Abschnitt "Lokal prüfen").
3. Beschreibe im PR, welche Regel du änderst und warum.

Bei größeren Vorschlägen öffne zuerst ein Issue, damit wir die Richtung klären, bevor du Arbeit investierst.
