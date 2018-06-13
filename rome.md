# Imperator Rome

## Entwicklertagebuch I - 28. Mai - Vision

Anfangsmotivation:
> Die Balance zwischen CK2, EU4 und V2 sollte in Rome 2 bestehen bleiben. Rome I war ein wunderbrase Spiel mit einem tollen Mix aus CK1(Charaktere), EU3 (Diplomatie & Krieg) und V1 (PArteien, Provinzen, Bevölkerung) kombiniert mit eigenen Features wie Barbarenmigration und die besten Bürgerkriege in Paradoxspielen https://forum.paradoxplaza.com/forum/index.php?threads/what-do-you-want-most-from-eu-rome-2-if-it-happens.769694/page-5#post-19193193

Konzepte aus dem ORignial, die sie entfernen/ändern wollten:
* Charaktere als Gesandte, schlechte Mechanik die v.a. genutzt wurde um Leute loszuwerden
* Omen und rel. Prestige waren wenig unterhaltsam und müssen geändert werden
* Handel war zu viel Micromanagement, auch dies wurde überarbeitet

![1](https://forumcontent.paradoxplaza.com/public/361060/2018_05_28_2.png)

Soweit möglich haben wir mehr Tiefe und Komplexität eingebaut um es zum ultimativen Grand Strategy Game zu machen.

## Entwicklertagebuch II - 4. Juni - Karte

Wahrscheinlich größte/detaillierteste Karte -> aber größer nicht immer besser, siehe HoI 3

Kleinste organisatorische Einheit auf Karte: Stadt (~Provinz in anderen Spielen) mit Ort, Bevölkerung, Handeslgüter und Gebäude
Nächste organisatorische Einheit: Provinz -> mehrere Städte (10-12)

Beispiel Sizilien, EU2 zwei Provinzen, CK2 fünf, EU4 drei, HoI 4 neun und Rome 23 Städte in zwei Provinzen mit vier unpassierbaren Gebirgen

![2](https://forum.paradoxplaza.com/forum/index.php?attachments/2018_06_04_6-png.376350)

Gründe für Startdatum: Interessante Zeit für Rom & die Diadochen im Osten.
Integration des südlichen Skandinaviens bewusst, da zum Startzeitpunkt die ursprünglichen germanischen Stämme aus Skandinavien nach Deutschland gewandert sind
Äthiopien lange aufgezeichnete Geschichte, der Nil ist bedeutend für Nordafrika und wir wollten soviel davon wie möglich integrieren
Indien relevant für hellenistische Ära, Konflikt zwischen Seleukiden & Maurya-Reich, griechische Händler haben mit Indien gehandelt
Außerdem auch interessante Staaten, die als Untertanen beginnen anstatt als von Gouverneuren regiert um besser pol. Realitäten darzustellen und dem Spieler mehr Möglichkeiten zu geben (z.B. Anatolien– Judäa)

Quellen beinhalten (aber nicht beschränkt auf):

* The Schwartzberg Historical Atlas of South Asia
* An Atlas of Ancient Indian History - Habib & Habib
* Perseus Digital Library
* Pelagios Project
* Pleiades Gazetteer

## Entwicklertagebuch II - 11. Juni - Machtpunkte / Ressourcen

* **Gold:** Verdient durch Handel und Steuern, verwendet für Entwicklung und Armeen
* **Manpower:** Für das bauen und erhalten von Armeen

Außerdem Machtpunkte, die nicht mit der Größe der Nation skalieren und als Balancing dienen
Machtpunkte erhält man v.a. durch die Fähigkeiten des Herrschers, aber es gibt auch Boni für nationale Ideen die zur Regierungsform passen

* ![mil](https://forum.paradoxplaza.com/forum/index.php?attachments/military-png.379145/) Militärisch, repräsentiert 'Virtus', genutzt für mil. Tradition, Hingabe inspirieren und Einheitenfähigkeiten
* ![civic](https://forum.paradoxplaza.com/forum/index.php?attachments/civic-png.379144/) Einfluss (Civic), repräsentiert 'Gravitas', genutzt für Erfindungen, Handelsrouten, Pops migrieren und anderes
* ![oratory](https://forum.paradoxplaza.com/forum/index.php?attachments/oratory-png.379146/) Rhetorik, reprärepräsentiert 'Dignitas', genutzt für Ansprüche, Gesetze erlassen, Parteien stärken und anderes
* ![religion](https://forum.paradoxplaza.com/forum/index.php?attachments/religious-png.379147/) Religion, repräsentiert 'Pietas', genutzt für Schweine abstechen, Bevölkerung konvertieren und Omen zu beschwören

Es gibt noch mehr Fähigkeiten, die eventuell auch eine Kombination von Punkten benötigen
**Aber:** Technologie erhält man durch Citizen-Pops, nicht durch Machtpunkte

![mil2](https://cdn.discordapp.com/attachments/456336207786278925/456336282193362945/mil.JPG)
![ora](https://cdn.discordapp.com/attachments/456336207786278925/456336284533915648/ora.JPG)


## Andere neue Infos


Performance mit Jomini angeblich besser als andere Spiele:
>Hoi4 specs should be good enough I guess.
>My work PC is a Intel(R) Core(TM) i7-6700 CPU @ 3.40GHz (8 CPUs), ~3.4GHz, with 16gb ram, and a NVIDIA GeForce GTX 1060 3GB.
>It takes about 28 seconds to run the first month in HoI4 at max speed on it.
>It takes about 28.5 seconds to run 1445 in EU4 on max-speed.  
>Current version of Imperator takes about 21 seconds to run the first year in.

**Bürgerkrieg-Beispiel (aus Telefoninterview):  **
Johan hat einen italienischen Minor gespielt und seine Hauptarmee wurde von einem sehr loyalen General befehligt. Er hat die Loyalität anderer ignoriert, die ziemlich gering war, da der Herrscher sehr uncharismatisch war und geringen Rhetorik-Skill hatte.
Als Folge haben andere Charaktere einen Bürgerkrieg mit zwei Dritteln der Provinzen angefangen und Johan hatte zwar eine starke Armee, aber keine guten Charaktere mehr um seine posten zu besetzen. Die Rebellen konnten schnell eine Armee ausheben und er musste einen sehr teure Rückeroberung führen.


* In den unspielbaren Gebieten können neuen Barbaren spawnen
* Unzivilisiertere Nationen haben v.a. Tribesmen und Sklaven -> Probleme mit den Mittelmeerreichen zu konkurieren -> wahrscheinlich Zivilisierungsmechanik
* Stämme sollen allgemein schwächer, dafür aber flexibler sein und zum Beispiel auch Wanderungen und Plünderungen ermöglichen


Out on the frontiers, many marginal societies will only have access to Tribesmen and Slaves, making it difficult for them to compete with the great Mediterranean empires unless they learn to adopt some of their civilized ways. Paradox wasn’t ready to go into detail about tribal mechanics yet, but said they're generally weaker but more flexible than the established empires and it will be fully possible to recreate such historical events as the Cimbri and the Teutons marching through the deep forests of Germany to ravage much of Spain and Italy in the 100s BCE.

* Charaktere haben Martial, Charisma, Finesse, Zeal - Militärische, Rhetorik, Einfluss, Religion Machtpunkte
* Charaktere die in den Rängen aufsteigen erhalten Prominence -> erwarten mehr für ihre Loyalität
* Korrupte Charaktere verringern Einkommen
* Soll auch Caesar-artige Aufstände geben, bei denen man auch die Seite des Aufstands wählen kann .
