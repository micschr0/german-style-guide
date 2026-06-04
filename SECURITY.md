# Sicherheit

Dieser Skill besteht aus Textregeln (Markdown und JSON). Er führt keinen Code aus, öffnet keine Netzverbindungen und verarbeitet keine Geheimnisse. Das Sicherheitsrisiko ist gering. Trotzdem nehmen wir Meldungen ernst.

## Schwachstelle melden

Melde eine Schwachstelle **nicht** über ein öffentliches Issue. Nutze stattdessen einen der folgenden Wege:

- GitHub: "Report a vulnerability" über den Reiter **Security** des Repos (Private Vulnerability Reporting).
- E-Mail: `micschr0@mailbox.org`

Bitte gib an:

- eine Beschreibung des Problems,
- die betroffene Datei oder Regel,
- die Schritte zum Nachstellen,
- die mögliche Auswirkung.

## Was als Problem zählt

- Eine Regel oder ein Beispiel, das zu unsicherem Code oder unsicheren Anleitungen rät.
- Ein Eval-Prompt, der versteckte oder schädliche Anweisungen enthält (Prompt Injection).
- Irreführende Inhalte, die ein Nutzer für eine offizielle Empfehlung halten könnte.

## Unterstützte Versionen

Nur die jeweils neueste veröffentlichte Version erhält Korrekturen.

| Version | Unterstützt |
|---------|-------------|
| 1.0.x | ja |
| < 1.0 | nein |

## Reaktion

Wir bestätigen den Eingang innerhalb weniger Tage und halten dich über den Fortschritt auf dem Laufenden. Nach der Korrektur nennen wir dich auf Wunsch in den Release Notes.
