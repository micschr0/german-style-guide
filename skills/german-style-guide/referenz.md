# Deutsche Stilregeln – Vollständige Referenz

Regelschema: **Regel** · **Warum** · **Wann nicht** · ❌ → ✓

---

## ⚠ Häufige Claude-Fehler — zuerst lesen

Diese Fehler passieren beim automatischen Lektorat am häufigsten:

**1. Erlaubtes Passiv fälschlich als Fehler markieren**
Passiv ist korrekt wenn das Objekt wichtiger ist als das Subjekt.
✓ "Die Anfrage wird asynchron verarbeitet." — kein Fehler, Subjekt irrelevant.
✓ "Der Container wird bei jedem Start neu erstellt." — Prozess im Vordergrund.
Passiv ist falsch wenn: "von wem?" fehlt und es relevant wäre.

**2. Anglizismen unnötig ersetzen**
Eingeführte Fachbegriffe nicht ersetzen: Deploy, Container, Pipeline, Branch, Merge,
Commit, Release, Service, Stack, Backend, Frontend, Cache, Token, Request, Response.
❌ "Bereitstellung" für "Deployment" in Tech-Kontext — falscher Ersatz.

**3. Sätze zu aggressiv kürzen**
Kürze > 25W ist das Ziel. Nicht jeden Satz auf 10W erzwingen.
Zusammenhang geht vor Kürze. Verständlichkeit > Kürze (Prioritätshierarchie).

**4. Parallelismus brechen beim Umschreiben**
Wenn eine Liste parallel ist, beim Umschreiben die Form beibehalten.

**5. Markdown-Inhalt stilistisch bewerten**
Code-Blöcke, URLs, Variablennamen, Pfade nicht als Stilproblem markieren.
`/etc/app/config.yml` ist kein langer Ausdruck — es ist ein Pfad.

---

> Gutes Deutsch versteht der Leser beim ersten Lesen — nicht der Schreiber beim ersten Schreiben.

## Regelkonflikte: Prioritätshierarchie

Bei Widerspruch zwischen Regeln gilt:
**Verständlichkeit > Kürze > Konsistenz > Stil**

Konkrete Konfliktbeispiele:

Kürze vs. Verständlichkeit:
❌ "Timeout fix nötig." (zu kurz, unklar)
✓ "Der Timeout muss auf 30 s erhöht werden." (klar, 9 Wörter — gut)

Kürze vs. Parallelismus:
❌ Parallelstruktur brechen um 2 Wörter zu sparen → nicht tun
✓ Parallelstruktur beibehalten auch wenn Satz 27 Wörter hat

Konsistenz vs. Klarheit:
✓ Einmal gewählter Begriff kann gewechselt werden wenn der neue klarer ist
— aber dann im ganzen Dokument wechseln.

---

## Erkennungsmuster für häufige Probleme

Nutze diese Muster zum schnellen Erkennen — nicht zum Suchen/Ersetzen ohne Kontext.

**Nominalstil erkennen:**
Muster: "Die [Substantiv-ung/-keit] von X erfolgt durch Y" → fast immer auflösbar.
Trigger-Wörter: erfolgt, findet statt, wird durchgeführt, kommt zur Anwendung,
steht zur Verfügung, findet Berücksichtigung, bedarf einer Überprüfung.

**Passiv erkennen:**
Muster: wird/wurde/werden + Partizip II (z.B. "wird geprüft", "wurde behoben").
Erlaubt wenn: kein sinnvolles Subjekt existiert oder Objekt im Fokus steht.

**Füllwörter erkennen:**
Streichen und prüfen ob Bedeutung sich ändert: eigentlich, grundsätzlich,
natürlich, selbstverständlich, gewissermaßen, sozusagen, quasi, irgendwie,
durchaus, letztendlich, bekanntlich, im Grunde genommen.

**Schachtelsatz erkennen:**
Mehr als eine Ebene Komma-Einschübe. Mehr als zwei "der/die/das/welche"-Relativsätze.
Satz lässt sich nicht laut lesen ohne Atemlosigkeit.

**Vage Formulierungen erkennen:**
Trigger: unter Umständen, möglicherweise, gewisse, einige, mehrere, bald,
zeitnah, in absehbarer Zeit, entsprechend, adäquat, optimal.

---

## P1 · Kürze

### R1: Sätze kurz halten
Ø 15 Wörter, max. 25. Warum: Lange Sätze = mehrfaches Lesen nötig.
Wann nicht: Parallelstrukturen dürfen länger sein.
❌ "Da die Konfiguration der Umgebungsvariablen, die für den korrekten Betrieb erforderlich sind, in der `.env`-Datei erfolgt, muss diese vor dem Start angelegt werden."
✓ "Die Konfiguration erfolgt in der `.env`-Datei. Lege sie vor dem Start an."

### R2: Ein Gedanke pro Satz
Zwei Ideen = zwei Sätze. Warum: Mehrere Ideen erzwingen komplexe Syntax.
Wann nicht: Enge kausale Zusammenhänge mit Komma OK.
❌ "Der Build schlägt fehl, weil die Gradle-Version inkompatibel ist, und außerdem fehlt `kotlin-kapt`."
✓ "Der Build schlägt fehl. Ursache 1: inkompatible Gradle-Version. Ursache 2: fehlendes Plugin `kotlin-kapt`."

### R3: Füllwörter streichen
Wort streichen, Bedeutung prüfen — ändert sich nichts → streichen.
Wann nicht: Direkte Rede, Zitate.
Füllwörter: eigentlich→, grundsätzlich→, natürlich→, selbstverständlich→,
gewissermaßen→, sozusagen→, quasi→, irgendwie→konkretisieren, durchaus→,
letztendlich→, bekanntlich→, im Grunde genommen→.

