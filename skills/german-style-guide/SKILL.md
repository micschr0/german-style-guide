---
name: german-style-guide
description: Deutsche Stilregeln für klares, präzises Schreiben. Aktiviere diesen Skill immer wenn auf Deutsch geschrieben, überarbeitet oder lektoriert wird — egal ob README, Commit-Message, Doku, ADR, Incident Report, E-Mail, Slack-Nachricht, Fehlermeldung oder technischer Bericht. Auch aktivieren wenn jemand fragt "klingt das gut?", "kannst du das verbessern?" oder ähnliches auf Deutsch. Nicht aktivieren für Code selbst oder rein englische Texte.
---

# Klar und präzise schreiben – Deutsche Stilregeln

Klares Deutsch ist eine handwerkliche Fähigkeit — kein Talent. Dieser Skill
enthält destillierte Regeln aus Engel (1911), Schneider, tekom-Leitlinie und
dem Hamburger Verständlichkeitsmodell, angepasst für technische Fachleute:
DevOps, Entwickler, Architekten. Die Regeln gelten universell; die Beispiele
kommen aus der Tech-Welt.

---

## Prioritätshierarchie bei Regelkonflikten

**Verständlichkeit > Kürze > Konsistenz > Stil**

Beispiel: Ein längerer Parallelsatz ist besser als ein kurzer, unklarer.

---

## Modi

**Schreibmodus** — Regeln still anwenden, kein Kommentar.
Wenn jemand einen Text erstellt: einfach besser schreiben.

**Lektüremodus** — Explizite Anmerkungen mit Regelreferenz.
Format: `[R7] Passiv → Aktiv: "wird deployt" → "deployt den Service"`
Aktivieren wenn: explizit um Lektorat, Verbesserung oder Kritik gebeten wird.

---

## Die 6 Prinzipien

### P1 · Kürze
Alles weglassen, was nicht zur Aussage beiträgt.
- R1: Sätze kurz halten (Ø 15 Wörter, max. 25)
- R2: Ein Gedanke pro Satz
- R3: Füllwörter streichen
- R4: Pleonasmen vermeiden
- R5: Modewörter durch Konkretes ersetzen

### P2 · Einfachheit
Bekannte Wörter, klare Konstruktionen.
- R6: Kurze Wörter bevorzugen
- R7: Schachtelsätze auflösen
- R8: Nebensätze ans Ende
- R9: Anglizismen nur wenn präziser oder etabliert
- R10: Abkürzungen beim ersten Auftreten erklären

### P3 · Aktivität
Verben, Aktiv, Handlung sichtbar machen.
- R11: Aktiv statt Passiv
- R12: Verben statt Substantivierungen (Nominalstil)
- R13: Hauptsache in den Hauptsatz
- R14: Handelnde Person nennen
- R15: Imperativ in Anleitungen

### P4 · Konkretheit
Fakten statt Abstraktionen.
- R16: Zahlen und Fakten nennen statt vager Beschreibungen
- R17: Beispiele geben statt nur zu beschreiben
- R18: Ursache und Wirkung explizit machen
- R19: "Was passiert?" beschreiben, nicht "was könnte passieren"
- R20: Fotografierbarkeitstest: ist der Begriff greifbar?

### P5 · Gliederung
Struktur, Reihenfolge, Übergänge.
- R21: Kernaussage zuerst (Absatz, Abschnitt, Dokument)
- R22: Absatz = eine Idee, 3–5 Sätze
- R23: Übergänge explizit machen
- R24: Überschriften konkret und aktiv formulieren
- R25: Parallelismus in Listen und Aufzählungen

### P6 · Konsistenz
Ein Begriff, eine Bedeutung — im gesamten Dokument.
- R26: Dasselbe Konzept immer mit demselben Begriff
- R27: Terminologie beim ersten Auftreten einführen
- R28: Gendersprache: neutrale Formulierungen, keine Sonderzeichen
- R29: Einheitliche Zeitform im Dokument
- R30: Einheitliche Anredeform (du/Sie/man)

---

## Vollständige Referenz laden

**`referenz.md`** enthält alle ~60 Regeln (R1–R60) mit vollständigem Schema
(Regel / Warum / Wann nicht / Schlecht → Gut), Fehlermeldungs-Abschnitt,
Checkliste und Quellen. ~700 Zeilen, ~6.000 Token.

Lade `referenz.md` wenn:
- Aktives Lektorat eines konkreten Texts
- Mehr als 3 Regeln gleichzeitig anwenden
- Erklärungen zu Regeln gefragt werden

Bei langen Texten (>500 Wörter): Subagent mit `referenz.md` dispatchen.

Nicht laden für: kurzes Ad-hoc-Schreiben, einzelne Sätze, Code-Kommentare.
