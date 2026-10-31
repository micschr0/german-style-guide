# Forschungsgrundlage für die Informationsgestaltung von Klartext

Stand: 30. Oktober 2026. Die Recherche bezog sich zunächst auf Commit `f43923b7dd98d7f05615b02735c2b2cf7a255b0b` des Branches `fix/concise-german-style-guide`. Die daraus abgeleiteten Regeln sind inzwischen in Klartext umgesetzt. Dieser Bericht dokumentiert die Belege und ihre Grenzen für die weitere Entwicklung.

## Ergebnis und Reichweite

Gezielte Hervorhebungen, informative Überschriften, sinnvolle Abschnitte und die räumliche Nähe zusammengehöriger Informationen haben eine wissenschaftliche Grundlage. Ihre Wirkung hängt von Aufgabe, Vorwissen und Material ab. Der Skill sollte Auffindbarkeit, korrektes Verständnis und korrekte Ausführung unterstützen. Eine generelle Beschleunigung des Lesens oder eine gemessene Senkung kognitiver Belastung durch diesen Skill ist damit nicht nachgewiesen.

Dies ist eine gezielte Literaturrecherche, keine systematische Übersichtsarbeit. Recherchiert wurde über Crossref, Europe PMC, ERIC, OpenAlex und Verlagsseiten. Die Auswertung umfasst wissenschaftliche Reviews, Metaanalysen, Einzelstudien und ergänzende W3C-Leitlinien. Verfügbare Volltexte und Abstracts werden unten getrennt ausgewiesen. Ein Abstract erlaubt keine vollständige Prüfung von Studiendesign, Verzerrungsrisiko oder Moderatoranalysen. Die Quellen sind über DOI- und Verlagslinks identifizierbar. Lokal abgerufene Quellenkopien und Metadaten lagen während der Recherche unter `/workspace/scratch/reading-research/`; sie sind nicht Bestandteil des Repositories und müssen bei Bedarf erneut abgerufen werden. Einzelne Verlagsvolltexte waren nicht direkt zugänglich.

## Befunde und Konsequenzen

### 1. Gezielte Hervorhebungen können das Lernen aus Text unterstützen