### R4: Pleonasmen und Schmuck-Adjektive
Zwei Wörter mit gleicher Bedeutung — eines streichen.
weißer Schimmel→Schimmel, vorausplanen→planen, neu renovieren→renovieren,
persönlich anwesend→anwesend, kurz zusammenfassen→zusammenfassen,
rückwirkend im Nachhinein→rückwirkend, heiß erhitzen→erhitzen.

**(B) Schmuck-Adjektive, Edelfüllsel, Absoluta.** Adjektive nur, wenn sie unterscheiden (»das blaue Kleid«). Streichen, wenn sie nur schmücken — Test: Streiche das Adjektiv. Ändert sich der Informationsgehalt? Nein → streichen.

- **Schmuck-Adjektive:** intensiv→, tiefgreifend→, bedeutsam→, wesentlich→
- **Edelfüllsel:** riesig→, enorm→, total→, absolut→, extrem→, wirklich→
- **Absoluta:** einzigartig, optimal, perfekt — nicht steigerbar, daher falsch verwendet. Streichen oder umformulieren.

| ❌ | ✓ |
|----|----|
| intensive Bemühungen | Bemühungen |
| sehr große Wellen | haushohe Wellen |
| einzigartiges Erlebnis | besonderes Erlebnis |

Grammatik-Notiz: »in keinster Weise« ist grammatisch falsch → siehe R33–R47.

### R5: Modewörter konkretisieren
Wann nicht: Fachbegriff in seinem Fachkontext (agil im Scrum-Kontext OK).
Test: Passt das Wort in einen Werbeprospekt? → Ersetzen.
nachhaltig→langfristig/dauerhaft, Mehrwert→Vorteil/Einsparung,
zeitnah→bis Freitag/in 24h, Synergien→gemeinsame Ressourcen,
Transparenz schaffen→erklären/offenlegen, ganzheitlich→vollständig,
proaktiv→vorausschauend, Optimierungspotenzial→konkrete Verbesserung benennen,
Paradigmenwechsel→grundlegender Wandel, Disruption→Verdrängung.

---

## P2 · Einfachheit

### R6: Kurze Wörter bevorzugen
Kürzeres Wort wenn gleich präzise. Warum: Kürzer = schneller lesbar.
Wann nicht: Eingeführte Fachbegriffe nicht ersetzen (Dependency Injection bleibt).
Inbetriebnahme→Start, Inanspruchnahme→Nutzung, Schlussfolgerung→Fazit,
Implementierungsdetail→Detail, Konfigurationsparameter→Parameter,
Fehlerbehebungsmaßnahme→Fix, Überprüfungsvorgang→Prüfung,
Benutzeroberfläche→UI/Oberfläche, Instandhaltungsmaßnahme→Wartung.

### R7: Schachtelsätze auflösen
Verschachtelte Nebensätze → separate Sätze. Warum: Satzbaum kostet Kapazität.
Wann nicht: Kurzer Relativsatz der nicht unterbricht ist OK.
❌ "Der Container, der beim letzten Deployment, das gestern Nacht lief, gestartet wurde, ist abgestürzt."
✓ "Der Container ist abgestürzt. Er wurde beim gestrigen Nacht-Deployment gestartet."

**Klemmkonstruktionen** — Einschübe, die zusammengehörende Satzteile trennen:

❌ "Er schlägt, nachdem er die gesamte Akte, die ihm sein Kollege gestern übergeben hatte, gelesen hatte, vor…"
✓ "Er las die Akte. Dann schlug er vor…"

❌ "Die von ihm seit Jahren verfolgte Strategie"
✓ "Die Strategie, die er seit Jahren verfolgte"

### R8: Nebensätze ans Ende
Hauptsatz vor Nebensatz. Einschübe in der Mitte vermeiden.
Wann nicht: Einleitende Bedingung darf voran stehen: "Falls X, dann Y."
❌ "Der Dienst, wenn er korrekt konfiguriert ist, startet automatisch."
✓ "Der Dienst startet automatisch, wenn er korrekt konfiguriert ist."

### R9: Anglizismen gezielt einsetzen
Anglizismus erlaubt wenn: präziser oder eingeführter Fachbegriff.
Mischformen vermeiden: entweder deployen oder bereitstellen — nie beides.
Überflüssig: implementieren→umsetzen (außer Softwarekontext), update→aktualisieren,
meeting→Besprechung, asap→sofort/bis heute, input→Eingabe/Beitrag.
Behalten: Deploy, Container, Pipeline, Branch, Merge, Commit, Stack, Cache.

### R10: Abkürzungen erklären
Beim ersten Auftreten ausschreiben. Format: Ausgeschrieben (ABK).
Wann nicht: z. B., d. h., etc., bzw. — universell bekannt.
❌ "Der SRE hat den RCA abgeschlossen. MTTR: 4h."
✓ "Der Site Reliability Engineer (SRE) hat den Root Cause Analysis (RCA) Bericht abgeschlossen. Mean Time to Recovery (MTTR): 4h."

### R42: Positiv formulieren
Doppelte Verneinungen und unnötige Negationen vermeiden. Warum: Verneinungen zwingen den Leser zum mentalen Rückübersetzen — positiv Formuliertes wird sofort verstanden.
Wann nicht: Ironie und bewusste Untertreibung (Litotes) — »nicht schlecht« als Stilmittel.
❌ "nicht selten" → ✓ "oft"
❌ "nicht unumstritten" → ✓ "umstritten"
❌ "nicht ohne Bedeutung" → ✓ "bedeutsam"
❌ "nicht unerheblich" → ✓ "erheblich"
❌ "Es ist nicht unmöglich, dass der Service startet." → ✓ "Der Service kann starten."

