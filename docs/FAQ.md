# FAQ

## Muss ich den Skill manuell aktivieren?

Nein. Claude Code lädt ihn nach der Installation automatisch. Sobald du auf Deutsch schreibst oder um Lektorat bittest, greifen die Regeln.

## Warum kommentiert der Skill mal, mal nicht?

Der Skill kennt zwei Modi. Im **Schreibmodus** wendet er die Regeln still an. Im **Lektüremodus** kommentiert er jede Änderung mit Regelreferenz. Der Lektüremodus startet, sobald du um Lektorat, Verbesserung oder Kritik bittest.

## Schreibt der Skill auch auf Englisch?

Nein. Er greift nur bei deutschem Text. Für englische Prosa gibt es eigene Stil-Skills.

## Wie reiche ich eine neue Regel ein?

Lies [CONTRIBUTING.md](../CONTRIBUTING.md). Dort steht das Schema einer Regel und der Weg über Issue und Pull Request.

## Wie prüfe ich, ob meine Änderung funktioniert?

`evals/evals.json` enthält sechs Testfälle. Installiere den Skill, gib den Prompt eines Testfalls an Claude, und vergleiche das Ergebnis mit den Assertions. Einen automatischen Runner gibt es noch nicht.

## Die Regeln widersprechen sich — welche gilt?

Es gilt die Hierarchie **Verständlichkeit > Kürze > Konsistenz > Stil**. Ein längerer, klarer Satz schlägt einen kurzen, unklaren.

## Woher stammen die Regeln?

Aus Engel (1911), Schneider, der tekom-Leitlinie und dem Hamburger Verständlichkeitsmodell. Die vollständige Liste mit Quellen steht in `skills/german-style-guide/referenz.md`.

## Verändert der Skill meinen Code?

Nein. Er wirkt nur auf Prosa: Doku, Commit-Messages, Fehlermeldungen, Berichte. Code-Kommentare lässt er bei kurzem Ad-hoc-Schreiben aus.
