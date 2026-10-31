# Klartext

**Deutsche Texte verständlich schreiben und gestalten.**

Klartext ist ein Skill für Claude Code. Er hilft beim Schreiben, Überarbeiten und
Erklären: Er ordnet Informationen nach Leserbedarf, formuliert präzise und macht
Wichtiges auffindbar.

## Installieren und nutzen

In Claude Code:

```text
/plugin marketplace add micschr0/german-style-guide
/plugin install klartext@klartext
```

Danach im Chat:

```text
Nutze klartext. Überarbeite die README.md neutral und prägnant.
Bewahre alle fachlichen Inhalte.
```

Du kannst auch neue Texte schreiben, Zusammenhänge erklären oder Entwürfe
beurteilen lassen. **Ton und Umfang bestimmst du.** Bei Textüberarbeitungen fragt
der Skill nach einem offenen Stil, sofern Rückfragen zulässig sind.

## Beispiel

Vorher:

> Die Durchführung des Imports wurde abgebrochen, da in Zeile 18
> die Angabe der Kundennummer fehlt.

Nachher:

> **Import abgebrochen:** In Zeile 18 fehlt die Kundennummer.

Beim Lektorat bleiben fachliche Aussagen, Zahlen, Bedingungen und Unsicherheiten
erhalten. Überschriften und Hervorhebungen helfen bei der Orientierung;
kurze Antworten brauchen keine zusätzliche Gliederung.

## Weitere Beispiele

20 Beispiele zum Aufklappen. Fachliche Angaben und Einschränkungen bleiben in den
Überarbeitungen erhalten.

<details>
<summary>1. Nominalstil durch Verben ersetzen</summary>

**Vorher:** Das Betriebsteam führt eine Prüfung der Konfiguration durch.

**Nachher:** Das Betriebsteam prüft die Konfiguration.

</details>

<details>
<summary>2. Zuständigkeit sichtbar machen</summary>

**Vorher:** Die Freigabe des Releases erfolgt durch die Teamleitung.

**Nachher:** Die Teamleitung gibt das Release frei.

</details>

<details>
<summary>3. Eine Anweisung direkt formulieren</summary>

**Vorher:** Führe vor dem Start eine Überprüfung des verfügbaren Speicherplatzes durch.

**Nachher:** Prüfe vor dem Start den verfügbaren Speicherplatz.

</details>

<details>
<summary>4. Die wichtigste Nachricht voranstellen</summary>

**Vorher:** Weil die Datenmigration noch läuft, haben wir beschlossen, den für heute geplanten Rollout auf Freitag zu verschieben.

**Nachher:** Wir verschieben den heutigen Rollout auf Freitag. Die Datenmigration läuft noch.

</details>

<details>
<summary>5. Eine Schrittfolge gliedern</summary>

**Vorher:** Erstelle zuerst eine Sicherung, installiere danach das Update und prüfe anschließend die Erreichbarkeit des Dienstes.

**Nachher:**

1. Erstelle eine Sicherung.
2. Installiere das Update.
3. Prüfe die Erreichbarkeit des Dienstes.

</details>

<details>
<summary>6. Eine Voraussetzung vor die Handlung stellen</summary>

**Vorher:** Starte die Migration nur dann, wenn die Sicherung erfolgreich geprüft wurde.

**Nachher:** **Nur wenn die Sicherung erfolgreich geprüft wurde**, darfst du die Migration starten.

</details>

<details>
<summary>7. Gleichzeitige Tätigkeiten zusammenhalten</summary>

**Vorher:** Während des Lasttests ist sowohl die Protokollierung als auch die Überwachung der Fehlerrate durchgehend aufrechtzuerhalten.

**Nachher:** Halte während des gesamten Lasttests Protokollierung und Überwachung der Fehlerrate gleichzeitig aktiv.

</details>

<details>
<summary>8. Unsicherheit beim Kürzen erhalten</summary>

**Vorher:** Es könnte sein, dass ein zu niedrig eingestellter Timeout die Ursache des Fehlers ist.

**Nachher:** Ein zu niedriger Timeout könnte den Fehler verursachen.

</details>

<details>
<summary>9. Ungefähre Angaben nicht zu exakten machen</summary>

**Vorher:** Die Wiederherstellung nahm einen Zeitraum von ungefähr zwei Stunden in Anspruch.

**Nachher:** Die Wiederherstellung dauerte ungefähr zwei Stunden.

</details>

<details>
<summary>10. Eine Empfehlung als Empfehlung belassen</summary>

**Vorher:** Es wird empfohlen, vor der Aktualisierung einen Export der Einstellungen vorzunehmen.

**Nachher:** Es empfiehlt sich, die Einstellungen vor der Aktualisierung zu exportieren.

</details>

<details>
<summary>11. Aus einer zeitlichen Folge keine Ursache machen</summary>