---

## P3 · Aktivität

### R11: Aktiv statt Passiv
Aktiv wenn: "von wem?" fehlt und es relevant wäre. Warum: Aktiv = Verantwortung sichtbar.
**Wann nicht (wichtig):** Objekt wichtiger als Subjekt → Passiv OK.
✓ "Die Anfrage wird asynchron verarbeitet." (Mechanismus irrelevant)
✓ "Der Container wird täglich neu erstellt." (Prozess im Vordergrund)
✓ "Das Log wird für 30 Tage gespeichert." (Ergebnis zählt, nicht wer)
❌→✓: "muss angepasst werden"→"passe an", "Es wurde deployt"→"Das Team hat deployt",
"Der Fehler wurde behoben"→"Lisa hat den Fehler behoben."

### R12: Verben wählen und schärfen
Endungen auf -ung, -keit, -heit, -ierung, -schaft → durch Verben ersetzen.
Warum: Nominalstil (Hauptwortseuche) macht Texte schwer und bürokratisch.
Wann nicht: Abstrakte Konzepte als Substantiv manchmal unvermeidbar:
"Die Verfügbarkeit beträgt 99,9%" — kein Fehler.
Häufigste Muster:
"Die Durchführung der X erfolgt durch"→"Y führt X durch",
"zur Anwendung bringen"→anwenden, "in Betrieb nehmen"→starten,
"Entscheidung treffen"→entscheiden, "zur Verfügung stehen"→verfügbar sein,
"Berücksichtigung finden"→berücksichtigen, "unter Beweis stellen"→beweisen,
"Überprüfung durchführen"→prüfen, "Anpassung vornehmen"→anpassen,
"Erwähnung verdienen"→erwähnenswert sein, "in Frage kommen"→möglich sein,
"Verwendung finden"→verwendet werden/nutzen.

**Streckverben-Blacklist:** durchführen→, erfolgen→, vornehmen→, tätigen→, bewerkstelligen→, bewirken→, erlangen→, erzielen→, in Angriff nehmen→.

**(b) Blasse Verben schärfen.** Ersetze blasse Verben (sein, haben, machen, tun, sagen, gehen) durch präzisere, wenn sie eine spezifische Handlung nur umschreiben. Ein starkes Verb transportiert die Handlung ohne Adjektive.

| Schwach | Stark |
|---------|-------|
| Er betrat den Raum mit Lärm | Er polterte herein |
| Sie sprach laut | Sie rief / schrie / donnerte |
| Das Wasser bewegte sich schnell | Das Wasser schoss / rauschte |

Wann nicht: Wenn das blasse Verb die präziseste Option ist — kein starkes Verb erzwingen.

### R13: Hauptsache in den Hauptsatz
Kernaussage im Hauptsatz, nicht im Nebensatz.
Wann nicht: Einleitende Bedingung im Nebensatz OK ("Wenn X, dann Y").
❌ "Obwohl der Service deployt wurde, schlägt der Health-Check fehl."
✓ "Der Health-Check schlägt fehl — obwohl der Service deployt wurde."

**Satzbau:** Subjekt und Verb so früh wie möglich — SVO-Wortstellung im Hauptsatz anstreben. Lange Attribute nicht vor das Subjekt stellen — sie gehören in einen Relativsatz.

❌ "Der gestern Abend in der Stadt gesehene Mann…"
✓ "Den Mann, den ich gestern sah…"

### R14: Handelnde Person nennen
Wer handelt? Nennen. Warum: "man"/"es" = unklare Zuständigkeit.
Wann nicht: "Das System prüft die Verbindung" — System als Akteur OK.
❌ "Man sollte die `.env`-Datei anlegen, bevor man startet."
✓ "Lege die `.env`-Datei an, bevor du den Service startest."

### R15: Imperativ in Anleitungen
Schritt-für-Schritt → Imperativ. Warum: Direkt, keine Interpretationsspielräume.
Wann nicht: Beschreibende Abschnitte (nicht Handlungsanleitung) → kein Imperativ.
❌ "Zuerst sollte man die Abhängigkeiten installieren. Dann kann der Build gestartet werden."
✓ "1. Installiere: `npm install` 2. Starte: `npm run build`"

---

## P4 · Konkretheit

### R16: Zahlen und Fakten statt vager Beschreibungen
Warum: Vagheit erzwingt Interpretation. Wann nicht: Lieber ehrlich vage als falsch präzise.
"unter Umständen"→konkrete Bedingung, "lange"→"8 Minuten", "zeitnah"→"bis Freitag",
"deutlich langsamer"→"3× langsamer (200ms→600ms)", "oft"→"in 7 von 10 Fällen".

### R17: Beispiele geben
Abstrakt → konkretes Beispiel ergänzen. Wann nicht: Bereits konkretes Konzept.
❌ "Konfiguriere die Umgebungsvariablen entsprechend deiner Umgebung."
✓ "Konfiguriere die Umgebungsvariablen. Beispiel: `DATABASE_URL=postgres://localhost:5432/dev`"

### R18: Ursache und Wirkung explizit machen
Kausalität explizit benennen. Wann nicht: Offensichtliche Kausalität kann implizit.
❌ "Der Service ist nicht verfügbar. Die Datenbank hat keinen Speicher mehr."
✓ "Der Service ist nicht verfügbar, weil der Datenbank der Speicher ausgegangen ist."

