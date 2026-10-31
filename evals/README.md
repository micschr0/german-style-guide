# Verhalten und Nutzen prüfen

Die Suite für `klartext` beschreibt 51 Entwicklungsfälle zu Sprache und Informationsgestaltung:
klare Formulierungen, passende Informationsauswahl und den Erhalt wichtiger Inhalte.
Die Fälle sind Entwicklungsmaterial und enthalten keine gemessenen Modellresultate.

## Lokal prüfen

Mit Python 3.9 oder neuer:

```bash
python3 evals/validate.py
python3 -m unittest discover -s evals -p 'test_*.py'
```

Der Validator prüft Schema, Rubrik, IDs, Textfelder, Fallgruppen, Folgerunden,
Fixturepfade, Langtextumfang und R1–R76 über alle Themenreferenzen hinweg.
Lokale Markdown-Links samt Überschriften, Plugin-Namen und -Pfade sowie die
20 aufklappbaren README-Beispiele werden ebenfalls geprüft. Zu den sieben
bisherigen Negativtests für Fallgruppen und Gesprächsrunden kommen sieben Tests
für fehlende Themen, doppelte Regeln, verlorene Ausnahmen, ungültige Regelverweise,
defekte Direktlinks, falsch zugeordnete Regeln und alte Plugin-Pfade hinzu (insgesamt 14).
Diese Checks führen keine Modelle aus und messen keine kognitive Belastung.

## Fallgruppen

| Gruppe | Fälle | Zweck |
|---|---|---|
| Erledigung | 44 | Fertige Texte und Antworten, Informationsauswahl, Inhaltstreue, ausführbare Anleitungen. |
| Lernen | 4 | Passende Erklärungstiefe, durchgearbeitete Beispiele, eigene Lösungsversuche. |
| Prozess | 3 | Gewünschte Regelreferenz sowie Zustimmung und Ablehnung der Stilübernahme über mehrere Runden. |

Die drei Fallgruppen müssen alle Fälle genau einmal abdecken.
`primary_quality_case_ids` enthält Erledigungs- und Lernfälle. Die Prozessfälle
stehen getrennt in `process_case_ids`: Fall 23 kann den Guide durch Regelnummern
verraten; Fälle 33 und 34 prüfen den Gesprächsablauf einschließlich Stilfrage.

## Fälle ausführen

1. Beginne pro Fall einen unabhängigen Kontext.
2. Übergib den unveränderten `prompt` und alle unter `files` genannten Inhalte.
   Fixturepfade gelten relativ zu `evals/`.
3. Falls `follow_up_turns` vorliegt, warte jeweils die Modellantwort ab und sende
   die Folgeprompts nacheinander im selben Kontext. Schiebe keine zusätzlichen
   Hinweise oder Korrekturen ein.

Die Erwartungen in `output_contract` dienen der Bewertung und werden nicht an
das erzeugende Modell übergeben. Zu erhaltende Inhalte beziehen sich jeweils auf
die bearbeitete Nachricht. Ein Kontextneustart zwischen Folgerunden würde die
Entscheidung über Stilübernahme verlieren.

Einige Regressionsaufträge geben den neutralen Stil ausdrücklich vor, damit sie
gezielt Inhaltstreue prüfen. Dieselben Vorgaben gelten für jede Bedingung.

`invariants` beschreibt zu erhaltende Inhalte, `authorized_changes` erlaubte
Änderungen und `hard_failures` konkrete Fehler. Ein reines Lektorat beauftragt
keine externe Sachprüfung. Neue CLI-Syntax ist in Fall 25 als Entwurf erlaubt;
Fall 2 verbietet erfundene bestehende Syntax.

## Antworten beurteilen

Die gemeinsame Rubrik bewertet Inhaltstreue, Auftragserfüllung, Verständlichkeit,
Zielgruppenpassung und angemessenen Leseaufwand mit 0–4 Punkten. 0, 2 und 4 sind
verankert; 1 und 3 sind Zwischenstufen. Harte Fehler mit Belegen separat erfassen.
Stilpunkte gleichen einen wichtigen Inhaltsverlust oder eine erfundene Tatsache
nicht aus. Ausgabeformat und Prozessverhalten getrennt prüfen.

Eine Tabelle, ein kurzer Satz oder eine Regelnummer bringt keinen eigenen
Qualitätsbonus. Eine längere Erklärung kann einen Lernauftrag besser erfüllen.
Die Rubrik beschreibt redaktionelle Erwartungen. Die Bewertung durch ein
KI-Modell ersetzt keine Messung des empfundenen Aufwands menschlicher Leser.

Die Fälle 49–51 prüfen Orientierung beim Überfliegen, Bedingungen am
Handlungsschritt und eine kurze Antwort ohne Formatierungsballast. Beurteile, ob
Überschriften und Hervorhebungen zusammen einen sachlich richtigen Eindruck
ergeben. Eine erhaltene Bedingung im Fließtext gleicht eine irreführende
Überschrift nicht aus. Die Fälle prüfen keine gemessene Wirkung auf menschliche Leser.

## Anwendung eines geänderten Skills prüfen

Nutze vor der Auslieferung ein konkretes Anwendungsszenario mit einer
Kontrollbedingung ohne Guide. Wiederhole die Varianten in unabhängigen Kontexten,
lies die tatsächlichen Ausgaben und dokumentiere Abweichungen vom vereinbarten
Verhalten. Nutze bei Formulierungstests mindestens fünf Wiederholungen pro Variante.
Verändere nach der Kontrolle nur beobachtete Lücken und prüfe geänderte Vorgaben erneut.

