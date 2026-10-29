# Terminologie, Anrede und Fachsprache

Es gilt der [Regelkern](SKILL.md). [Geltung und Quellen](referenz.md#geltung-und-quellen).

## Konsistenz und Anrede

### R28: Fachbegriffe konsistent verwenden
**Typ:** Fachkonvention.
**Regel/Warum:** Benenne dasselbe Konzept konsistent, damit Leser es wiedererkennen.
**Wann nicht:** Verwandte Begriffe wie Konfiguration und Parameter nicht fälschlich gleichsetzen.
**Beispiel:** „Konfiguration (im Dialog: Einstellungen)“ kann notwendige unterschiedliche Benennungen ausdrücklich zuordnen.

### R29: Terminologie für das Publikum einführen
**Typ:** Stilheuristik.
**Regel/Warum:** Erkläre neue oder projektspezifische Begriffe, wo sie zum Verständnis gebraucht werden.
**Wann nicht:** Nicht jeden geläufigen Fachbegriff im Expertendokument definieren.
**Beispiel:** „Mit Release meinen wir hier die freigegebene Version samt Artefakten“ nur verwenden, wenn dies die Projektdefinition ist.

### R30: Personenbezeichnungen nach Vorgabe und Publikum wählen
**Typ:** Stilheuristik.
**Regel/Warum:** Beachte den Hausstil; ohne Vorgabe eignen sich klare neutrale Formen oder eine passende Direktanrede.
**Wann nicht:** Genderzeichenvorgaben sind Hausstil. Eignung für assistive Technik nicht pauschal behaupten.
**Beispiel:** „Das Betriebsteam erhält eine Nachricht“ ist möglich, wenn tatsächlich das Team gemeint ist.

### R31: Zeitbezüge konsistent darstellen
**Typ:** Stilheuristik.
**Regel/Warum:** Stelle vergangene, aktuelle und geplante Vorgänge unterscheidbar dar.
**Wann nicht:** Unterschiedliche Darstellungsebenen brauchen oft unterschiedliche Zeitformen.
**Beispiel:** „Gestern fiel der Dienst aus. Heute läuft er stabil“ benötigt keine durchgehend gleiche Zeitform.

### R32: Anrede aus Auftrag und Kontext übernehmen
**Typ:** Stilheuristik.
**Regel/Warum:** Verwende gewünschte oder vorhandene Anrede konsistent, ohne Ton und Distanz ungefragt zu ändern.
**Wann nicht:** Zitate oder verschiedene Adressatengruppen können andere Formen benötigen.
**Beispiel:** Eine mit „Sie“ formulierte Kundenanleitung nicht ungefragt auf „du“ umstellen.
## Fachsprache und Anglizismen

Die folgenden Regeln bieten Alternativen für technische Prosa. Entlehnte Verben
sind nicht allein wegen ihrer Herkunft falsch oder unflektierbar. Entscheidend
sind Publikum, Fachbedeutung, Glossar und verständliche Flexion. Die Vorschläge
sind keine pauschalen Ersetzungslisten für Code, Zitate oder Teamjargon.

### R61: Fehlerbehandlung begrifflich genau beschreiben
**Typ:** Stilheuristik.
**Regel/Warum:** Nutze bei passender Bedeutung etwa „Exception werfen“, „Exception abfangen“ und „Fehler behandeln“.
**Wann nicht:** Erkennen, Auslösen und Behandeln sind unterschiedliche Vorgänge.
**Beispiel:** „Der Handler catcht die Exception.“ → „Der Handler fängt die Exception ab“, sofern genau diese Operation gemeint ist.

### R62: Testhandlung und Testergebnis unterscheiden
**Typ:** Stilheuristik.
**Regel/Warum:** Nutze klare Begriffe wie „Test ausführen“, „Test besteht“ oder „Test schlägt fehl“.
**Wann nicht:** Das englische `assert` kann nach Kontext „prüfen“ oder „zusichern“ meinen.
**Beispiel:** „Der Test failt.“ → „Der Test schlägt fehl.“

### R63: Datenfluss mit etablierten Begriffen erklären
**Typ:** Stilheuristik.
**Regel/Warum:** Verwende bei passender Bedeutung „zurückgeben“, „aufrufen“ und „übergeben“.
**Wann nicht:** Auflösen, Ermitteln und Laden sind keine beliebigen Synonyme.
**Beispiel:** „Die Funktion returnt null.“ → „Die Funktion gibt null zurück.“

### R64: Übertragene Wendungen auf Verständlichkeit prüfen
**Typ:** Stilheuristik.
**Regel/Warum:** Ersetze im Kontext missverständliche oder unnötig umständliche Wendungen.
**Wann nicht:** „Am Ende des Tages“ existiert im Deutschen; sein Vorkommen allein ist kein Sprachfehler.
**Beispiel:** „Auf derselben Seite“ kann „einig“ oder „auf demselben Stand“ meinen. Ohne Kontext nicht automatisch ersetzen.

### R65: Datentransfer verständlich benennen
**Typ:** Stilheuristik.
**Regel/Warum:** Nutze bei passender Bedeutung herunter-, hochladen, laden oder einlesen.
**Wann nicht:** Laden und Parsen nicht gleichsetzen; Git-Operationen nicht zu allgemeinen Uploads/Downloads umdeuten.
**Beispiel:** „Das Image wird heruntergeladen“ passt, wenn tatsächlich ein Download gemeint ist.

### R66: Betriebsoperationen fachlich unterscheiden
**Typ:** Stilheuristik.
**Regel/Warum:** Wähle Überwachen, Bereitstellen, Provisionieren oder Einplanen nach tatsächlicher Operation und Glossar.
**Wann nicht:** Provisioning und Deployment nicht ohne Prüfung zu demselben Vorgang machen.
**Beispiel:** „Prometheus monitort die Latenz.“ → „Prometheus überwacht die Latenz.“

### R67: Persistenz- und Speicherbegriffe präzise verwenden
**Typ:** Stilheuristik.
**Regel/Warum:** Wähle nach Vorgang etwa Zwischenspeichern, Persistieren, Synchronisieren, Exportieren oder Befüllen mit Grunddaten.
**Wann nicht:** Persistieren ist nicht beliebiges Speichern; Synchronisieren kann mehr als Abgleichen bedeuten.
**Beispiel:** „Die Antwort wird gecacht.“ → „Die Antwort wird zwischengespeichert“, sofern dies dieselbe Operation bezeichnet.

### R68: Verarbeitung und Zuordnung genau benennen
**Typ:** Stilheuristik.
**Regel/Warum:** Nutze nach Bedeutung Verarbeiten, Zuordnen, Abbilden oder stapelweises Verarbeiten.
**Wann nicht:** Prozessieren kann fachsprachlich Verarbeitung bezeichnen; Mapping kann eine Transformation statt bloßer Zuordnung sein.
**Beispiel:** „Die Felder werden dem DTO zugeordnet“ nur verwenden, wenn tatsächlich eine Zuordnung gemeint ist.

### R69: Lebenszyklusoperationen nach Wirkung benennen
**Typ:** Stilheuristik.
**Regel/Warum:** Wähle passende Begriffe wie Skalieren, Neustarten, hartes Beenden, Herunterfahren oder Zurücksetzen.
**Wann nicht:** Hartes Beenden und geordnetes Herunterfahren nicht gleichsetzen; `SIGKILL` bleibt ein Bezeichner.
**Beispiel:** „Der Prozess wird gekillt“ → „Der Prozess wird hart beendet“, wenn die technische Bedeutung dies bestätigt.

### R70: Konfigurationsänderungen eindeutig beschreiben
**Typ:** Stilheuristik.
**Regel/Warum:** Nutze bei passender Bedeutung Einrichten, Aktivieren, Deaktivieren, Überschreiben, Übersteuern oder Einbinden.
**Wann nicht:** Method Overriding, Konfigurationspriorität und Dateisystem-Mounts sind unterschiedliche Fachkonzepte.
**Beispiel:** „Das Feature-Flag wird disabled.“ → „Das Feature-Flag wird deaktiviert.“