### R19: Ist-Zustand beschreiben, nicht Potenzial
Konjunktiv (könnte, würde, möglicherweise) bei Fakten vermeiden.
Wann nicht: Echte Unsicherheiten → Konjunktiv korrekt.
❌ "Es könnte sein, dass der Timeout zu niedrig ist."
✓ "Der Timeout ist zu niedrig: 5 s konfiguriert, empfohlen 30 s."

### R20: Fotografierbarkeitstest
Kann man den Begriff fotografieren? Nein → konkretisieren.
Wann nicht: Technische Abstraktionen mit präziser Definition sind OK (Latenz, Durchsatz).
"Probleme beheben"→"Fehlermeldungen im Log korrigieren",
"System verbessern"→"Antwortzeit von 800ms auf 200ms reduzieren".

Je konkreter, desto besser — die kleinste, konkreteste Einheit wählen:
❌ Vegetation → ✓ Eiche / Linde / Farn
❌ Transportmittel → ✓ Fahrrad / U-Bahn
❌ Wohnsituation → ✓ Zwei-Zimmer-Wohnung im dritten Stock

---

## P5 · Gliederung

### R21: Kernaussage zuerst
Wichtigstes am Anfang — Satz, Absatz, Abschnitt, Dokument.
Warum: Leser scannen. Wer abbricht, hat die Kernaussage trotzdem.
Wann nicht: Postmortems mit Chronologie, bewusstes Storytelling.
❌ "Wir haben Logs analysiert und verschiedene Konfigurationen getestet und festgestellt, dass das Problem an einem fehlenden Timeout liegt."
✓ "Das Problem: fehlender Timeout. Wir haben Logs analysiert und Konfigurationen getestet."

**Schlechte Einstiege vermeiden.** Diese Formeln sind Leser-Killer — streiche sie ersatzlos:
- "Seit jeher hat der Mensch…"
- "In der heutigen Zeit ist es wichtiger denn je…"
- "Im Folgenden wird dargestellt…"

Stattdessen: Kernaussage, Frage, provokante These oder konkrete Szene.

### R22: Absatz = eine Idee
Eine Idee, 3–5 Sätze. Struktur: Themensatz → Erklärung → Abschluss.
Wann nicht: Einzelsatz-Übergänge dürfen alleinstehen.

Abschließend prüfen: Was trägt dieser Absatz zur Kernbotschaft bei? Trägt er nichts bei → streichen oder umschreiben.

### R23: Übergänge explizit machen
Logische Beziehung zeigen. Wann nicht: Nicht jeden Satz mit Übergangswort beginnen.
Ursache→Folge: deshalb, daher, folglich. Gegensatz: aber, jedoch, trotzdem.
Ergänzung: außerdem, zudem. Einschränkung: allerdings, nur wenn.
Reihenfolge: zuerst, dann, danach, abschließend.

### R24: Überschriften konkret und aktiv
Keine vagen Nomen. Wann nicht: Etablierte Standard-Überschriften OK (Installation, Konfiguration).
Einleitung→Was dieser Dienst macht, Hintergrund→Warum wir X umgestellt haben,
Lösung→Konfiguration in 3 Schritten, Fazit→Empfehlung: X abschalten,
Fehlerbehebung→Häufige Fehler und ihre Ursachen.

### R25: Parallelismus in Listen
Alle Items gleiche grammatische Form. Wann nicht: Zu unterschiedliche Inhalte → Fließtext.
❌ "- Datei anlegen / - Konfiguration der Parameter / - Der Service muss gestartet werden"
✓ "- Datei anlegen / - Parameter konfigurieren / - Service starten"

### R26: Rhythmus durch Satzlängen-Variation
Nicht alle Sätze gleich lang. Kurze Sätze nach langen = Nachdruck.
Wann nicht: Referenzdoku, API-Docs — Gleichmäßigkeit akzeptabel.

### R27: Interpunktion als Stilmittel
Gedankenstrich (—): Einschub/Zuspitzung. "Fehl — seit gestern."
Doppelpunkt: kündigt an. "Das Problem: fehlender Timeout."
Semikolon: enge Verbindung ohne Konjunktion. "Startet; Verbindung schlägt fehl."

---

## P6 · Konsistenz

### R28: Ein Begriff je Konzept
Dasselbe Konzept immer mit demselben Begriff. Verschiedene Begriffe = verschiedene Konzepte.
Wann nicht: Bewusster Vergleich von Alternativen.
❌ "Konfiguration … Einstellungen … Parameter" (für dasselbe Konzept)
✓ Einen Begriff wählen und durchhalten.

Nur Nebensächliches variieren — das Wichtige ruhig wiederholen. Wien muss nicht zur »Donaumetropole« werden (der Leser denkt dann an den Fluss, nicht die Stadt). Der Tisch bleibt der Tisch — nicht »das Möbelstück« oder »der Vierbeiner«.

### R29: Terminologie einführen
Fachbegriffe beim ersten Auftreten ausschreiben. Format: Ausgeschrieben (ABK).
Wann nicht: Expertendokument für Fachpublikum → Grundbegriffe voraussetzen OK.

### R30: Gendersprache — neutrale Formulierungen
Neutrale Nomen bevorzugen. Sonderzeichen (*, :, _) vermeiden.
Warum: Keine anerkannte Orthographie (Rat f. dt. Rechtschreibung 2023), Screenreader-Probleme.
Nutzende statt Nutzer*innen, Lehrende statt Lehrer/innen,
Direktanrede (du/Sie) statt generisches Maskulinum,
Plural ("Alle Admins werden benachrichtigt.").

### R31: Einheitliche Zeitform
Eine Zeitform wählen, durchhalten. Empfehlung: Präsens (kürzer als Futur).