Eine Stilfrage, die nur der Guide verlangt, ist eine konfigurierte Verhaltensregel.
Ihre Befolgung beweist keinen allgemeinen Qualitätsvorteil gegenüber der Kontrolle.
Ein Anwendungstest mit manuell geladenen Regeldateien prüft weder die native
Skill-Auswahl noch das Nachladen durch einen bestimmten Host.

Für Änderungen der Ladestruktur zusätzlich vorherigen und neuen Skill vergleichen.
Je Antwort die tatsächlich geladenen Dateien, Leseaufrufe und erneut eingebundene
Inhalte festhalten. Ergebnisse mit Modellversion, Datum, vollständigen Ausgaben
und Prüfgrenzen im jeweiligen Pull Request dokumentieren. Manuell vorab geladene
Dateien und die automatische Auswahl durch den Host getrennt ausweisen.

## Tokenumfang und Nachladen prüfen

Vergleiche Ausgangsstand und Änderung mit derselben Tokenizer-Version und demselben
Encoding. Eine Dateimessung mit `tiktoken==0.14.0` und `o200k_base` ist für Claude
eine Näherung, keine Messung mit dessen Tokenizer. Installiere den optionalen
Zähler in einer separaten Python-Umgebung; die Strukturprüfungen benötigen ihn nicht.

Vom Repository-Root aus, mit verfügbarem Encoding oder vorhandenem Cache:

```python
from pathlib import Path
import tiktoken

encoding = tiktoken.get_encoding("o200k_base")
total = 0
for path in sorted(Path("skills/klartext").glob("*.md")):
    count = len(encoding.encode(path.read_bytes().decode("utf-8")))
    total += count
    print(path.name, count)
print("Gesamt", total)
```

Führe dieselbe Messung am gesicherten Ausgangsstand aus. Halte die verglichenen
Commits, genauen Dateien oder Abschnitte sowie Summen für Kurzantwort,
Sprachkorrektur, bedingte Anleitung, Langtext und Lernfrage fest. Zähle Markdown,
Links und Metadaten mit. Vergleiche auch die Volllektüre und bereits mögliche
Abschnittsreads; eine kleinere Kerndatei allein belegt keine Gesamtersparnis.

Erfasse bei Hosttests zusätzlich Leseaufrufe, Tool-Hüllen, tatsächlich übergebene
Eingabetokens und Cacheanteile, soweit der Host diese ausweist. Mehrere Referenzen,
ein zusätzlicher Indexaufruf und wiederholt übergebener Kontext können die
Ersparnis aufheben. Dokumentiere, ob Dateien gemeinsam oder einzeln gelesen
wurden und welche Inhalte bei Folgerunden im Kontext blieben.

Dateiumfang, tatsächlicher Hostverbrauch und Antwortqualität sind getrennte
Ergebnisse. Berichte fehlende Modell- oder Hosttests ausdrücklich. Eine
redaktionelle Durchsicht oder ein grüner Strukturtest belegt keine
Verhaltenstreue und keinen gemessenen Nutzen.

## Vergleich vorbereiten

Vergleiche mindestens drei Bedingungen: nur Aufgabe, kurzer Stilprompt und
aktueller Skill. Eine mögliche Kurzvorgabe lautet:

> Antworte neutral und prägnant. Richte den Inhalt auf Ziel und Vorwissen aus.
> Erhalte wichtige Inhalte und liefere die angeforderte Antwort direkt.

Halte Modellversion, Datum, Einstellungen, vollständige Instruktionen und geladene
Dateien fest. Verwende gleiche Aufgaben, unabhängige Kontexte und dieselbe
Kontextposition der zusätzlichen Vorgaben. Weise vollständig geladene Referenzen
als solche aus; damit wird nicht das bedarfsabhängige Nachladen geprüft.
Vergleiche Antworten möglichst blind und lasse Gleichstand zu.

Ergänze vorab zurückgehaltene Aufgaben und passende Leser. Die öffentlichen
Entwicklungsfälle sind kein Holdout; Wiederholungen zählen nicht als zusätzliche
Aufgaben. Prüfe automatische Aktivierung, Nachladen, Gesprächspersistenz und
Kontextwechsel in einem getrennten Hosttest. Die Suite gibt keinen Gewinner vor.

## Offenes Abschluss-To-do

Den tatsächlichen Nutzen für Erledigungs- und Lernaufgaben getrennt prüfen:

- **Auffindbarkeit:** Finden Leser Termin, Voraussetzung und Unsicherheit korrekt?
- **Verständnis:** Können Leser die entscheidende Aussage oder den Zusammenhang korrekt wiedergeben?
- **Korrekte Ausführung:** Können sie die Aufgabe mit erhaltenen Voraussetzungen und Bedingungen lösen?
- **Empfundener Aufwand:** Wie bewerten die Leser den Aufwand auf einer vorab festgelegten Skala?
- **Nacharbeit:** Welche Korrekturen sind vor der Verwendung nötig?

Zeit bis zur korrekten Antwort, Fehler und empfundenen Aufwand getrennt erfassen.
Für den Formatierungseffekt denselben Inhalt in verschiedenen Darstellungen
vergleichen; Reihenfolge und Textzuordnung ausbalancieren. Der Vergleich ganzer
Modellantworten prüft zusätzlich Unterschiede in Sprache und Informationsauswahl.
Lesedauer und Textlänge ergänzend erfassen. Für Lernaufgaben kann ein späterer
Transfer- oder Behaltenstest hinzukommen; unmittelbares Verständnis allein belegt
keinen langfristigen Lernerfolg. Die Nutzenprüfung wird mit dieser Änderung
vorbereitet und bleibt offen.
