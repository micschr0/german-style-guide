# Monitoring-Stack im Standort Nord

## Zweck und Grenzen

Der Monitoring-Stack dient der Erfassung von Metriken und der Benachrichtigung des Bereitschaftsteams. Die Erfassung erfolgt für zwölf Linux-Hosts und drei Anwendungsdienste im Standort Nord. Eine Überwachung der Kundendaten selbst findet nicht statt. Das Dashboard stellt Betriebszustände dar; es ersetzt keine Prüfung einzelner Geschäftsvorgänge. Für die Betrachtung durch das Bereitschaftsteam ist die Nutzung der Übersicht vorgesehen. Externe Kundschaft erhält keinen Zugang zu dieser Übersicht. Eine Aussage über die Verfügbarkeit des Standorts Süd ist mit diesen Daten nicht möglich.

## Erfassung und Aufbewahrung

Die Durchführung der Metrikerfassung erfolgt durch Prometheus. Das konfigurierte Abfrageintervall beträgt 30 Sekunden. Für die Aufbewahrung der Zeitreihen ist eine Dauer von 14 Tagen festgelegt. Der Node Exporter stellt die Metriken der Hosts bereit. Die drei Anwendungen stellen ihre Metriken jeweils unter `/metrics` bereit. Die Übertragung innerhalb des Monitoring-Netzes erfolgt verschlüsselt. Eine Änderung dieser Vorgaben ist im vorliegenden Dokument nicht beschlossen. Die Dokumentation der verwendeten Zertifikate erfolgt im internen Betriebswiki. Zertifikatswerte und Zugangsdaten gehören nicht in das Dashboard.

## Benachrichtigungen

Die Zustellung von Benachrichtigungen übernimmt Alertmanager. Eine Warnung zur Speicherauslastung erfolgt nach fünf Minuten oberhalb von 85 Prozent. Eine kritische Benachrichtigung erfolgt nach zwei Minuten oberhalb von 95 Prozent. Diese Bedingungen sind unabhängig voneinander zu prüfen. Das Bereitschaftsteam erhält kritische Benachrichtigungen über den vereinbarten Rufdienst. Warnungen werden im internen Kanal gesammelt. Eine automatische Durchführung von Neustarts ist nicht vorgesehen. Vor einem Eingriff sollte das Bereitschaftsteam die zugehörigen Logs prüfen. Eine verbindliche Pflicht zum Neustart ergibt sich aus einer Benachrichtigung nicht.

## Beobachtung vom Dienstag

Am Dienstag um 09:10 Uhr stieg die Antwortzeit des Dienstes `orders-api` an. Um 09:12 Uhr war zugleich eine erhöhte Speicherauslastung des Datenbankhosts zu sehen. Ein ursächlicher Zusammenhang ist bisher nicht nachgewiesen. Die Durchführung einer gemeinsamen Betrachtung beider Kurven ist für die nächste Besprechung vorgesehen. Der Dienst blieb erreichbar. Es liegt keine bestätigte Aussage über verlorene Bestellungen vor. Die Bezeichnung als vollständiger Ausfall wäre deshalb nicht durch die vorliegenden Beobachtungen gedeckt. Eine erneute Bewertung erfolgt erst nach der Sichtung weiterer Daten.

## Dashboard und Zugriff

Die Darstellung der Messwerte erfolgt in Grafana. Für die Anmeldung ist der zentrale Identitätsdienst vorgesehen. Mitglieder der Gruppe `ops-observer` erhalten ausschließlich Leserechte. Die Durchführung einer Änderung an Dashboards bleibt der Gruppe `ops-editor` vorbehalten. Diese Trennung dient der Vermeidung versehentlicher Änderungen während eines Einsatzes. Die Freigabe weiterer Gruppen ist derzeit nicht erfolgt. Bei Problemen mit der Anmeldung soll zunächst die vorhandene Betriebsanleitung verwendet werden. Eine konkrete Ursache für ein fehlgeschlagenes Login darf ohne Prüfung nicht aus der sichtbaren Fehlermeldung abgeleitet werden.

## Wartung und Zuständigkeit

Die Durchführung geplanter Wartungsarbeiten erfolgt donnerstags zwischen 18 und 19 Uhr. Das Plattformteam kündigt eine Wartung spätestens am vorherigen Arbeitstag an. Während des Wartungsfensters kann die Darstellung einzelner Kurven unterbrochen sein. Die Ankündigung einer Wartung ist keine Garantie für die Verfügbarkeit anderer Systeme. Für die Pflege der Benachrichtigungsregeln ist das Bereitschaftsteam zuständig. Die Pflege der Zugriffsgruppen erfolgt durch das Identitätsteam. Eine Übertragung dieser Zuständigkeiten ist nicht geplant. Unklare Zuständigkeiten müssen in der nächsten Betriebsbesprechung geklärt werden.

## Geplante Prüfung

Für Freitag ist die Durchführung eines Tests der Benachrichtigungskette geplant. Dabei soll eine künstliche Metrik ausschließlich in der Testumgebung verwendet werden. Eine Veränderung der Produktionsschwellen ist für diesen Test nicht freigegeben. Das Ergebnis wird anschließend im Betriebswiki dokumentiert. Erst nach dieser Dokumentation entscheidet das Plattformteam über weitere Schritte. Die Einführung einer zusätzlichen Langzeitaufbewahrung ist lediglich ein Vorschlag. Ein Budget und ein Termin dafür sind nicht beschlossen. Bis zu einer gesonderten Entscheidung bleibt die Aufbewahrungsdauer unverändert bei 14 Tagen. Das vorliegende Dokument enthält keine Freigabe zur Umsetzung dieses Vorschlags.