### R32: Einheitliche Anredeform
du/Sie/man — einmal wählen, durchhalten. Empfehlung: du (direkt, modern).

---

## Häufige Grammatikfehler

### R33: das / dass
das = Artikel oder Relativpronomen (ersetzbar durch "welches").
dass = Konjunktion (nicht ersetzbar durch "welches").
❌ "Ich sehe das das Skript fehlschlägt." ✓ "Ich sehe, dass das Skript fehlschlägt."

### R34: scheinbar / anscheinend
scheinbar = sieht so aus, ist es aber nicht (Täuschung).
anscheinend = sieht so aus und stimmt wahrscheinlich.
❌ "Der Fehler ist scheinbar aufgetreten." (=er ist es nicht?) ✓ "anscheinend aufgetreten."
✓ "Der Fehler ist scheinbar behoben." (=sieht behoben aus, ist es aber nicht)

### R35: wegen + Genitiv
Formell: wegen des Fehlers (nicht: wegen dem Fehler).
Wann nicht: Informelle Texte — Dativ verbreitet und akzeptiert.

### R36: wie / als
Gleiche Ebene: "so schnell wie". Komparativ: "schneller als".
❌ "schneller wie" ✓ "schneller als"

### R37: seit / seitdem
seit = Zeitpunkt ("seit dem Deployment").
seitdem = Zeitraum mit Folge ("wir haben deployt; seitdem läuft es stabil").

### R38: derzeit / zurzeit / seinerzeit
derzeit = zurzeit = im Moment (synonym). seinerzeit = damals.

### R39: aufgrund + Genitiv
aufgrund des Fehlers (nicht: aufgrund dem Fehler). Zusammenschreibung bevorzugt.

### R40: beziehungsweise (bzw.)
Bedeutet "im anderen Fall" oder "genauer gesagt" — nicht einfach "und" oder "oder".
❌ "Starte den Service bzw. die Datenbank." ✓ "... oder — falls bereits läuft — ..."

### R41: Komma vor "und"/"oder"
Kein Komma vor und/oder wenn kein vollständiger Nebensatz folgt.
❌ "Startet, und prüft die Verbindung." ✓ "Startet und prüft die Verbindung."
✓ "Startet, und die Verbindung wird geprüft." (zwei Hauptsätze → Komma OK)

### R43: kein statt nicht ein
❌ "Das ist nicht ein Fehler der ignoriert werden kann." ✓ "Das ist kein Fehler ..."

### R44: Satzanfang nicht mit Ziffer
❌ "3 Dienste sind ausgefallen." ✓ "Drei Dienste sind ausgefallen." / "Es sind 3 Dienste ausgefallen."

### R45: Bindestrich bei Abkürzungs-Komposita
DI-Container, CI-Konfiguration, API-Dokumentation, REST-Endpoint.

### R46: Leerzeichen vor Einheiten (DIN 1301)
5 ms, 100 MB, 30 s, 8 GB. Ausnahme: 99,9% (Prozent ohne Leerzeichen akzeptiert).

### R47: realisieren
Mehrdeutig: "erkennen" (original) oder "umsetzen" (Anglizismus).
In technischen Texten "umsetzen" oder "implementieren" bevorzugen.

---

## Technische Texte

### R48: Regeln für Markdown-Inhalte
Nicht als Stilfehler markieren: Code-Blöcke, URLs, Pfade, Variablennamen,
Kommandos, Versionsnummern, technische Bezeichner.
`/etc/app/config.yml` ist kein langer Nominalausdruck — es ist ein Pfad.
`MAX_WORKERS` ist kein Füllwort — es ist ein Konfigurationsparameter.

### R49: Commit-Messages — Was, nicht Wie
Imperativ. Beschreibt was sich ändert, nicht wie implementiert.
Format: `<typ>: <was ändert sich>` + optionale Begründung.
Typen: feat, fix, refactor, docs, chore, test, perf, ci.
Fix→fix: Health-Check-Timeout auf 30 s erhöht,
Changes→feat: Pomerium-Bypass für API-Routen,
WIP→refactor: Caddy-Konfiguration modularisiert.

### R50: README — Nutzen zuerst
Reihenfolge: 1. Was ist das (1 Satz Nutzen) 2. Wofür 3. Schnellstart 4. Konfiguration 5. FAQ.
Nicht mit Geschichte oder Danksagung beginnen.

### R51: ADR — Entscheidung im ersten Satz
Format: Status, Entscheidung, Begründung, Alternativen, Konsequenzen.
Entscheidung steht im Titel und im ersten Satz — nicht am Ende der Argumentation.

### R52: Warnhinweise sparsam
Max. 1–2 pro Seite. Zu viele → alle werden ignoriert.
NOTE für Hinweise, WARNING für destruktive Aktionen, TIP für Alternativen.

### R53: Version und Stand angeben
Bei statischer Doku: Version und Datum nennen.
Wann nicht: Lebende Dokumente (Wikis mit automatischer Aktualität).