**Vorher:** Zunächst wurde das Update installiert. Im Anschluss daran kam es zu einem Ausfall des Dienstes.

**Nachher:** Nach der Installation des Updates fiel der Dienst aus.

Die Reihenfolge bleibt erhalten. Die Fassung behauptet nicht, dass das Update den Ausfall verursacht hat.

</details>

<details>
<summary>12. Technische Bezeichner unverändert lassen</summary>

**Vorher:** Die Funktion `findEntry` führt die Rückgabe von `null` durch, wenn kein Eintrag vorhanden ist.

**Nachher:** Die Funktion `findEntry` gibt `null` zurück, wenn kein Eintrag vorhanden ist.

</details>

<details>
<summary>13. Technische Schreibweisen korrigieren</summary>

**Vorher:** Die API Dokumentation nennt eine Antwortzeit von 250ms.

**Nachher:** Die API-Dokumentation nennt eine Antwortzeit von 250 ms.

</details>

<details>
<summary>14. Eine Fehlermeldung auf den bekannten Befund beschränken</summary>

**Vorher:** Bei dem Versuch, eine Verbindung herzustellen, ist ein Fehler aufgetreten.

**Nachher:** Verbindung fehlgeschlagen.

Ohne weitere Diagnose ergänzt der Skill weder eine Ursache noch einen konkreten Reparaturbefehl.

</details>

<details>
<summary>15. Optionen anhand gleicher Merkmale vergleichen</summary>

**Vorher:** Tarif A bietet 5 GB für 4 Euro im Monat. Tarif B bietet 10 GB für 7 Euro im Monat. Benötigt werden 6 GB, weitere Kriterien spielen keine Rolle.

**Nachher:**

**Tarif B deckt den Bedarf von 6 GB.**

| Tarif | Speicher | Preis pro Monat |
|---|---|---|
| A | 5 GB | 4 Euro |
| B | 10 GB | 7 Euro |

Weitere Kriterien spielen bei dieser Auswahl keine Rolle.

</details>

<details>
<summary>16. Einen Status für das Überfliegen aufbereiten</summary>

**Vorher:** Die Vorbereitung ist abgeschlossen. Als Termin ist Donnerstag um 22 Uhr vorgesehen. Der Rollout darf allerdings erst nach der noch ausstehenden Freigabe beginnen.

**Nachher:**

- **Vorbereitung:** abgeschlossen.
- **Geplanter Termin:** Donnerstag, 22 Uhr.
- **Startbedingung:** Die Freigabe steht noch aus. Erst danach darf der Rollout beginnen.

</details>

<details>
<summary>17. Eine Warnung direkt beim betroffenen Befehl platzieren</summary>

**Vorher:** Führe `cleanup --all` aus. Beachte dabei, dass dieser Befehl sämtliche lokalen Testdaten unwiderruflich löscht.

**Nachher:** **`cleanup --all` löscht alle lokalen Testdaten unwiderruflich.** Führe den Befehl aus.

Der Befehl ist ein fiktives Beispiel. Seine hier beschriebene Wirkung stammt aus dem Ausgangstext.

</details>

<details>
<summary>18. Eine Überschrift konkretisieren</summary>

**Vorher:** Weitere Informationen — Dieser Abschnitt erklärt, wie du den Timeout konfigurierst.

**Nachher:** Timeout konfigurieren

Als Überschrift kündigt die neue Fassung den Inhalt direkt an.

</details>

<details>
<summary>19. Einen verschachtelten Satz entlasten</summary>

**Vorher:** Der Container, der beim gestrigen Deployment, das um 22 Uhr begann, gestartet wurde, ist abgestürzt.

**Nachher:** Der Container, der beim gestrigen Deployment gestartet wurde, ist abgestürzt. Das Deployment begann um 22 Uhr.

Der betroffene Container bleibt eindeutig bezeichnet. Ein genauer Startzeitpunkt des Containers wird nicht ergänzt.

</details>

<details>
<summary>20. Eine klare Formulierung beibehalten</summary>

**Vorher:** Die Anfrage wird asynchron verarbeitet.

**Nachher:** Die Anfrage wird asynchron verarbeitet.

Das Passiv stellt den Vorgang in den Mittelpunkt. Ein klarer Satz braucht keine Änderung.

</details>

## Weiterlesen

- [Sprachreferenz](skills/klartext/referenz.md): Themenzugang zu 76 Regeln mit Beispielen und Ausnahmen.
- [Informationsgestaltung](skills/klartext/gestaltung.md): Aufbau, Formatierung und Forschungsquellen.
- [FAQ](docs/FAQ.md): Aktivierung und Verhalten.
- [Mitwirken](CONTRIBUTING.md): Regeln, Beispiele und Testfälle verbessern.

[Regelkern](skills/klartext/SKILL.md) · [MIT-Lizenz](LICENSE)
