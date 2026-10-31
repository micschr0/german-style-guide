# Zu Klartext beitragen

Beiträge verbessern die Sprache und den Aufbau deutscher technischer Texte.
Hilfreich sind Beispiele für Sprachfehler, umständliche Formulierungen und unklare
Bezüge sowie Aufgaben, bei denen Information fehlt oder beim Kürzen verloren geht.

## Aufbau des Repos

| Pfad | Inhalt |
|---|---|
| `skills/klartext/SKILL.md` | Kurzer Regelkern mit Prioritäten und bedarfsabhängigen Verweisen. |
| `skills/klartext/gestaltung.md` | Informationsauswahl, Aufbau, Formatierung und Erklärungstiefe. |
| `skills/klartext/referenz.md` | Themenindex, Geltung und Sprachquellen. |
| `skills/klartext/satzbau.md` | R1–R20, R71–R74: Kürze, Satzbau, Belege und Perspektive. |
| `skills/klartext/grammatik.md` | R33–R47, R75–R76: Grammatik, Orthografie und Typografie. |
| `skills/klartext/terminologie.md` | R28–R32, R61–R70: Begriffe, Anrede und Fachsprache. |
| `skills/klartext/textformen.md` | R21–R27, R48–R60: Gliederung und technische Textformen. |
| `evals/evals.json` | Erledigungs-, Lern- und Prozessfälle. |

## Eine Leitlinie ändern

Beschreibe den konkreten Leserbedarf und die beabsichtigte Verbesserung.
Prüfe zuerst, ob eine vorhandene Leitlinie genügt. Führe Dopplungen zusammen.
Der Kern enthält häufig benötigte Handlungsregeln und direkte Ladeauslöser.
Stilentscheidung, Inhaltsschutz und Ausgabeauftrag stehen dort einmal.
Umfangreiche Details gehören in eine optionale Themenreferenz. Die `description` nennt
Einsatzanlässe und erkennbare Probleme; sie fasst den Ablauf nicht zusammen.

Beachte die Vorgaben zu Bearbeitungsumfang, Inhaltstreue und Stilentscheidung im
[Regelkern](skills/klartext/SKILL.md). Prüfe Änderungen anhand konkreter
Anwendungsszenarien mit und ohne die geänderte Vorgabe. Halte die Ausgaben und
beobachtete Abweichungen fest; das Vorgehen beschreibt die
[Eval-Anleitung](evals/README.md#anwendung-eines-geänderten-skills-prüfen).
Eine ergänzende Anleitung zur Skill-Erstellung ist
[writing-skills](https://github.com/obra/superpowers/blob/main/skills/writing-skills/SKILL.md).

## Sprachliche Detailregeln pflegen

Erhalte bestehende IDs als Verweisziele. Neue IDs kommen hinter die bisher höchste
Nummer; eine Erweiterung muss mit dem Validator abgestimmt werden.
Das Schema in den Themenreferenzen lautet:

```markdown
### R<Nummer>: <Titel>
**Typ:** Sprachnorm, Fachkonvention oder Stilheuristik.
**Regel/Warum:** Was gilt unter welchen Bedingungen?
**Wann nicht:** Welche Ausnahme oder Grenze ist wichtig?
**Beispiel:** Eine bedeutungswahrende Fassung oder ein zulässiger Gegenfall.
```

Belege normative Behauptungen mit einer überprüfbaren Quelle. Eine fremde
Schreibheuristik ist keine allgemeine deutsche Sprachregel.

## Entwicklungsfälle ergänzen

Nutze `evals/evals.json`. Gib eine echte Aufgabe, Ausgabeerwartungen, zu erhaltende
Inhalte, erlaubte Änderungen und konkrete harte Fehler an. Ordne den Fall einer
Erledigungs-, Lern- oder Prozessgruppe zu. Für Gesprächsabläufe über mehrere
Runden verwende `follow_up_turns` und den Tag `multi_turn`.

Prüfe sprachliche Verbesserungen mit echten Korrekturfällen und passenden
Gegenfällen. Zulässiges Passiv, etablierte Fachbegriffe und geschützte Inhalte
dürfen unverändert bleiben. Die bloße Zahl der vorgenommenen Änderungen ist kein Ziel.

## Prüfen und einreichen

Mit Python 3.9 oder neuer:

```bash
python3 evals/validate.py
python3 -m unittest discover -s evals -p 'test_*.py'
git diff --check
```

Die Checks prüfen Struktur, Fallgruppen, Fixtures und Regelverweise; sie führen
keine Modelle aus. Sie prüfen auch lokale Markdown-Links samt Überschriften,
Plugin-Pfade und die 20 aufklappbaren Beispiele. Regel-IDs werden über alle
Skill-Dateien hinweg geprüft, einschließlich Ausnahmen und Beispielschema.

Bei Änderungen an der Ladestruktur mit demselben Tokenizer messen und die
zusätzlichen Dateizugriffe berücksichtigen; siehe
[Messhinweise](evals/README.md#tokenumfang-und-nachladen-prüfen).

Erstelle einen Branch und beschreibe im Pull Request das konkrete Problem,
das neue Verhalten und die Prüfung. Nutze Conventional Commits, etwa `feat:`,
`fix:`, `docs:` oder `test:`. Aktualisiere betroffene Beispiele und Dokumentation.

## Entwicklungsnotizen

- [Forschung zu Lesbarkeit und Informationsgestaltung](docs/forschung-lesbarkeit.md): Belege und Grenzen der Gestaltungsregeln.