### R54: Code-Blöcke mit Sprache annotieren
\`\`\`bash, \`\`\`yaml, \`\`\`python etc. — Syntax-Highlighting + Maschinenlesbarkeit.

### R55: Anleitungen als nummerierte Liste
Sequenzielle Schritte nummeriert, nicht als Fließtext.
Orientierung ("Ich bin bei Schritt 3") nur mit Nummerierung möglich.

---

## Fehlermeldungen (R56–R60)

### R56: Ursache, nicht Symptom
❌ "Error: Something went wrong."
✓ "Error: Verbindung zu postgres:5432 fehlgeschlagen. Server nicht erreichbar."

### R57: Konkrete Werte nennen
❌ "Error: Timeout aufgetreten."
✓ "Error: Timeout nach 5 s. Verbindung zu redis:6379 fehlgeschlagen (REDIS_TIMEOUT=5s)."

### R58: Handlung vorschlagen
❌ "Error: Konfigurationsdatei fehlt."
✓ "Error: `/etc/app/config.yml` nicht gefunden. Erstelle die Datei oder setze CONFIG_PATH."

### R59: Fehlercodes erklären
❌ "Error: E_CONN_REFUSED_0x0042"
✓ "Error: E_CONN_REFUSED (0x0042): Verbindung zu redis:6379 abgelehnt. Prüfe: `systemctl status redis`"

### R60: Aktiv und direkt
❌ "Es konnte keine Verbindung hergestellt werden."
✓ "Verbindung zu postgres:5432 fehlgeschlagen. Prüfe: `systemctl status postgresql`"

**Fehlermeldungs-Muster:**
`[Typ]: [Was fehlschlug] — [konkrete Werte]`
`Ursache: [warum]`
`Aktion: [was tun]`

---

## Denglisch-Verbfallen (R61–R70)

Wörtliche Übersetzungen aus dem Englischen, die grammatisch korrekt aber falsch klingen.

### R61: Exceptions und Fehler
schmeißen→werfen ("eine Exception werfen", nie "schmeißen")
fangen / catchen→abfangen ("Exception abfangen", das *ab-* ist nicht optional)
brechen→fehlschlagen / abbrechen / Exception werfen (Code *bricht* nicht, er *schlägt fehl*)
triggern→auslösen ("Fehler auslösen", *triggern* klingt amateurhaft in Prosa)
hitten→auf X stoßen ("auf einen Fehler stoßen", nie "hitten")
handeln→behandeln (*handeln* = to trade; Fehler werden *behandelt*)
anheben (raise)→werfen / auslösen (Deutsch hat kein "raise"-Idiom für Exceptions)
erholen von→sich erholen von / nach X zurückkehren (Reflexiv nicht weglassen)

### R62: Tests und Builds
passt (passes)→besteht / geht durch (*passen* = to fit; Tests *bestehen*)
failt / failed→schlägt fehl / fällt durch (*failen* ist reines Denglisch)
runnen→ausführen / laufen lassen (*ausführen* ist die kanonische Form)
covern→abdecken (*covern* ist Musikbranchen-Deutsch; Tests *decken ab*)
asserten→prüfen / zusichern (*eine Assertion* als Nomen OK; Verbform: *prüfen*)
gefangen (caught)→erkannt / aufgedeckt / abgefangen (*gefangen* = prisoner sense)

### R63: Datenfluss und Kontrolle
returnen→zurückgeben (kanonisch: "null zurückgeben")
callen→aufrufen ("Methode aufrufen")
passen (pass argument)→übergeben ("Parameter übergeben", nicht *passen*)
enden (end up)→landen ("Prozess landet in einem Zustand", nie *endet in*)
resolven→auflösen / ermitteln
checken→prüfen (schriftlich; *checken* in Chat akzeptiert)
auf Fehler hitten→auf Fehler stoßen

### R64: Calqued Idioms — wörtliche Übersetzungen die nicht existieren
"am Ende des Tages" (as an idiom)→letztlich / unter dem Strich / am Ende
"auf derselben Seite" (on the same page)→einer Meinung / auf demselben Stand
"low-hanging fruit"→leicht erreichbare Verbesserung / einfache Gewinne
"bare X" (ein bare get)→ein unqualifiziertes X / ein nacktes X
"vanilla" (default)→unverändert / Standard-
"happy path" (OK als Loanword)→Normalfall / Standardablauf
"Es ist wichtig, dass ..." (weak opener)→direkt mit Subjekt beginnen: "X muss ..."
"Wenn X, dann Y, was Z macht" (stacked calque)→in zwei Sätze aufteilen

### R65: Datentransfer-Verben eindeutschen
download→herunterladen, upload→hochladen, load→laden (Modul/Image) bzw. einlesen (Datei/Stream parsen), lazy load→nachladen
Warum: Hybridflexion wie "downgeloadet", "geuploadet", "geloadet" ist unflektierbares Stolper-Deutsch; die deutschen Vollverben sind eingebürgert und sauber trennbar.
Wann nicht: *der Download* / *der Upload* (Substantive) bleiben. Git-Verben *pushen, pullen, fetchen, clonen* bleiben als Fachkonzepte. False friend: *load* im Sinn von Auslastung wird *Last/Lasttest*, nie *einlesen*.
❌ "Das Image wird beim Start downgeloadet." ✓ "… heruntergeladen."
❌ "Die Konfig wird beim Start geloadet." ✓ "… eingelesen." (Parsen) / "… geladen." (allgemeines load)
❌ "Lade das Artefakt in die Registry up." ✓ "… in die Registry hoch."

### R66: Betriebsverben eindeutschen — Substantive behalten
monitort→überwacht, provisioniert→richtet ein, gescheduled→eingeplant / terminiert
Warum: Die deutschen Verben sind präzise; die Mischkonjugation ("gemonitort", "gescheduled") ist holprig und uneinheitlich.
Wann nicht: *Monitoring, Provisioning, Scheduler, Cronjob* bleiben. *deployen* und *Deployment* bleiben ebenfalls (siehe Anti-Regel #2 und R9) — "Bereitstellung" ist hier KEIN Ersatz.
❌ "Prometheus monitort die Latenz." ✓ "Prometheus überwacht die Latenz."
❌ "Terraform provisioniert die VMs." ✓ "Terraform richtet die VMs ein."
❌ "Der Cronjob ist für Mitternacht gescheduled." ✓ "… ist für Mitternacht eingeplant."

### R67: Daten und Persistenz
gecacht→zwischengespeichert (in Prosa), persistieren→speichern (außerhalb ORM), syncen→abgleichen / synchronisieren, dumpen→exportieren / ausgeben, seeden→mit Grunddaten befüllen
Warum: Englischer Stamm plus deutsche Beugung ergibt echtes Denglisch; das deutsche Verb steht bereit und ist präziser.
Wann nicht: *persistieren* bleibt in ORM-Fachsprache (JPA/Doctrine: "die Entität persistieren"); *synchronisieren, migrieren, serialisieren* sind etablierte Fachbegriffe; *der Cache* und *das Caching* bleiben.
❌ "Die Response wird gecacht." ✓ "Die Response wird zwischengespeichert."
❌ "Der Job synct die Tabellen jede Nacht." ✓ "Der Job gleicht die Tabellen jede Nacht ab."
❌ "Dumpe die Konfig nach config.json." ✓ "Exportiere die Konfig nach config.json."
❌ "Das Skript seedet die Datenbank." ✓ "Das Skript befüllt die Datenbank mit Grunddaten."

### R68: Verarbeitung und Transformation
prozessieren→verarbeiten, gemappt→zugeordnet / abgebildet, batchen→stapelweise verarbeiten
Warum: Englischer Stamm mit deutscher Beugung ergibt echtes Denglisch; *prozessieren* heißt auf Deutsch "einen Prozess führen / klagen" — ein echter Falschfreund.
Wann nicht: *aggregieren* (Lateinstamm) und *streamen* (etabliert) bleiben; das Nomen *Batch* bleibt — nur *batchen* ersetzen. *parsen* / *Parser* bleiben (CS-Lehnwort), und das Nomen *Mapping* bleibt.
❌ "Der Worker prozessiert die Events." ✓ "Der Worker verarbeitet die Events."
❌ "Die Felder werden auf das DTO gemappt." ✓ "Die Felder werden dem DTO zugeordnet."
❌ "Die Spalten werden auf das Schema gemappt." ✓ "Die Spalten werden auf das Schema abgebildet."
❌ "Der Importer batcht die Inserts." ✓ "Der Importer verarbeitet die Inserts stapelweise."

### R69: Skalierungs- und Lifecycle-Verben eindeutschen
scalen→skalieren (gerichtet: hoch-/herunterskalieren), restarten→neu starten, killen→abbrechen / hart beenden, shutdownen→herunterfahren, cleanuppen→aufräumen, resetten→zurücksetzen
Warum: Lifecycle-Operationen, die R61–R66 nicht abdecken; die deutschen Verben sind präzise und kurz, die Mischformen ("gekillt", "geresettet") klingen amateurhaft.
Wann nicht: *Reboot, Shutdown, Cleanup, Reset* (Substantive) bleiben. *rebooten, resetten, killen* sind mündlich toleriert; "SIGKILL senden" bleibt. Bedeutung beachten: killen = hart beenden, nicht herunterfahren.
❌ "Wir scalen die Replikas hoch." ✓ "Wir skalieren die Replikas hoch."
❌ "Der hängende Prozess wird heruntergefahren." ✓ "… wird hart beendet." (killen ≠ herunterfahren)
❌ "Das Skript cleanuppt die Temp-Dateien." ✓ "Das Skript räumt die Temp-Dateien auf."

### R70: Konfigurations- und Setup-Verben eindeutschen
setuppen→einrichten, enablen / disablen→aktivieren / deaktivieren, overriden→überschreiben / übersteuern, mounten→einbinden
Warum: Klare, kurze deutsche Entsprechungen; die Mischformen ("gemountet", "overridden", "gesetupt") sind nicht sauber flektierbar.
Wann nicht: *konfigurieren* ist eingebürgert und bleibt (*configuren* ist kein Wort). *Setup, Mount, Override* (Substantive) bleiben; *mounten* im Filesystem-Kontext toleriert. Sinn beachten: Methode/Default → *überschreiben*; Wert vorrangig setzen → *übersteuern*.
❌ "Das Feature-Flag wird disabled." ✓ "Das Feature-Flag wird deaktiviert."
❌ "Wir setuppen die CI-Umgebung." ✓ "Wir richten die CI-Umgebung ein."
❌ "Der Default wird per ENV overridden." ✓ "Der Standardwert wird per ENV übersteuert."

---

## Zeitform und Person (R71–R74)

### R71: Präsens-Indikativ als Standard
Default für: was Code tut, wie ein System funktioniert, was ein Ticket beschreibt.
❌ "Der Service würde eine Exception werfen." (Konjunktiv ohne Gegenfall)
✓ "Der Service wirft eine Exception." (Fakt → Indikativ)

### R72: Konjunktiv II nur für echte Hypothesen
Konjunktiv II (würde/wäre/hätte) nur wenn ein echter Gegenfall vorliegt.
✓ "Wenn wir die TTL senken würden, würde der Index seltener aufgebaut." (Hypothese)
✓ "Ohne den Decorator würde ein Rename erst im Behat-Lauf auffallen." (Gegenfall: Decorator existiert)
❌ "Der Service würde null zurückgeben wenn die DB leer ist." → ✓ "gibt … zurück"

### R73: Perfekt für abgeschlossene Arbeit — kein Präteritum
Präteritum klingt literarisch/erzählerisch — nie in Jira-Texten oder technischer Doku.
❌ "Der Test *schlug fehl*, weil die Fixture leer *war*." (Präteritum = Roman-Stil)
✓ "Der Test *ist fehlgeschlagen*, weil die Fixture leer war." (Perfekt = tech-natürlich)
Perfekt für: Status-Updates, Akzeptanzkriterien, abgeschlossene Schritte.
✓ "Die Lock-Datei ist aktualisiert. Die Pipeline läuft grün."

### R74: Kein Ich/Wir in Artefakt-Texten
"Ich" und "wir" gehören in Chat-Nachrichten und 1:1-Kommunikation — nicht in Tickets,
READMEs, Wikis oder Spezifikationen.
❌ "Ich habe den Bug gefixt." ✓ "Der Bug ist behoben."
❌ "Wir müssen das noch testen." ✓ "Das muss noch getestet werden."
❌ "Ich fixe das indem ich die Methode umbennene." ✓ "Fix: Methode wird auf X umbenannt."
"man" nur für generische Aussagen ohne identifizierbares Subjekt OK:
✓ "Man kann X auch über Y erreichen." — aber: ❌ "Man muss das Baseline neu aufbauen."
✓ "Das Baseline muss neu aufgebaut werden."

---

## Artikel und Komposita (R75–R76)

### R75: Artikel für Loanwords
Häufigste Fehlerquelle: falsches Genus. Korrekte Artikel:

**der:** Commit, Rebase, Merge, Branch, Build, Bug, Fix, Patch, Hook, Mock, Stub,
Wrapper, Decorator, Provider, Service, Controller, Token, Header, Callback,
Listener, State, Request, Endpoint, Cache, Index, Retry, Diff, Rollback, Hotfix,
Download, Upload, Reboot, Scheduler, Cronjob, Mount, Dump

**die:** Pipeline, Exception, Fixture, Assertion, Response, Session, Migration,
Query, Prop, Factory, Komponente, Schnittstelle, Regression, Roadmap

**das:** Interface, Feature, Event, Ticket, Issue, Template, Deployment, Staging,
Logging, Monitoring, Framework, Caching, Routing, Rendering, Payload,
Refactoring, Repository, Schema, Release, Timeout (oder *der*), Shutdown,
Cleanup, Setup, Mapping, Override, Provisioning

Wenn kein Eintrag: zuerst Duden prüfen, dann Microsoft German Style Guide.

### R76: Komposita — Stapelgrenze
Zusammengesetzte Nomen max. 3 Elemente. Ab 4: mit Präposition aufteilen.
✓ "Produkt-Konfigurations-Attribut" (3 Elemente — OK)
⚠ "Produkt-Konfigurations-Attribut-Validierung" (4 — grenzwertig)
❌ "Produkt-Konfigurations-Attribut-Validierungs-Service" (5 — aufteilen)
✓ "Validierungs-Service für Produkt-Konfigurations-Attribute"

Bindestrich-Regel: bei Loanword-Komposita immer Bindestrich:
Exception-Handler, CI-Pipeline, PriceList-Rebuild, API-Dokumentation.
Rein deutsche Komposita: Bindestrich optional, aber immer sicherer.

---

**Text beenden, wenn alles gesagt ist.** Kein Ausklingen, kein Nachtreten. Test: Fehlt etwas, wenn du den letzten Satz streichst? Nein → streichen. Jeder Text ist einen Satz zu lang.

---

## Checkliste

**Kürze**
- [ ] Kein Satz länger als 25 Wörter
- [ ] Füllwörter gestrichen
- [ ] Schmuck-Adjektive und Edelfüllsel gestrichen

**Aktivität**
- [ ] Kein ungerechtfertigtes Passiv (erlaubtes Passiv prüfen!)
- [ ] Keine auflösbaren Substantivierungen auf -ung/-keit/-ierung
- [ ] Blasse Verben durch präzisere ersetzt

**Konkretheit**
- [ ] Zahlen statt vage Beschreibungen
- [ ] Ursache-Wirkung explizit
- [ ] Kleinste konkreteste Einheit gewählt

**Gliederung**
- [ ] Kernaussage am Anfang
- [ ] Überschriften konkret
- [ ] Listen parallel formuliert
- [ ] Text endet, wenn alles gesagt ist

**Konsistenz**
- [ ] Ein Begriff je Konzept
- [ ] Einheitliche Anredeform
- [ ] Abkürzungen erklärt

**Stil & Klarheit**
- [ ] Positiv formuliert (kein »nicht selten«)
- [ ] Keine abgedroschenen Einstiegsfloskeln
- [ ] Erster Satz fesselt

**Sprache & Register**
- [ ] Kein Denglisch-Verb (returnen, failen, callen, triggern, geloadet, gemonitort, gecacht, gesynct, gemappt, gekillt, disabled, gemountet…)
- [ ] Kein calqued Idiom (am Ende des Tages, auf derselben Seite…)
- [ ] Zeitform: Präsens-Indikativ für Fakten, Perfekt für Abgeschlossenes
- [ ] Kein Konjunktiv II ohne echten Gegenfall
- [ ] Kein Ich/Wir in Dokument-Texten
- [ ] Komposita max. 3 Elemente, sonst Präposition
- [ ] Loanword-Artikel korrekt (die Exception, der Build, das Feature…)

---

## Typografie

Gedankenstrich: — (nicht -). In Markdown: — oder `--` je nach Renderer.
Anführungszeichen: „deutsch" nicht "englisch" für deutschen Text.
Leerzeichen vor Satzzeichen: keines vor , . ! ? : ;
Zahlen: bis 12 ausschreiben, ab 13 Ziffern.
Tausender: 1.000 oder 1 000 — nicht 1,000.
