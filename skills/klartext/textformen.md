# Gliederung und technische Textformen

Es gilt der [Regelkern](SKILL.md). [Geltung und Quellen](referenz.md#geltung-und-quellen).

## Gliederung

### R21: Orientierung früh geben
**Typ:** Stilheuristik.
**Regel/Warum:** Stelle die für den Textzweck wichtigste Information früh bereit.
**Wann nicht:** Chronologie, Argumentation oder Erzählung können eine andere Reihenfolge brauchen.
**Beispiel:** „Das Deployment ist verschoben. Neuer Termin: Donnerstag, 22 Uhr.“ orientiert bei einem Terminupdate sofort.

### R22: Absätze nach inhaltlicher Einheit bilden
**Typ:** Stilheuristik.
**Regel/Warum:** Bündele zusammengehörige Aussagen und trenne neue Schwerpunkte.
**Wann nicht:** Keine allgemeine Mindest- oder Höchstzahl von Sätzen pro Absatz erzwingen.
**Beispiel:** Ein einzelner Satz mit dem neuen Termin kann einen eigenen Absatz bilden.

### R23: Logische Beziehungen sichtbar machen
**Typ:** Stilheuristik.
**Regel/Warum:** Verwende Übergänge für tatsächlich vorhandene Beziehungen; „deshalb“ bedeutet mehr als „danach“.
**Wann nicht:** Bei bloßer zeitlicher Folge kein Kausalwort ergänzen.
**Beispiel:** „Zuerst prüfen wir die Logs. Danach vergleichen wir die Konfiguration“ beschreibt eine Reihenfolge.

### R24: Überschriften für die Orientierung schreiben
**Typ:** Stilheuristik.
**Regel/Warum:** Formuliere Überschriften so konkret, wie Navigation und Inhalt es brauchen.
**Wann nicht:** Standardüberschriften wie Installation oder Konfiguration sind oft ausreichend.
**Beispiel:** „Timeout konfigurieren“ passt zu einer Anleitung für genau diesen Schritt.

### R25: Vergleichbare Listeneinträge parallel formulieren
**Typ:** Stilheuristik.
**Regel/Warum:** Gib gleichartigen Einträgen eine gemeinsame Form, um den Vergleich zu erleichtern.
**Wann nicht:** Unterschiedliche Informationsarten brauchen kein erzwungenes Satzmuster.
**Beispiel:** „Datei anlegen; Parameter konfigurieren; Dienst starten“ ist eine parallele Schrittliste.

### R26: Satzrhythmus dem Textzweck anpassen
**Typ:** Stilheuristik.
**Regel/Warum:** Variiere Satzlängen, wenn der Text dadurch flüssiger wird.
**Wann nicht:** Referenzen und API-Beschreibungen profitieren oft von einheitlichen Mustern.
**Beispiel:** Zwei kurze, parallele Fehlermeldungen brauchen keinen längeren Satz zur Abwechslung.

### R27: Satzzeichen nach Funktion einsetzen
**Typ:** Stilheuristik.
**Regel/Warum:** Nutze Doppelpunkt, Gedankenstrich und Semikolon, um passende Beziehungen sichtbar zu machen.
**Wann nicht:** Satzzeichen nicht nur zur Dekoration ergänzen; ihre grammatische Funktion beachten.
**Beispiel:** „Das Problem: ein fehlender Timeout“ kündigt eine Erläuterung an.
## Technische Textformen

### R48: Technische und zitierte Inhalte schützen
**Typ:** Fachkonvention.
**Regel/Warum:** Ändere Code, Befehle, Bezeichner, Pfade, URLs und direkte Zitate nur im beauftragten Umfang.
**Wann nicht:** Ein ausdrücklicher Auftrag zur Codekorrektur oder Zitatübersetzung erweitert den Umfang.
**Beispiel:** `/etc/app/config.yml` und `MAX_WORKERS` sind keine Nominalstilprobleme.

### R49: Commit-Messages nach Projektkonvention schreiben
**Typ:** Fachkonvention.
**Regel/Warum:** Beschreibe Änderung und bei Bedarf Grund im vereinbarten Format.
**Wann nicht:** Conventional Commits und Imperativ sind keine universellen Sprachvorschriften.
**Beispiel:** Wenn Projektformat und Wert bekannt sind: „fix: Health-Check-Timeout auf 30 s erhöhen“.

### R50: README auf Nutzen und tatsächlichen Einstieg ausrichten
**Typ:** Fachkonvention.
**Regel/Warum:** Erkläre Zweck, Voraussetzungen und einen belegten Einstieg in angemessenem Umfang.
**Wann nicht:** Bei bestehenden Systemen keine Installationsbefehle, Optionen oder unterstützten Versionen erfinden, um eine Vorlage zu füllen. Bei ausdrücklich beauftragtem Entwurf dürfen solche Details als Vorschlag erscheinen, aber nicht als bereits nutzbare Schnittstelle.
**Beispiel:** Beim Dokumentieren eines bestehenden Tools ohne bekannte CLI-Syntax Funktionen beschreiben und die konkrete Befehlsreferenz offenlassen. Bei ausdrücklich beauftragtem CLI-Entwurf dagegen neue Syntax als Vorschlag ausarbeiten.

### R51: Entscheidungen in ADRs auffindbar machen
**Typ:** Fachkonvention.
**Regel/Warum:** Mache Status, Entscheidung, Gründe und Folgen leicht auffindbar; nutze das vereinbarte Template.
**Wann nicht:** Ein vorhandenes Format kann Kontext vor der Entscheidung vorsehen.
**Beispiel:** „Entscheidung: Wir verwenden PostgreSQL“ passt, wenn dies die tatsächliche Entscheidung ist.

### R52: Warnhinweise nach Relevanz gewichten
**Typ:** Stilheuristik.
**Regel/Warum:** Nenne bekannte Folgen rechtzeitig am betroffenen Handlungsschritt.
**Wann nicht:** Eine feste Seitenquote darf notwendige Warnungen nicht unterdrücken.
**Beispiel:** Eine bekannte Löschwirkung unmittelbar vor dem zugehörigen Befehl nennen.

### R53: Versionsbezug aus belegten Angaben nennen
**Typ:** Fachkonvention.
**Regel/Warum:** Nenne bekannte Versionen und Gültigkeitsstände, wenn sie für die Nutzung relevant sind.
**Wann nicht:** Kein Prüfdatum erfinden; das Änderungsdatum eines Wikis ist kein automatischer fachlicher Prüfstand.
**Beispiel:** „Gilt für Version 2.4“ nur schreiben, wenn dieser Geltungsbereich belegt ist.

### R54: Code-Blöcke passend auszeichnen
**Typ:** Fachkonvention.
**Regel/Warum:** Ergänze bei bekannten Sprachen und geeignetem Ausgabeformat eine passende Sprachkennung.
**Wann nicht:** Sprache nicht raten; Blockinhalt und technische Literale im vereinbarten Umfang schützen.
**Beispiel:** Für bekannte Shellbefehle eignet sich die Kennung `bash`.

### R55: Abhängige Schritte geordnet darstellen
**Typ:** Fachkonvention.
**Regel/Warum:** Nummeriere Schritte, wenn ihre Reihenfolge wichtig ist. Nenne Voraussetzungen vor der betroffenen Handlung. Pflichtschritte gehören sichtbar in die Schrittfolge.
**Wann nicht:** Unabhängige Optionen dürfen eine ungeordnete Liste bilden. Gleichzeitig nötige Handlungen müssen als gleichzeitig erkennbar bleiben.
**Beispiel:** „Wenn die Sicherung erfolgreich geprüft ist, starte das Update.“ Eine entsprechende Prüfung darf nicht nur in einem beiläufigen Hinweis stehen.
## Fehlermeldungen

Für alle Muster gilt: Nur bekannte Diagnoseinformationen ausgeben. Unbekannte
Ursachen oder Maßnahmen dürfen fehlen. Eine Vermutung nicht als gesicherte Diagnose
formatieren. Zusätzliche Angaben in Beispielen setzen den jeweils genannten Kontext voraus.

### R56: Bekannten Fehler und bekannte Ursache unterscheiden
**Typ:** Fachkonvention.
**Regel/Warum:** Benenne den bekannten Fehlschlag; ergänze eine Ursache nur bei entsprechender Diagnose.
**Wann nicht:** „Verbindung fehlgeschlagen“ belegt weder Serverausfall noch falsche Zugangsdaten.
**Beispiel:** „Verbindungsfehler aufgetreten.“ → „Verbindung fehlgeschlagen.“ Ohne weitere Diagnose keine Ursache ergänzen.

### R57: Vorhandene Diagnosewerte erhalten
**Typ:** Fachkonvention.
**Regel/Warum:** Nenne bekannte relevante Werte, damit die Meldung bei der Fehlersuche hilft.
**Wann nicht:** Ohne bekannte Dauer kein konkretes Timeout ergänzen.
**Beispiel:** Bei bekanntem Timeout nach 5 s: „Zeitüberschreitung nach 5 s.“

### R58: Begründete nächste Schritte nennen
**Typ:** Fachkonvention.
**Regel/Warum:** Schlage zum bekannten Fehler passende Handlungen vor, wenn der Kontext sie trägt.
**Wann nicht:** Keine systemspezifischen Befehle, Pfade oder destruktiven Maßnahmen aus einer allgemeinen Meldung ableiten.
**Beispiel:** Bei diagnostizierter fehlender Datei: „Konfigurationsdatei fehlt. Prüfe den angegebenen Pfad.“

### R59: Fehlercodes unverändert und nachvollziehbar erklären
**Typ:** Fachkonvention.
**Regel/Warum:** Erhalte den Code exakt und ergänze seine dokumentierte Bedeutung, falls bekannt.
**Wann nicht:** Keine unbelegte numerische Kennung oder Produktdiagnose aus dem Namen ableiten.
**Beispiel:** Bei dokumentierter Bedeutung: „E_CONN_REFUSED: Verbindung abgelehnt.“

### R60: Fehlermeldungen knapp und handlungsnah schreiben
**Typ:** Stilheuristik.
**Regel/Warum:** Formuliere den bekannten Fehlschlag verständlich und mit nötigem Kontext.
**Wann nicht:** Aktive Form verlangt keinen erfundenen Akteur; kurze Fragmente sind möglich.
**Beispiel:** „Es konnte keine Verbindung hergestellt werden.“ → „Verbindung fehlgeschlagen.“
