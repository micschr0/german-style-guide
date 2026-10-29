# Satzbau, Kürze und Perspektive

Es gilt der [Regelkern](SKILL.md). [Geltung und Quellen](referenz.md#geltung-und-quellen).

## Kürze

### R1: Satzlänge nach Verständlichkeit beurteilen
**Typ:** Stilheuristik.
**Regel/Warum:** Teile einen Satz, wenn Verschachtelung oder mehrere Schwerpunkte das Verstehen erschweren. Eine Wortzahl ist nur ein Prüfanlass.
**Wann nicht:** Ein längerer, gut gegliederter Satz kann klarer sein als mehrere abgehackte Sätze.
**Beispiel:** „Die Konfiguration steht in der `.env`-Datei, die du vor dem Start anlegen musst.“ darf als klarer Satz unverändert bleiben.

### R2: Zusammengehörige Gedanken zusammenhalten
**Typ:** Stilheuristik.
**Regel/Warum:** Gib einem Satz einen erkennbaren Schwerpunkt; trenne unabhängige Aussagen, damit ihre Beziehungen klar bleiben.
**Wann nicht:** Ursache, Bedingung und Folge gehören oft in denselben Satz.
**Beispiel:** „Der Build schlägt fehl, weil das Plugin fehlt.“ kann als klarer kausaler Satz bleiben.

### R3: Nur entbehrliche Wörter streichen
**Typ:** Stilheuristik.
**Regel/Warum:** Streiche Wörter nur, wenn Aussage und vereinbarter Ton erhalten bleiben. Nötiger Kontext darf zusätzlichen Raum beanspruchen.
**Wann nicht:** „Grundsätzlich erlaubt“ ist etwas anderes als „erlaubt“; Höflichkeit kann beabsichtigt sein.
**Beispiel:** „Bitte starte den Dienst erneut.“ darf unverändert bleiben.

### R4: Redundanz und Verstärkung prüfen
**Typ:** Stilheuristik.
**Regel/Warum:** Entferne Wiederholungen und Adjektive nur, wenn sie keine relevante Unterscheidung beitragen.
**Wann nicht:** „Kritischer Fehler“ oder „persönlich anwesend“ kann sachlich wichtig sein.
**Beispiel:** „Eine vollständige, komplette Übersicht“ → „eine vollständige Übersicht“ entfernt eine gleichbedeutende Wiederholung.

### R5: Vage Modewörter mit belegten Angaben klären
**Typ:** Stilheuristik.
**Regel/Warum:** Nenne bekannte Fristen oder konkrete Wirkungen, wenn Leser dadurch handeln können.
**Wann nicht:** Fehlende Fristen und Messwerte nicht erfinden.
**Beispiel:** „Bitte prüfe das zeitnah“ enthält keine konkrete Frist. Ohne weiteren Kontext keine ergänzen; „spätestens bis Freitag“ darf nur übernommen werden, wenn diese Frist im Auftrag steht.
## Einfachheit

### R6: Vertraute, präzise Wörter wählen
**Typ:** Stilheuristik.
**Regel/Warum:** Bevorzuge verständliche Wörter gleicher Bedeutung; Wortlänge allein misst keine Verständlichkeit.
**Wann nicht:** „Implementierungsdetail“ kann genauer sein als „Detail“; Inbetriebnahme kann mehr umfassen als Start.
**Beispiel:** „Die Nutzung des Tools“ ist meist verständlicher als „die Inanspruchnahme des Tools“.

### R7: Schwierige Verschachtelungen auflösen
**Typ:** Stilheuristik.
**Regel/Warum:** Entlaste lange Einschübe, damit zusammengehörige Satzteile erkennbar bleiben.
**Wann nicht:** Kurze Relativsätze können einen Begriff knapp und eindeutig bestimmen.
**Beispiel:** „Der Container, der beim gestrigen Deployment, das um 22 Uhr begann, gestartet wurde, ist abgestürzt.“ → „Der Container, der beim gestrigen Deployment gestartet wurde, ist abgestürzt. Das Deployment begann um 22 Uhr.“ Der identifizierende Bezug bleibt erhalten; ein genauer Startzeitpunkt des Containers wird nicht behauptet.

### R8: Nebensätze nach ihrer Funktion platzieren
**Typ:** Stilheuristik.
**Regel/Warum:** Platziere Bedingungen, Gründe und Erläuterungen so, dass ihr Bezug klar ist. Muss eine Voraussetzung vor einer Handlung bekannt sein, nenne sie zuerst.
**Wann nicht:** Nebensätze müssen nicht grundsätzlich am Satzende stehen.
**Beispiel:** „Wenn der Dienst korrekt konfiguriert ist, startet er automatisch.“ ist ebenso möglich wie die umgekehrte Reihenfolge.

### R9: Anglizismen nach Publikum und Bedeutung wählen
**Typ:** Stilheuristik.
**Regel/Warum:** Nutze etablierte Fachbegriffe und das vereinbarte Glossar; erkläre oder übersetze sie bei Bedarf.
**Wann nicht:** Produktnamen, API-Bezeichner und Zitate bleiben im vereinbarten Bearbeitungsumfang geschützt.
**Beispiel:** „Deployment“ kann intern passen; „Bereitstellung“ kann für ein anderes Publikum dasselbe präzise Konzept benennen.

### R10: Unbekannte Abkürzungen einführen
**Typ:** Stilheuristik.
**Regel/Warum:** Erkläre Abkürzungen, wenn die Zielgruppe sie voraussichtlich nicht kennt.
**Wann nicht:** In einer kurzen Notiz für ein SRE-Team muss „SRE“ nicht ausgeschrieben werden.
**Beispiel:** Für fachfremdes Publikum: „Ursachenanalyse (Root Cause Analysis, RCA)“.
## Handlung und Satzbau

### R11: Aktiv und Passiv nach Informationsbedarf wählen
**Typ:** Stilheuristik.
**Regel/Warum:** Nenne bekannte Akteure, wenn Zuständigkeit wichtig ist. Passiv kann den Vorgang sinnvoll fokussieren.
**Wann nicht:** Keinen Akteur erfinden; „Die Anfrage wird asynchron verarbeitet“ ist klar und korrekt.
**Beispiel:** „Die Prüfung der Konfiguration erfolgt durch das Betriebsteam.“ → „Das Betriebsteam prüft die Konfiguration.“

### R12: Unnötigen Nominalstil auflösen
**Typ:** Stilheuristik.
**Regel/Warum:** Ersetze umständliche Funktionsverbgefüge bedeutungsgleich durch klare Verben.
**Wann nicht:** Fachbegriffe und präzise Abstraktionen wie Verfügbarkeit sind keine Fehler.
**Beispiel:** „Das Team führt eine Prüfung der Konfiguration durch.“ → „Das Team prüft die Konfiguration.“

### R13: Kernaussage syntaktisch hervorheben
**Typ:** Stilheuristik.
**Regel/Warum:** Platziere wichtige Aussagen so, dass Leser Schwerpunkt und Beziehungen erkennen.
**Wann nicht:** Eine vorangestellte Bedingung oder ein Gegensatz kann wesentlich sein.
**Beispiel:** „Obwohl der Dienst läuft, schlägt der Health-Check fehl.“ ist klar und braucht keine automatische Umstellung.

### R14: Zuständigkeiten nur aus dem Kontext benennen
**Typ:** Stilheuristik.
**Regel/Warum:** Ersetze unklare Akteure durch bekannte Personen, Teams oder Systeme, wenn die Aufgabe es braucht.
**Wann nicht:** Unbekannte Verantwortung bleibt unbekannt; generisches „man“ ist möglich.
**Beispiel:** Bei reinem Lektorat bleibt „Das Betriebsteam sollte die Konfiguration prüfen“ eine Empfehlung; „Prüfe die Konfiguration“ ändert Adressat und Verbindlichkeit. Ein ausdrücklicher Auftrag zur stärkeren Verpflichtung erweitert den Bearbeitungsumfang.

### R15: Handlungsschritte direkt formulieren
**Typ:** Fachkonvention.
**Regel/Warum:** Nutze für tatsächliche Schritte eine klare Form, häufig den Imperativ.
**Wann nicht:** Empfehlungen und Möglichkeiten dürfen dadurch nicht zu Pflichten werden.
**Beispiel:** „Führe `npm install` aus“ ist ein Schritt; „Du kannst `npm install` ausführen“ beschreibt eine Möglichkeit.
## Konkretheit und Belege

### R16: Belegte Werte und ihre Genauigkeit erhalten
**Typ:** Stilheuristik.
**Regel/Warum:** Bewahre bekannte Werte, Einheiten, Bereiche und Näherungen, damit keine falsche Präzision entsteht.
**Wann nicht:** Aus „ungefähr zwei Stunden“ wird ohne neue Daten keine exakte Dauer.
**Beispiel:** „Die Behebung dauerte einen Zeitraum von ungefähr zwei Stunden.“ → „Die Behebung dauerte ungefähr zwei Stunden.“

### R17: Beispiele als Beispiele kennzeichnen
**Typ:** Stilheuristik.
**Regel/Warum:** Ergänze Beispiele, wenn Auftrag und Verständlichkeit es rechtfertigen; mache ihren Beispielcharakter sichtbar.
**Wann nicht:** Beim reinen Lektorat keine zusätzlichen Systemdetails als Tatsachen einführen. Ein Beispiellabel macht unbekannte CLI-Syntax eines bestehenden Systems nicht zu dokumentierter Syntax. Beauftragte Schnittstellenentwürfe dürfen dagegen neue Details vorschlagen, wenn ihr Entwurfscharakter klar ist.
**Beispiel:** „Fiktives Beispiel: `DATABASE_URL=postgres://localhost:5432/dev`.“ Nur als Beispiel eines passenden Datenbankformats verwenden.

### R18: Kausalität nur bei belegtem Zusammenhang ausdrücken
**Typ:** Stilheuristik.
**Regel/Warum:** Benenne Ursachen, wenn Ausgangstext oder belegter Kontext sie nennen; ein „weil“ behauptet Kausalität.
**Wann nicht:** „Die Datenbank ist voll. Der Dienst ist nicht erreichbar“ belegt allein keine Ursache.
**Beispiel:** „Der Dienst ist ausgefallen. Laut Diagnose liegt es am vollen Datenbankspeicher.“ → „Laut Diagnose ist der Dienst wegen des vollen Datenbankspeichers ausgefallen.“

### R19: Gewissheitsgrad erhalten
**Typ:** Stilheuristik.
**Regel/Warum:** Beschreibe belegte Fakten direkt; bewahre echte Unsicherheit.
**Wann nicht:** Ein Lektorat macht aus einer Hypothese keinen Befund.
**Beispiel:** „Es könnte sein, dass der Timeout zu niedrig ist.“ → „Der Timeout könnte zu niedrig sein.“

### R20: Abstraktionen bei Bedarf erklären
**Typ:** Stilheuristik.
**Regel/Warum:** Erkläre unklare Abstraktionen anhand bekannter Vorgänge oder gekennzeichneter Beispiele.
**Wann nicht:** Präzise Fachbegriffe wie Latenz müssen nicht bildhaft sein.
**Beispiel:** „Das System verbessert die Antwortzeit von 800 ms auf 200 ms.“ → „Das System senkt die Antwortzeit von 800 ms auf 200 ms.“ Die Werte stehen bereits im Ausgangssatz.
## Zeitform und Perspektive

### R71: Tatsächliches Verhalten direkt beschreiben
**Typ:** Stilheuristik.
**Regel/Warum:** Für belegtes gegenwärtiges Systemverhalten passt oft Präsens im Indikativ.
**Wann nicht:** Planung, Hypothese, fremde Aussage oder vergangene Version brauchen eine andere Darstellung.
**Beispiel:** „Der Dienst gibt bei leerer Datenbank null zurück“ nur schreiben, wenn dieses Verhalten belegt ist.

### R72: Modalität und indirekte Rede erhalten
**Typ:** Sprachnorm und Stilheuristik.
**Regel/Warum:** Wähle Modus und Modalverben nach der Aussage; erhalte Möglichkeiten, Hypothesen und berichtete Aussagen.
**Wann nicht:** Konjunktiv hat mehr Funktionen als einen ausdrücklich genannten Gegenfall; nicht allein aus Stilgründen in Tatsachenindikativ ändern.
**Beispiel:** „Bei geringerer TTL könnte die Last sinken“ bleibt eine Möglichkeit, keine zugesicherte Wirkung.

### R73: Vergangenheitsform nach Textfunktion wählen
**Typ:** Stilheuristik.
**Regel/Warum:** Präteritum und Perfekt sind in technischen Texten möglich; Textfunktion und Zeitbeziehungen entscheiden.
**Wann nicht:** Präteritum ist nicht auf Literatur beschränkt und in Tickets nicht grundsätzlich falsch.
**Beispiel:** „Um 22 Uhr fiel der Dienst aus“ passt zur Incident-Chronologie; „Wir haben den Dienst neu gestartet“ zu einem Statusupdate.

### R74: Perspektive und Zuständigkeit passend wählen
**Typ:** Stilheuristik.
**Regel/Warum:** Nutze Ich, Wir, Teamnamen, Direktanrede oder unpersönliche Form nach Dokumentzweck und ausdrücklich vereinbartem Stil. Sachlich relevante Perspektiven bleiben auch im neutralen Standard erhalten.
**Wann nicht:** Persönliche Formen sind in ADRs, READMEs und Tickets nicht grundsätzlich falsch. Akteure nicht erfinden oder unbemerkt entfernen.
**Beispiel:** „Wir haben PostgreSQL gewählt“ kann eine Entscheidung klar dokumentieren, wenn „wir“ im Kontext eindeutig ist.
## Formulierungen prüfen

Prüfe Wichtigkeitsformeln, Selbstbewertungen und mechanische Übergänge auf ihren
Beitrag zur Aussage. Einleitungen und Fazits dürfen entfallen, wenn sie nur
Bekanntes wiederholen. Erhalte notwendige Begründungen und logische Beziehungen.
Ein einzelnes „außerdem“ oder ein Gedankenstrich ist kein Sprachfehler.

Bei „Es ist wichtig zu betonen, dass die Sicherung vor dem Update erfolgen muss“
genügt „Die Sicherung muss vor dem Update erfolgen“. Die Verbindlichkeit bleibt.
Persönliche Erfahrungen, Quellen und Gewissheit werden nicht für den Stil erfunden.