**Quelle:** Ponce, Mayer & Méndez (2022), *Effects of Learner-Generated Highlighting and Instructor-Provided Highlighting on Learning from Text: A Meta-Analysis*. [DOI](https://doi.org/10.1007/s10648-021-09654-1). Verlagsabstract gelesen; Volltext kostenpflichtig.

36 Veröffentlichungen aus den Jahren 1938–2019 ergaben 85 Effektstärken. Für bereits durch die Lehrperson hervorgehobenes wichtiges Material berichtet der Abstract mittlere Effektstärken von jeweils 0,44 für Erinnern und Verstehen. Selbstständiges Markieren verbesserte Erinnern, aber nicht das Verständnis statistisch verlässlich. Diese Unterscheidung ist wichtig: Selbst mit Textmarker zu lernen und von Autoren gesetzte Orientierungssignale zu lesen sind verschiedene Interventionen.

**Konsequenz:** Wichtige Aussagen oder Suchbegriffe gezielt hervorheben. Fettdruck ist eine mögliche Umsetzung im Markdown, aber seine genaue Dosierung in deutschen Chat-Antworten wurde durch diese Recherche nicht bestimmt. 0,44 ist eine standardisierte Effektstärke, keine Verbesserung um 44 Prozent. Die Studie liefert keinen allgemeinen Beleg für eine verringerte kognitive Belastung oder höhere Lesegeschwindigkeit durch Fettdruck.

### 2. Überschriften steuern Aufmerksamkeit und die mentale Textstruktur

**Quellen:**

- Lorch et al. (2001), *Effects of Headings on Text Summarization*. [DOI](https://doi.org/10.1006/ceps.1999.1037), [PubMed](https://pubmed.ncbi.nlm.nih.gov/11273655/). Abstract über Europe PMC gelesen.
- Sanchez, Lorch & Lorch (2001), *Effects of Headings on Text Processing Strategies*. [DOI](https://doi.org/10.1006/ceps.2000.1056), [PubMed](https://pubmed.ncbi.nlm.nih.gov/11414729/). Abstract über Europe PMC gelesen.
- *Effects of headings and familiarity with a text on strategies for searching a text* (2000). [DOI](https://doi.org/10.3758/BF03201256). Verlagsabstract gelesen.

Die Zusammenfassungsstudie zeigt, dass Themen mit Überschriften eher in Zusammenfassungen auftauchten. Wurde nur die Hälfte der Themen mit Überschriften versehen, profitierten diese besonders; nicht markierte Themen tauchten hingegen seltener auf als in Texten ganz ohne Überschriften. Die Verarbeitungsstudie zeigt Vorteile für das Erinnern von Themen und deren Organisation. Die Suchstudie zeigt, dass Überschriften und Vertrautheit beeinflussen, wie Seiten durchsucht werden; daraus folgt kein hier bezifferter allgemeiner Zeitgewinn.

**Konsequenz:** Überschriften sollen Inhalt und Beziehungen zuverlässig abbilden. Wichtige Einschränkungen nicht durch selektive Hervorhebung unsichtbar machen. Die Anweisung „Hebe die wichtigsten Wörter fett hervor“ allein ist unzureichend. Besser: „Prüfe, ob Überschriften und Hervorhebungen zusammen einen sachlich richtigen Eindruck ergeben.“ Dies ist eine redaktionelle Ableitung, keine wörtliche Studienvorgabe.

### 3. Sinnvolle Abschnitte helfen; kürzere Lesezeit ist nicht automatisch besser

**Quelle:** Rey et al. (2019), *A Meta-analysis of the Segmenting Effect*. [DOI](https://doi.org/10.1007/s10648-018-9456-4). Verlagsabstract gelesen.

56 Untersuchungen mit 88 Paarvergleichen zeigen kleine bis mittlere Vorteile für Behalten und Transfer. Die Zusammenfassung berichtet außerdem geringere kognitive Belastung, aber längere Lernzeit. Untersucht wurde die Segmentierung multimedialer Instruktionen, unter anderem in selbstgesteuertem Lerntempo.

**Konsequenz:** Abschnitte nach Sinn und Aufgabe bilden, Anleitungen in nachvollziehbare Schritte zerlegen. Die Übertragung auf statische Textabsätze ist plausibel, aber kein unmittelbarer Beweis, dass mehr Absatzumbrüche in Chat-Antworten dieselbe Wirkung haben. Keine starre Obergrenze für Wörter oder Sätze aus dieser Studie ableiten.

### 4. Zusammengehörige Informationen am benötigten Ort anbieten

**Quelle:** Sweller, van Merriënboer & Paas (2019), *Cognitive Architecture and Instructional Design: 20 Years Later*. [DOI](https://doi.org/10.1007/s10648-019-09465-5). Open-Access-Volltext; insbesondere Split Attention, Redundancy, Expertise Reversal und Belastungsmessung gelesen.

Wenn zwei für das Verständnis notwendige Informationsquellen räumlich oder zeitlich getrennt sind, kann ihre mentale Integration zusätzliche Anforderungen erzeugen. Der Review behandelt auch redundante Informationen und den Einfluss des Vorwissens: Unterstützung, die Einsteigern hilft, kann mit wachsender Expertise unnötig oder störend werden.

**Konsequenz:** Voraussetzungen vor dem betroffenen Schritt nennen; Warnung, Befehl und erforderliche Erklärung zusammenhalten. Grundlagen nach Vorwissen erläutern. Nicht pauschal jede Wiederholung entfernen: Ein notwendiger Rückbezug am Handlungsschritt hat eine Funktion. Die Befunde stammen wesentlich aus Instruktions- und Lernkontexten; die Anwendung auf technische Dokumentation ist eine begründete Übertragung.

### 5. Interessante, aber sachfremde Zusätze können Verständnis beeinträchtigen

**Quellen:**

- Sundararajan & Adesope (2020), *Keep it Coherent: A Meta-Analysis of the Seductive Details Effect*. [DOI](https://doi.org/10.1007/s10648-020-09522-4). Verlagsabstract gelesen.
- Cheng et al. (2026), *Seductive Details, Cognitive Load, and Learning Outcomes: A Multi-level Meta-analysis and MASEM*. [DOI](https://doi.org/10.1007/s10648-025-10099-z). Verlagsabstract gelesen; veröffentlicht am 5. März 2026.

Die neuere Analyse umfasst 50 Studien und 177 Effektstärken. Sie berichtet einen kleinen negativen Gesamteffekt auf Lernergebnisse (g = −0,16), einschließlich Verständnis, Erinnern und Transfer. Effekte hängen unter anderem von Sprache und Lernumgebung ab. Die im Abstract berichtete Mediation über zusätzliche kognitive Belastung ist keine Garantie eines bestimmten Mechanismus in jedem Einzelfall.

**Konsequenz:** Dekorative Abschweifungen, Selbstkommentare und sachfremde Beispiele vermeiden. Ein relevantes Beispiel, eine hilfreiche Analogie oder eine notwendige Begründung ist kein „seductive detail“, nur weil sie den Text verlängert.

### 6. Überfliegen und gründliches Verstehen getrennt behandeln

**Quelle:** Rayner et al. (2016), *So Much to Read, So Little Time: How Do We Read, and Can Speed Reading Help?* [DOI](https://doi.org/10.1177/1529100615623267). Abstract über Crossref gelesen; Verlagsvolltext nicht zugänglich.

Der Review beschreibt einen Zielkonflikt zwischen Geschwindigkeit und Genauigkeit. Überfliegen kann für einen Überblick genügen. Eine Verdopplung oder Verdreifachung der Lesegeschwindigkeit bei unverändert gründlichem Verständnis ist nach dem Review unwahrscheinlich.

**Konsequenz:** Zuerst das Leseziel bestimmen: Information suchen, Entscheidung treffen, Zusammenhang verstehen oder Anleitung ausführen. Ein guter Einstieg kann relevante Stellen auffindbar machen; das ersetzt nicht das Lesen ihrer Bedingungen.

### 7. Keine universelle Schrift- oder Wortmarkierungsregel

**Quellen:**

- Wallace et al. (2022), *Towards Individuated Reading Experiences: Different Fonts Increase Reading Speed for Different Individuals*. [DOI](https://doi.org/10.1145/3502222). Abstract über Crossref gelesen.
- Beelders (2025), *Guiding the Gaze: How Bionic Reading Influences Eye Movements*. [DOI](https://doi.org/10.3390/jemr18050049), [Volltext](https://pmc.ncbi.nlm.nih.gov/articles/PMC12565662/). Open-Access-Volltext, Ergebnisse und Einschränkungen gelesen.
- *No, Bionic Reading does not work* (2024). [DOI](https://doi.org/10.1016/j.actpsy.2024.104304). Abstract über Europe PMC gelesen.

Die Schriftstudie berichtet Unterschiede zwischen individuell schnellen und langsamen Schriften und betont, dass eine Schrift nicht für alle passt. Die berichteten 35 Prozent sind ein Vergleich der schnellsten und langsamsten Schrift innerhalb der Untersuchung, kein garantierter Gewinn durch eine beliebige Schriftumstellung. Die Bionic-Reading-Studien fanden in den untersuchten Bedingungen keinen signifikanten Vorteil des Hervorhebens von Wortanfängen. Die Studie von 2025 nennt Einschränkungen hinsichtlich Stichprobe, Textauswahl und einmaliger Exposition.

**Konsequenz:** Keine pauschale Wortanfangsmarkierung oder angebliche Universalschrift vorschreiben. Leserpräferenzen und Anpassbarkeit unterstützen. Aus einem nicht signifikanten Unterschied folgt kein Nachweis vollständiger Wirkungslosigkeit in allen Populationen und Langzeitanwendungen.

### 8. W3C ergänzt die Studien um konkrete Zugänglichkeitsregeln

**Quellen:** [Making Content Usable for People with Cognitive and Learning Disabilities](https://www.w3.org/TR/coga-usable/), [Understanding Headings and Labels](https://www.w3.org/WAI/WCAG22/Understanding/headings-and-labels.html), [Understanding Text Spacing](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html). Publizierte COGA-Fassung und offizielle W3C-Quelltexte gelesen.

COGA empfiehlt erkennbare Gruppen, beschreibende Überschriften, sichtbare wichtige Informationen, getrennte Handlungsschritte, passende Zusammenfassungen und Leerraum. Diese ergänzenden Empfehlungen sind keine experimentelle Metaanalyse und keine zusätzlichen Pflichtkriterien zur WCAG-Konformität. WCAG 1.4.12 fordert, dass Inhalte bestimmte Änderungen der Textabstände ohne Verlust überstehen; die Prüfwerte sind kein universelles optimales Standardlayout.

**Konsequenz:** Semantische Überschriften, Listen und verständliche Linktexte verwenden. Bedeutung nicht ausschließlich durch Farbe oder visuelle Markierung vermitteln. Abstände und Schriftgestaltung anpassbar halten, soweit das Ausgabeformat und die Anwendung das erlauben.

## Aus der Recherche abgeleitete Gestaltungsempfehlung

Die folgende Synthese bildete die Grundlage für die Ergänzung in [gestaltung.md](../skills/klartext/gestaltung.md). Maßgeblich für das aktuelle Verhalten sind diese Skill-Datei und der [Regelkern](../skills/klartext/SKILL.md):

> **Schnelles Erfassen und genaues Verstehen unterstützen**
>
> Richte die Gestaltung auf das Leseziel aus: Informationen finden, Zusammenhänge verstehen oder eine Handlung ausführen. Bei längeren Texten helfen konkrete Überschriften und erkennbare Inhaltsgruppen. Kurze Antworten brauchen keine zusätzliche Gliederung.
>
> - Stelle das für die Aufgabe wichtigste Ergebnis früh bereit. Nenne entscheidende Bedingungen und Unsicherheiten unmittelbar bei der Aussage.
> - Nutze Überschriften, die den folgenden Inhalt zuverlässig ankündigen. Zusammen sollen sie eine verständliche Übersicht ergeben.
> - Hebe gezielt entscheidende Aussagen, Bedingungen oder Suchbegriffe hervor. Prüfe, ob beim Überfliegen der Hervorhebungen ein falscher Eindruck entstehen könnte.
> - Nutze Aufzählungen für gleichrangige Punkte und nummerierte Listen für abhängig aufeinanderfolgende Schritte. Halte gleichzeitig nötige Handlungen als gleichzeitig erkennbar.
> - Nutze Tabellen, wenn mehrere Optionen anhand gleicher Merkmale verglichen werden. Für lange Erklärungen oder schlecht lesbare breite Tabellen sind Absätze häufig geeigneter.
> - Trenne Sinnabschnitte durch Leerraum. Halte Erläuterungen, Bedingungen und Beispiele bei dem Inhalt, auf den sie sich beziehen.
> - Nutze semantische Überschriften, Listen, beschreibende Links und Codeauszeichnung. Wichtige Bedeutung darf nicht ausschließlich durch Farbe, Symbole oder Fettdruck entstehen.
> - Entferne dekorative Elemente und Wiederholungen ohne erkennbaren Nutzen. Bewahre nötige Begründungen und hilfreiche Rückbezüge.

Dieser Text ist eine Synthese aus Forschung, Zugänglichkeitsleitlinien und redaktioneller Übertragung. Besonders die konkrete Tabellenwahl und Fettdruckdosierung sind hier nicht als isolierte Interventionen für deutsche technische Texte belegt.

Daraus abgeleitete stille Schlussprüfung:

> Sind Kernaussage, wichtige Bedingungen und gegebenenfalls die nächste Handlung leicht auffindbar, ohne dass die Gliederung Zusammenhänge verdeckt?

Nicht ergänzen: feste Fettdruckquoten, Pflichtüberschriften in jeder Antwort, universelle Satzlängengrenzen, künstliche Wortanfangsmarkierung oder unbelegte Aussagen wie „wissenschaftlich erwiesen 30 Prozent leichter lesbar“.

## Evaluation: den Nutzen tatsächlich prüfen

Die vorhandenen Evals prüfen bereits Inhaltstreue und passende Ausgabe. Eval 37 erlaubt bei einem Vergleich Tabelle oder klare Prosa; diese Offenheit sollte bleiben. Die Formatierung selbst ist kein Qualitätsbonus.

Für eine Nutzenprüfung sind fünf Aufgabentypen relevant:

1. Langer Statusbericht: Termin, bestätigten Zustand und unbestätigte Ursache finden.
2. Bedingte Anleitung: Voraussetzungen und Reihenfolge korrekt ausführen.
3. Optionsvergleich: relevante Werte vergleichen und Entscheidung begründen.
4. Kurze direkte Antwort: unnötige Gliederung vermeiden.
5. Auffällige Kernaussage mit entscheidender Einschränkung: beide müssen korrekt erfasst werden.

Vergleiche den bisherigen Skill, den Skill mit Zusatz und eine kurze neutrale Stilvorgabe mit identischen Aufgaben. Dokumentiere Modellversionen und nutze unabhängige Kontexte. Um den reinen Formatierungseffekt zu isolieren, vergleiche zusätzlich denselben Inhalt in verschiedenen Layouts. Vollständige Modellantworten prüfen dagegen den Gesamteffekt einschließlich Informationsauswahl.

Menschliche Leser bearbeiten Such-, Verständnis- und Handlungsaufgaben. Erfasse Zeit bis zur korrekten Antwort, Fehlerquote, Verständnis und subjektiven Aufwand getrennt. Für Aufwand kann eine vorab festgelegte, einheitlich eingesetzte mentale Anstrengungsskala dienen; sie beweist allein nicht die Ursache des Aufwands. Reihenfolge und Textzuordnung ausbalancieren. Wiederholtes Lesen desselben Texts kann Übungseffekte erzeugen. Fachkundige und Einsteiger sowie schmale Bildschirmdarstellungen berücksichtigen.

Kleine formative Lesertests können Probleme aufdecken. Ein verallgemeinerbarer Wirksamkeitsnachweis braucht ein vorab geplantes Design und eine begründete Stichprobengröße. KI-Bewertungen und Schema-Validatoren ersetzen keine Messung menschlicher Leseleistung.

## Umsetzungsstand

Die Gestaltungsregeln sind im Skill implementiert. README und FAQ wurden mit dem Skill überarbeitet; das README enthält 20 weitere aufklappbare Beispiele. Die Suite umfasst 51 Entwicklungsfälle. Die Fälle 49–51 behandeln Orientierung beim Überfliegen, Bedingungen am Handlungsschritt und kurze Antworten ohne unnötige Formatierung. Zur Tokenoptimierung wurden die ursprünglich sieben Validator-Tests um sieben Prüfungen der Referenzaufteilung erweitert. Diese Strukturprüfungen messen weder Modellqualität noch menschliche Leseleistung. Native Vergleiche in Claude Code und Lesertests stehen weiterhin aus.

Hinweise zur Tokenmessung, zum Nachladen und zu Prüfgrenzen stehen in der
[Eval-Anleitung](../evals/README.md#tokenumfang-und-nachladen-prüfen).
