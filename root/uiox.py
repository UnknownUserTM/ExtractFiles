import ui
import chat
import app
import fgGHGjjFHJghjfFG1545gGG
import snd
import item
import GFHhg54GHGhh45GHGH
import uiToolTip  
import wndMgr 
import time
import grp
import mouseModule  
import constInfo
import event
import settinginfo
import shop
import uiCommon

QUESTIONS = [
	["Kann Aspirin gegen einen Herzinfakt helfen?",True],
	["Besteht ein Diamant aus Kohlenstoff?",True],
	["Besteht ein Diamant aus Schwefel?",True],
	["Besteht Bronze aus Kupfer und Zinn?",True],
	["Besteht Bronze aus Kupfer und Silber?",False],
	["Beträgt der absolute Nullpunkt -273,15 Grad Celsius?",True],
	["Beträgt der absolute Nullpunkt -263,15 Grad Celsius?",False],
	["Heißt Gold auf lateinisch Germanium?",False],
	["Heißt Gold auf lateinisch Aurum?",True],
	["Bedeutet das Wort Atom teilbar?",False],
	["Bedeutet das Wort Atom unteilbar?",True],
	["Ist Radium Radioaktiv?",True],
	["Ist Hafnium Radioaktiv?",False], 
	["Ist Californium Radioaktiv?",True], 
	["Ist Mangan Radioaktiv?",False], 
	["Gehört Helium zu den Edelgasen?",True], 
	["Gehört Radon zu den Gasen?",True],
	["Ist Radon Radioaktiv?",True],
	["Hat Bohrium im Periodensystem die Ordnungszahl 107?",True],
	["Hat Neodym im Periodensystem  die Ordnungzahl 60?",True],
	["Hat Wasserstoff im Periodensystem die Ordnungszahl 1?",True], 
	["Hat Bohrium im Periodensystem die Ordnungszahl 70?",False], 
	["Hat Bohrium im Periodensystem die Ordnungszahl 51?",False],
	["Hat Neodym im Periodensystem die Ordningszahl 55?",False],
	["Hat Neodym im Periodensystem die Ordnungszahl 26?",False], 
	["Hat Wasserstoff im Periodensystem die Ordnungszahl 72?",False], 
	["Hat Wasserstoff im Periodensystem die Ordnungszahl 22?",False], 
	["Hat das Element Eisen die Abkürung Fe?",True],
	["Hat das Element Quecksilber die Abkürzung Hg?",True], 
	["Hat das Element Kalium die Abkürzung K?",True],
	["Hat das Element Platin die Abkürzung Pt?",True], 
	["Hat das Element Silber die Abkürzung Ag?",True],
	["Hat das Element Eisen die Abkürzung Ei?",False],
	["Hat das Element Quecksilber die Abkürzung Qs?",False], 
	["Hat das Element Kalium die Abkürzung Km?",False],
	["Hat das Element Platin die Abkürzung P?",False],
	["Hat das Element Silber die Abkürzung Sr?",False], 
	["Ist das Element Brom im Aggregatzustand Flüssig?",True], 
	["Ist das Element Brom im Aggregatzustand  Fest?",False],
	["Ist das Element Uran im Aggregatzustand Fest?",True],
	["Wird die Chemie auch Scheidekunst genannt?",True],
	["Hat Albertus Magnus das Chemische Element Arsen entdeckt?",True],  
	["Wird Trichlorphenol =TCP= aus Tetrachlorbenzol unter Zugabe von Natriumhydroxid Hergestellt?",True], 
	["Wird Natriumhydroxid auch Ätznatron gennant?",True],
	["Ist Chlorakne ein Symptom einer Vergiftung durch chlorierte Kohlenwasserstoffe?",True], 
	["Wurde im Mittelalter die Chemie, Alchemie genannt?",True],
	["Wird Natronhydrogencarbonat auch Doppeltkohlensaures Natron genannt?",True], 
	["Hat Henry Cavendish Das Element Wasserstoff entdeckt?",True],
	["Ist das Universum etwa 13,7 Milliarden Jahre alt?",True],
	["Dehnt sich das Universum immer weiter aus?",True],
	["Zieht sich das Universum immer weiter zusammen?",False],
	["Ist das Universum etwa 13,7 Millionen Jahre alt?",False],
	["Ist eine Supernova das kurze Aufleuchten eines Explodierenden Massereichen Sterns?",True],
	["Kann aus einer Supernova ein schwarzes Loch entsehen?",True],
	["Kann aus einer Supernova ein Pulsar entstehen?",True],
	["Ist ein Pulsar ein schnell rotierender Neutronenstern?",True],
	["Ist ein Pulsar ein schnell rotierender Protonenstern?",False],
	["Stammt das Wort Psychologie aus dem Griechischen?",True],
	["Stammt das Wort Psychologie aus dem Lateinischen?",False],
	["Wurde das Ouija-Brett 1891 von Elijah Bond Patentiert?",True], 
	["Wurde das Ouija-Brett 1881 von Elijah Bond Patentiert?",False],
	["War Elijah Bond der Erfinder des Ouija-Brettes?",True],
	["War William Fuld der Erfinder des Ouija-Brettes?",False],
	["Soll Ouija vermutlich aus dem französischen und deutschen ein Ja beinhalten?",True],
	["Wird in der Physik Kraft mit Newton gerechnet?",True],
	["Wird in der Physik Kraft mit Hertz gerechnet?",False],
	["Besteht das Skelett von Stachelhäutern aus Calcit?",True],
	["Besteht das Skelett von Stachelhäutern aus Magnesiumsulfat?",False],
	["Bildet das Skelett bei Lebewesen die Stützfunktion?",True],
	["Bildet das Skelett bei Lebewesen keine Stützfunktion?",False],
	["Sind die Knochen der Vögel teilweise mit Luft gefüllt?",True], 
	["Sind die Knochen der Vögel nicht mit Luft gefüllt?",False],
	["Besitzt der Mensch eine sogenannte Siebbeinhöhle?",True],
	["Besitzt der Mensch eine sogenannte Gaumenhöhle?",False],
	["Ist Multiple Sklerose =MS= eine Erkrankung des Nervensystems?",True],
	["Ist Multiple Sklerose =MS= eine Erkrankung der Muskulatur?",False],
	["Ist Multiple Sklerose =MS= eine Erkrankung der Knochen?",False],
	["Befasst sich die Angiologie mit Gefäßkrankheiten?",True],
	["Befasst sich die Angiologie mit Nervenkrankheiten?",False],
	["Befasst sich die Angiologie mit Knochenkrankheiten?",False],
	["Sind ca. 3% Arbeitsunfähig nach einer Reisekrankheit?",True],
	["Sind ca. 6% Arbeitsunfähig nach einer Reisekrankheit?",False],
	["Steht die Abkürzung FSME für Frühsommer-Meningoenzephalitis?",True],
	["Steht die Abkürzung FSME für Frühsommer-Meningitis?",False],
	["Ist der Zusatzstoff E-500 ein Salz der Kohlensäure?",True],
	["Wird der Mars als roter Planet bezeichnet?",True],
	["Wird der Jupiter als roter Planet bezeichnet?",False],
	["Liegt Chile in Südamerika?",True],
	["Liegt Indonesien in Südamerika?",False],
	["Liegt Argentinien in Südamerika?",True],
	["Liegt Bolivien in Südamerika?",True],
	["Liegt Panama in Südamerika?",False],
	["Liegt Honduras in Südamerika?",False],
	["Liegt Belize in Südamerika?",False],
	["Grenzt das Karibische Meer an Venezuela?",True],
	["Grenzt das Karibische Meer an Bolivien?",False],
	["Ist Südafrika das Flächenmäßig größte Land in Südamerika?",False],
	["Ist Brasilien das Flächenmäßig größte Land in Südamerika?",True],
	["Ist Sucre die Hauptstadt von Bolivien?",True],
	["Ist Santiago die Hauptstadt von Bolivien?",False],
	["Beträgt die Fläche von Südamerika circa 18 Millionen Quadratkilometer?",True],
	["Beträgt die Fläche von Südamerika circa 9 Millionen Quadratkilometer?",False],
	["Beträgt die Fläche von Südamerika circa 23 Millionen Quadratkilometer?",False],
	["Beträgt die Fläche von Südamerika circa 28 Millionen Quadratkilometer?",False],
	["Sind die Anden die längste Gebirgskette der Erde?",True],
	["Sind die Alpen die längste Gebirgskette der Erde?",False],
	["Liegt Mallorca im Mittelmeer?",True],
	["Liegt Mallorca im Atlantik?",True],
	["Ist die Donau der längste Fluss in Europa?",False],
	["Ist die Wolga der längste Fluss in Europa?",True],
	["Ist die Oder der längste Fluss in Europa?",False],
	["Ist der Rhein der längste Fluss in Europa?",False],
	["Ist Stockholm die Hauptstadt von Schweden?",True],
	["Ist Oslo die Hauptstadt von Schweden?",False],
	["Ist Stockholm die Hauptstadt von Norwegen?",False],
	["Ist Oslo die Hauptstadt von Norwegen?",True],
	["Steht das Chilehaus in Hamburg?",True],
	["Steht das Chilehaus in Chile?",False],
	["Hat die Schweiz 26 Kantone?",True],
	["Hat die Schweiz 28 Kantone?",False],
	["Steht das Taj Mahal in Agra?",True],
	["Steht das Taj Mahal in Bhopal?",False],
	["Steht das Taj Mahal in New Delhi?",False],
	["Steht das Taj Mahal in Jaipur?",False],
	["Steht der Tempel der Artemis in Ephesos?",True],
	["Steht der Tempel der Artemis in Athen?",False],
	["Steht der Tempel der Artemis in Izmir?",False],
	["Ist die Hauptstadt von Hessen Potsdam?",False],
	["Ist die Hauptstadt von Hessen Frankfurt?",False],
	["Ist die Hauptstadt von Hessen Wiesbaden?",True],
	["Hat das Bundesverfassungsgericht seinen sitz in Karlsruhe?",True],
	["Hat das Bundesverfassungsgericht seinen sitz in Berlin?",False],
	["Liegen die Pyrenäen in Europa?",True],
	["Liegen die Anden in Europa?",False],
	["Ist die Hauptstadt von Polen Danzig?",False],
	["Ist die Hauptstadt von Polen Warschau?",True],
	["Beträgt die Fläche von Europa circa 10 Millionen Quadratkilometer?",True],
	["Beträgt die Fläche von Europa circa 5 Millionen Quadratkilometer?",False],
	["Beträgt die Fläche von Europa circa 20 Millionen Quadratkilometer?",False],
	["Beträgt die Fläche von Europa circa 2 Millionen Quadratkilometer?",False],
	["Liegt Afrika südlich von Europa?",True],
	["Liegt Asien südlich von Europa?",False],
	["Fließt der Fluss Donau durch Prag?",False],
	["Fließt der Fluss Moldau durch Prag?",True],
	["Gehört Kreta zu Zypern?",False],
	["Gehört Kreta zu Griechenland?",True],
	["Liegt Andorra zwischen Spanien und Frankreich?",True],
	["Liegt Malta zwischen Frankreich und Spanien?",False],
	["Ist die größte Wüste in Afrika die Sahara-Wüste?",True],
	["Ist die größte Wüste in Afrika die Atacama-Wüste?",False],
	["Ist Kairo die meistbewohnte Stadt in Afrika?",True],
	["Ist Alexandria die meistbewohnte Stadt in Afrika?",False],
	["Gibt es in Afrika 2000 verschiedene Sprachen?",True],
	["Gibt es in Afrika 200 verschiedene Sprachen?",False],
	["Ist die Hauptstadt von Marokko Rabat?",True],
	["Ist die Hauptstadt von Marokko Marrakesch?",False],
	["Ist die Küste von ganz Afrika etwa 3000 Kilometer lang?",False],
	["Ist die Küste von ganz Afrika etwa 30000 Kilometer lang?",True],
	["Ist Ägypten das größte Land in Afrika?",False],
	["Ist Algerien das größte Land in Afrika?",True],
	["Ist der Indische Ozean westlich von Afrika?",False],
	["Ist der Antlantische Ozean westlich von Afrika?",True],
	["Ist Russland das Flächenmäßig größte Land in Asien?",True],
	["Ist China das Flächenmäßig das größte Land in Asien?",False],
	["Ist der höchste Berg in Asien der Mount Everest?",True],
	["Ist der höchste Berg in Asien der K2?",False],
	["Grenzt der Indische Ozean an Japan?",False],
	["Grenzt der Pazifische Ozean an Japan?",True],
	["Ist Peking die Hauptstadt von Süd-Korea?",False],
	["Ist Soul die Hauptstadt von Süd-Korea?",True],
	["Liegt die Mongolei zwischen China und Russland?",True],
	["Liegt die Mongolei zwischen Japan und China?",False],
	["Bestehen die Philippinen aus 452 Inseln?",False],
	["Bestehen die Philippinen aus 6842 Inseln?",False],
	["Bestehen die Philippinen aus 2487 Inseln?",False],
	["Bestehen die Philippinen aus 7641 Inseln?",True],
	["Ist der längste Fluss in Asien der Nil?",False],
	["Ist der längste Fluss in Asien der Amazonas?",False],
	["Ist der längste Fluss in Asien der Mississippi?",False],
	["Ist der längste Fluss in Asien der Jangtsekiang?",True],
	["Ist Washington, D.C. die Hauptstadt der USA?",True],
	["Ist Washington die Hauptstadt der USA?",False],
	["Beträgt die Fläche der USA circa 10 Millionen Quadratkilometer?",True],
	["Beträgt die Fläche der USA circa 5 Millionen Quadratkilometer?",False],
	["Beträgt die Fläche der USA circa 100 Millionen Quadratkilometer?",False],
	["Beträgt die Fläche der USA circa 15 Millionen Quadratkilometer?",False],
	["Ist die Stadt Los Angeles in Kalifornien?",True],
	["Ist die Stadt Los Angeles in Florida?",False],
	["Fließt der Fluss Po durch Florenz?",False],
	["Fließt der Fluss Arno durch Florenz?",True],
	["Befindet sich in Albanien die Stadt Varna?",False],
	["Befindet sich in Bulgarien die Stadt Varna?",True],
	["Ist der südlichste Punkt Afrikas Cape Horn?",False],
	["Ist der südlichste Punkt Afrikas Cape of Goog Hope?",False],
	["Ist der südlichste Punkt Afrikas Cape Agulhas?",True],
	["Führt durch die Stadt Mainz der fünfzigste Breitengrad?",True],
	["Führt durch die Stadt Koblenz der fünfzigste Breitengrad?",False],
	["Führt durch die Stadt Saarbrücken der fünfzigste Breitengrad?",False],
	["Ist die Stadt Marsala in Sizilien?",True],
	["Ist die Stadt Marsala in Sardinien?",False],
	["Ist der höchste Berg Ozeaniens mit 5030m Höhe der Puncak Jaya?",True],
	["Ist der höchste Berg Ozeaniens mit 5030m Höhe der Mount Snowdon?",False],
	["Liegt die Stadt Radolszell am Bodensee?",True],
	["Liegt die Stadt Radolszell am Chiemsee?",False],
	["Liegt die Region Ramsau in Österreich?",True],
	["Liegt die Region Ramsau in der Schweiz?",False],
	["Entspringt der Fluss Saar im Schwarzwald?",False],
	["Entspringt der Fluss Saar in den Vogesen?",True],
	["Liegt die Stadt Magdeburg in Sachsen?",False],
	["Liegt die Stadt Dresden in Sachsen?",True],
	["Ist der längste Fluss in Kalifornien der San Antonio-River?",False],
	["Ist der längste Fluss in Kalifornien der Los Angeles-River?",False],
	["Ist der längste Fluss in Kalifornien der Sacramento-River?",True],
	["Gehört die Provinz Seeland zu den Niederlanden?",True],
	["Gehört die Provinz Seeland zu Belgien?",False],
	["Gehört die Provinz Seeland zu Schweden?",False],
	["Ist Bornholm die größte Insel in Dänemark?",False],
	["Ist Seeland die größte Insel in Dänemark?",True],
	["Verliert eine Kiefer ihre Nadeln im Winter?",False],
	["Leben in der Antarktis Pinguine?",True],
	["Leben in der Arktis Pinguine?",False],
	["Fressen Eisbären Pinguine in freier Wildbahn?",False],
	["Ist die Antarktis ein Kontinent?",False],
	["Ist Antarktika ein Kontinent?",True],
	["Herrschen in der Antarktis Durchschnittlich -55 grad°?",True], 
	["Geht die Sonne am Nordpolarkreis im Sommer unter?",False],
	["Können Haie rückwärts Schwimmen?",False],
	["Ist ein Brillant nach dem Schliff benannt?",True],
	["Hat der Ameisenbär eine bis zu 60 cm lange Zunge?",True],
	["Hat der Ameisenbär eine über 60 cm lange Zunge?",False], 
	["Frisst ein Elefant bis zu 400 Kg Nahrung am Tag?",True],
	["Gehören Fledermäuse zu den Säugetieren?",True],
	["Gehören Fledermäuse zu den Vögeln?",False],
	["Sind Fledermäuse die einzigsten Säugetiere die fliegen können?",True],
	["Gibt es Fledermäuse die sich ausschließlich von Blut Ernähren?",True], 
	["Können Fledermäuse bis zu 30 Jahre alt werden?",True],
	["Stehen Wölfe in Deutschland unter Naturschutz?",True], 
	["Ist die Loire der letzte ungebändigte Strom Europas?",True],
	["Benutzten die Ägypter den Schlamm des Nils als Dünger?",True],
	["Sind Katzen sogenannte Ansitzjäger?",True],
	["Ist die Haltung eines Chamäleons Meldepflichtig?",True],
	["Haben Chamäleons eine sogenannte Schleuderzunge?",True],
	["Haben Chamäleons eine sogennante Peitschenzunge?",False], 
	["Wachsen die Nadeln der Kiefer einzeln und auch in Bündeln von 2-8 Nadeln?",True],
	["Wachsen die Nadeln der Kiefer nur einzeln?",False],
	["Wachsen die Nadeln der Kiefer nur in Bündeln?",False], 
	["Ergibt eine Schätzung ca. 21.000-96.000 Todesfälle durch Giftschlangen pro Jahr?",True],
	["Ergibt eine Schätzung ca. 100.000 Todesfälle durch Giftschlangen pro Jahr?",False],
	["Kann die kleinste Phytonart ca. 70-90 cm Lang werden?",True],
	["Wird die größte Phytonart ca. knapp über 6 meter?",True],
	["Erkranken heutzutage immer noch bis zu 3000 Menschen an der Pest?",True],
	["Kann man bei einer Nebensonne 3 Sonnen gleichzeitig sehen?",True],
	["Sind die Nebensonnen in einem Winkel von etwa 22° zu sehen?",True],
	["Ist ein Regenbogen eigentlich ein Kreis?",True],
	["Ist ein Regenbogen eigentlich ein Halbkreis?",False],
	["Entsteht der Effekt der Nebensonne durch Eiskristalle?",True],
	["Entsteht der Effekt der Nebensonne durch Wassertröpfchen?",False],
	["Entsteht der Effekt eines Regenbogens durch Eiskristalle?",False],
	["Entsteht der Effekt eines Regenbogens durch Wassertröpfchen?",True],
	["Nennt man das eintreten des Mondes in den Schatten eines Planeten Immersion?",True],
	["Steht bei einer Mondfinsternis die Erde zwischen Sonne und Mond?",True],
	["Steht bei einer Mondfinsternis der Mond Zwischen Sonne und Erde?",False],
	["Steht bei einer Sonnenfinsternis der Mond zwischen Erde und Sonne?",True],
	["Steht bei einer Sonnenfinsternis die Erde zwischen Mond und Sonne?",False],
	["Hat ein Quader 9 Ecken?",False],
	["Ist 3,1415926535897932384626433832795028841971 die Zahl Pi?",True],
	["Ist 3,1415926535897932384626433832795028841971 die Zahl Pi?",True],
	["Ist 3,1415926535897932384626433832795028841971 die Zahl Pi?",True],
	["Ist 3,1415926535897932384626433832795028841971 die Zahl Pi?",True],
	["Ist 3,1415926535897932384626433832795028841971 die Zahl Pi?",True],
	["Ist 3,1415926535897932384626443832795028841971 die Zahl Pi?",False],
	["Ist 3,1415926535896932384626433832795028841971 die Zahl Pi?",False],
	["Ist 3,1415926535897932384626433832795028741971 die Zahl Pi?",False],
	["Ist 3,1415927535897932384626433832795028841971 die Zahl Pi?",False],
	["Ist 3,1415926535897932384626433832795029841971 die Zahl Pi?",False],
	["Besteht ein Basketballteam aus 5 Spielern?",True],
	["Besteht ein Basketballteam aus 7 Spielern?",False],
	["War George Washington der erste Präsident der USA?",True],
	["War Phil Washington der erste Präsident der USA?",False],
	["Ist Donald Trump der 45. Präsident der USA?",True],
	["Hat die Flagge der USA 50 Sterne?",True],
	["Hat die Flagge der USA 51 Sterne?",False],
	["Hat die Flagge der USA 49 Sterne?",False],
	["Ist Alaska seit 1903 offiziell im Besitz der USA?",False],
	["Ist Alaska seit 1860 offiziell im Besitz der USA?",False],
	["Ist Alaska seit 1867 offiziell im Besitz der USA?",True],
	["Hat Neil Armstrong als erster Mensch den Mond betreten?",True],
	["Hat Buzz Aldrin als erster Mensch den Mond betreten?",False],
	["Wurde die letzte deutsche Dampflok 1972 außer Betrieb gestellt?",False],
	["Wurde die letzte deutsche Dampflok 1977 außer Betrieb gestellt?",True],
	["Hatte Ramses der 2. 40 Töchter?",True],
	["Hatte Ramses der 2. 45 Söhne?",True], 
	["Hatte Ramses der 2. 40 Söhne?",False],
	["Hatte Ramses der 2. 45 Töchter?",False], 
	["Bestand Magellans Flotte aus 5 Schiffen?",True],
	["Bestand Magellans Flotte aus 3 Schiffen?",False],
	["Hieß eines der Schiffe von Magellans Weltumsegelung Santiago?",True], 
	["Hieß eines der Schiffe von Magellans Weltumsegelung Trinidad?",True],    
	["Hieß eines der Schiffe bei Magellans Weltumsegelung Tobak?",False], 
	["Starb Magellan auf der Insel Mactan?",True],
	["Starb Magellan am 21. April 1521?",True],
	["Starb Magellan am 21. März 1521?",False],
	["Brachte bei Magellans Weltumsegelung nur ein Schiff die Reise zu Ende?",True], 
	["Wurde die Schöne Helena nach Troja entführt?",True],
	["Wurde die schöne Athena nach Troja entführt?",False], 
	["Ist die Artus Sage auf den Englischen König Richard Löwnherz bezogen?",True],
	["Wollte der Papst in die Scheidung Heinrich des 8. und seiner Frau einwilligen?",False],
	["Wurde die Königin Mary 1. auch Bloody Mary genannt?",True],
	["Wurde Kaiser Karl der 5. in Aachen gekrönt?",True],
	["Starb der Forscher David Livingstone bei der Suche nach der Nilquelle?",True],
	["Starb der Forscher David Livingstone bei der Suche nach der Amazonasquelle?",False],
	["Wiegt ein Block einer Ägyptischen Pyramide mind. 2,5 Tonnen?",True],
	["Wurde Das Heilige Römische Reich Deutscher Nation ab mitte des 15. Jahrhunderts geprägt?",True],
	["Hatten manche Dinosaurier Federn?",True],
	["Heißt der Merkspruch von Roms Gründung 7,5,3, Rom kroch aus dem Ei?",True],
	["Heißt der Merkspruch von Roms Gründung 7,2,3, Rom kroch aus dem Ei?",False],
	["Wurde Rom nach Etruskischem und Griechischem Vorbild erbaut?",True],
	["Wurde ein Aquädukt zur Frischwasserversorgung genutzt?",True],
	["Wurde ein Aquädukt zur Abwasserentsorgung genutzt?",False],
	["Brannte Rom im Jahr 64 nach Christus?",True],
	["Brannte Rom im Jahr 55 nach Christus?",False],
	["Brannte Rom im Jahr 105 nach Christus?",False],
	["Hatte das Kolosseum ca. 50.000 Plätze?",True],
	["Bedeutet Hieroglyphen Heilige Vertiefungen?",True],
	["Hat die Demokratie seinen Ursprung in Athen?",True],
	["Wurde König Friedrich der 1. auch Barbarossa genannt?",True],
	["Heißt Barbarossa eigentlich Roter Bart?",True],
	["Wurde das Kloster Lorch von Barbarossa und seiner Familie gestiftet?",True],
	["Wurde das Kloster Schöntal von Barbarossa und seiner Familie gestiftet?",False],
	["Verkauft Uriel Tränke und andere Items?",False],
	["Sind alle drei reiche direkt miteinander verbunden?",False],
	["Kann man mit Level 39 in den Dämonenturm?",False],
	["Kann man bei der Gemischtwarenhändlerin Items Verkaufen?",True],
	["Verkauft der Rüstungshändler Level 34 Rüstungen?",False],
	["Hat der Metin der Schlacht das Level 25? ",False],
	["Verkauft die Gemischtwarenhändlerin grüne Tränke? ",True],
	["Begegnet man dem stolzen Dämonenkönig auf Ebene 3 des Dämonenturms ? ",False],
	["Kostet es 200k, wenn man eine Gilde aufmachen will ? ",False],
	["Heißt das Feuerland Dojum Papier ? ",False],
	["Haben MODs was mit der InGame arbeit zu tun ? ",False],
	["Kann eine Drachenschami heilen ? ",False],
	["Kann eine Kriegerin mit einem Fächer kämpfen ? ",False],
	["Gibt es Pet EXP - Ringe nur im Itemshop zu kaufen ? ",False],
	["Kann man seine Frisur umändern ? ",True],
	["Kann man sich zu seinem Ehepartner porten ? ",True],
	["Kann auch das Pferd Fähigkeiten erlernen ? ",True],
	["Bekommt man Fertigkeitsbücher nur aus Metinsteinen ? ",False],
	["Kann man alle Waffen tragen ? ",False],
	["Bekommt man Seelensteine aus jeder Mission ? ",False],
	["Kann man seine ITEM`s verlieren ? ",True],
	["Kann man über Level 30 noch seine Lehre ändern ? ",True],
	["Kann man seine Angelrute bei dem Schmied verbessern? ",False],
	["Kann man sich bei der alten Frau von seinem Ehepartner scheiden lassen? ",False],
	["Hat der Dämonen Turm 7 Ebenen? ",True],
	["Ist Se-Rang der Anführer der Weißen Eids? ",False],
	["Hat man von Anfang an Fertigkeiten ? ",False],
	["Kann man beim Fischer Lagerfeuer kaufen? ",True],
	["Darf man mit angezogener Rüstung einen Shop aufmachen ? ",False],
	["Kann man mit lvl 1 schon einen negativen Rang haben? ",False],
	["Kann man Spieler aus einem anderen Reich in die Gruppe nehmen? ",True],
	["Kann man Spieler aus einem anderen Reich Heiraten? ",False],
	["Ist es möglich 2 gleiche Steine in eine Rüstung einzufügen ? ",False],
	["Können sich Spieler aus verschiedenen Reichen küssen ? ",True],
	["Stehen beim Stallburschen vier Pferde ? ",False],
	["Kann ein Körper Krieger starker Körper einsetzen ? ",False],
	["Kann ein Krieger ein Exorzismusschwert tragen ? ",False],
	["Kann der Nahkampfninja Tarnung benutzen ? ",True],
	["Kann ein Ninja drei Waffenklassen benutzen ? ",True],
	["Kann ein Sura eine Roteisenklinge tragen ? ",False],
	["Hat ein Sura Waffen, die nur er nutzen kann ? ",True],
	["Kann der Schamane mit einem Schwert kämpfen ? ",False],
	["Kann eine Heilschamanin Hilfe des Drachen anwenden ? ",False],
	["Fragen euch Gamemaster nach euren Accountdaten ? ",False],
	["Hat der Oberork drei Köpfe ? ",False],
	["Kann man den Metin der Schwärze auf Map 1 finden ? ",True],
	["Braucht man eine Emotionsmaske um zu tanzen ? ",False],
	["Kann der alte Mann wahrsagen ? ",False],
	["Macht der Schmied als einziger Dinge kaputt ? ",False],
	["Sammelt der Biologe Blumen ? ",False],
	["Kann man bei der Gemischtwarenhändlerin einen Blumenstrauß kaufen ? ",False],
	["Kann man mit Level 35 eine Gilde gründen ? ",False],
	["Hat man durch die Hochzeit Vorteile ? ",True],
	["Gibt es drei verschiedene Reiche ? ",True],
	["Können bis zu 8 Leute in eine Gruppe ? ",True],
	["Regnet es in Kimiko ? ",False],
	["Kann man Haarfärbemittel angeln ? ",True],
	["Hat der Dämonen Turm 8 Ebenen? ",False],
	["Gibt es Kimiko in mehreren Sprachen ? ",False],
	["Kann man während einer Hochzeit die Emotionen frei benutzen ? ",True], 
	["Lebt die Schildkröte im Feuerland ? ",False],
	["Kann man mit 8 Gildenmitgliedern einen Gildenkrieg starten ? ",True],
	["Ist Aranyo die Frau von Soon ? ",True],
	["Kann man Perlen abbauen ? ",False],
	["Kann man Perlen angeln ? ",False],
	["Verkauft die Gemischtwarenhändlerin lila Tränke ? ",False],
	["Bekommt man den Verlobungsring von der alten Frau ? ",True],
	["Gibt es in jedem Reich zwei Marktplätze ? ",True], 
	["Ist es möglich mit Level 15 schon zu reiten ? ",True],
	["Kann man Gildenfertigkeiten nur im Krieg nutzen ? ",True],
	["Kann man Rangpunkte verlieren ? ",True],
	["Ist Soon ein Bücherwurm ? ",True],
	["Kann man in die antike Glocke drei Steine einbringen ? ",True],
	["Bekommt man den Anzug vom fahrenden Händler ? ",False],
	["Kann man mit Level 25 heiraten ? ",True],  
	["Gibt es ein Schlangenschild?",False],
	["Kann ein Sura ein Azuranzug tragen?",False],
	["Gibt es eine Dämonenklinge?",True],
	["Kratzen sich Wildhunde hinter den Ohren?",True],
	["Gibt der Wächter des Dorfplatzes Tipps?",True],
	["Gibt es in jeder Map einen Teleporter?",True],
	["Hat der Spinnendungeon 2 eine Levelbeschränkung?",False],
	["Gibt es im Dämoneturm einen Alchimisten?",False],
	["Droppt der Brutale Spezialist Karotten?",False],
	["Endet der Dämoneturm nach dem Schmied?",False],
	["Hat ein Magiesura Verzauberte Klinge?",False],
	["Kann ein Waffenmagie Sura Feuer beschwören?",False],
	["Gibt es einen Stein der Hässlichkeit?",False],
	["Gibt es +9 Stein?",False],
	["Leben Verfluchte Tiere im Gildenland?",True],
	["Gibt es in Kimiko Hafer?",False],
	["Kommen aus dem Metin der Schlacht Weiße Tiger?",False],
	["Kommen aus dem Metin der Schlacht Tiger?",True],
	["Kann man mit Level 40 ein Barbarenschwert tragen?",True],
	["Können Krieger Speere tragen?",True],
	["Können Schamanen Speere tragen?",False],
	["Kann man in Kimiko fliegen?",False],
	["Gibt es einen Lehrer für Feuer Magie?",False],
	["Gibt es einen blauen Drachen?",False],
	["Trägt der Schlachterverwalter einen Bogen?",True],
	["Sind die Augen der alten Frau geöffnet?",False],
	["Gibt es einen Metin der Schande?",False],
	["Kann die Alte Frau Wahrsagen?",True],
	["Kommen aus dem Metin des Kummers Tiger?",False],
	["Findet man den Metin des Todes im ersten Dorf?",False],
	["Gibt es eine Oase in Kimiko?",True],
	["Haben die Wüstenbanditen eine blaue Robe an?",True],
	["Hat Bera zwei Begleiter?",True],
	["Kämpft der Gelbe Tigergeist alleine?",True],
	["Gibt es Schatztruhen in Kimiko?",False],
	["Gibt es Kupferschlüssel?",False],
	["Gibt es Kimiko Verzaubertes Eis?",True],
	["Ist der Biologe Weiblich?",False],
	["Gibt es Schneebälle in Kimiko?",False],
	["Kann man mit Mais angeln?",False],
	["Kann man beim Schmied einen Keuschheitsgürtel herstellen?",False],
	["Haben die Alpha Wölfe Weiße Streifen?",True],
	["Hat der Betrunke Bürger ein Bier in der Hand?",False],
	["Kann man die Helme in Kimiko sehen?",False],
	["Kann man Kimiko im Fenstermodus spielen?",True],
	["Kann man die Lautstärke von Kimiko anpassen?",True],
	["Kann man in Kimiko Musik hören?",True],
	["Kann man in Kimiko eigene Musik hören?",True],
	["Kann man in Kimiko Kinder bekommen?",False],
	["Kann man in Kimiko eine Familie gründen?",True],
	["Kann man in Kimiko küssen?",True],
	["Ist der Flammenlord der Boss im Feuerland?",False],
	["Gibt es einen Flammenkönig?",True],
	["Kann man Schmuck in Kimiko erbeuten?",True],
	["Kann ein Ninja stehlen?",False],
	["Kann man sein Reich wechseln?",True],
	["Gibt es eine ItemMall?",False],
	["Kann man aus Wolfskrallen eine Kette machen?",False],
	["Tragen die Arahane Helme?",True],
	["Tragen die Fanatiker eine Fliege?",False],
	["Stehen bei Octavio 10 Flaschen auf dem Tisch?",False],
	["Gibt es einen Stein der Weißen?",False],
	["Gibt es einen Stadtwächter?",True],
	["Gibt es einen Dorfwächter?",False],
	["Ist Yu-Hwan ein Spion?",True],
	["Ist Koe-Pung ein NPC in Kimiko?",True],
	["Droppen die Keiler Lehm?",False],
	["Droppen die Roten Keiler Pfirsichsamen?",False],
	["Tragen die Wilden Infanteristen einen Hut?",True],
	["Kann man in Kimiko schwimmen?",False],
	["Kann man in Kimiko springen?",False],
	["Hängen bei den Wölfen im laufen die Zungen raus?",False],
	["Hat der Wilde Ergebene 2 Krallen?",False],
	["Hat die Kriegerin am Arm Tatoos?",True],
	["Tragen die Schwarzwindsoldaten ein Beil?",True],
	["Gibt es einen Straußenflügel Fächer?",False],
	["Gibt es einen Zwergenpanzer?",False],
	["Gibt es Zwerge in Kimiko?",False],
	["Kann man ein Haustier halten?",True],
	["Kann man seine Lehre vergessen?",True],
	["Ist die Aura des Schwertes Rot?",False],
	["Gibt es einen Manaschild?",False],
	["Gibt es Jahrtausendpanzer?",False],
	["Gibt es eine Turmuhr?",False],
	["Gibt es Bogenschützen als Monster?",True],
	["Wird bei der Hochzeit ein Lied gespielt?",True],
	["Kann man es auf der Hochzeit regnen lassen?",False],
	["Hat Yung Rang in ihrem Korb Kuchen?",False],
	["Bewegen sich die Blätter der Bäume?",False],
	["Gibt es Grünzeug im Flammenland?",False],
	["Gibt es im Flammenland Magisches Eis?",False],
	["Haben die Flammen 4 Füße?",True],
	["Gibt es einen Teleporter zum Dämonenturm?",False],
	["Trägt eine Schamanin auch schwarze Unterwäsche?",True],
	["Können Gleiche Geschlechter heiraten?",True],
	["Zeigen die Buhmänner ihre Zähne?",True],
	["Haben Eisinsekten 5 Eiszapfen auf dem Rücken?",True],
	["Haben Eislöwen 5 Eiszapfen auf dem Rücken?",False],
	["Haben Eislöwen 4 Eiszapfen auf dem Rücken?",True],
	["Stehen neben dem Eingang von Nemere 2 Zelte?",True],
	["Sind es 971 Steinstufen auf dem direkten Weg durch den Tempel zum DT?",True],
	["Sind es 972 Steinstufen auf dem direkten Weg durch den Tempel zum DT?",False],
	["Sind es 970 Steinstufen auf dem direkten Weg durch den Tempel zum DT?",False],
	["Sind es 969 Steinstufen auf dem direkten Weg durch den Tempel zum DT?",False],
	["Sind es 973 Steinstufen auf dem direkten Weg durch den Tempel zum DT?",False],
	["Sind es 974 Steinstufen auf dem direkten Weg durch den Tempel zum DT?",False],
	["Sind es 975 Steinstufen auf dem direkten Weg durch den Tempel zum DT?",False],
	["Sind es 978 Steinstufen auf dem direkten Weg durch den Tempel zum DT?",False],
	["Sind es 966 Steinstufen auf dem direkten Weg durch den Tempel zum DT?",False],
	["Sind es 989 Steinstufen auf dem direkten Weg durch den Tempel zum DT?",False],
	["Gibt es auf Map1 ein Fass in dem 2 Speere stehen?",True],
	["Stehen auf den Tischen bei der alten Frau im Roten Reich insgesamt 16 Vasen?",True],
	["Stehen auf den Tischen bei der alten Frau im Roten Reich insgesamt 18 Vasen?",False],
	["Hat der Crafingschmied einen Meißel und einen Hammer in der Hand?",False],
	["Schreit das Baby auf Ah-Yu´s Rücken?",True],
	["Hat der Stadtwächter einen grauen Bart?",True],
	["Hat der Stadtwächter einen Braunen Bart?",False],
	["Hat Baek-Go eine Brille auf?",True],
	["Hat Baek-Go keine Brille auf?",False],
	["Hat Hong-Hae ein Rotes Haarband?",True],
	["Hat der Teleporter einen Leberfleck auf der Stirn?",True],
	["Hat das Infinitum Schwert +1 einen Angriffswert von 142-182?",True],
	["Hat das Infinitum Schwert +1 einen Angriffswert von 132-172?",False],
	["Hat das Infinitum Schwert +3 einen Angriffswert von 146-186?",True],
	["Hat das Infinitum Schwert +3 einen Angriffswert von 156-196?",False],
	["Hat das Auxilium Schwert +5 einen Angriffswert von 190-230?",True],
	["Hat das Auxilium Schwert +5 einen Angriffswert von 180-220?",False],
	["Hat das Auxilium Schwert +8 einen Angriffswert von 196-236?",True],
	["Hat das Auxilium Schwert +8 einen Angriffswert von 206-246?",False],
	["Hat das Damnum Schwert +3 einen Angriffswert von 206-246?",True],
	["Hat das Damnum Schwert +3 einen Angriffswert von 216-256?",False],
	["Hat das Damnum Schwert +5 einen Angriffswert von 210-250?",True],
	["Hat das Damnum Schwert +5 einen Angriffswert von 200-240?",False],
	["Hat das Honoris Schwert +4 einen Angriffswert von 248-288?",True],
	["Hat das Honoris Schwert +4 einen Angriffswert von 258-298?",False],
	["Hat das Honoris Schwert +6 einen Angriffswert von 252-292?",True],
	["Hat das Honoris Schwert +6 einen Angriffswert von 242-282?",False],
	["Hat das Rubin Schwert +7 einen Angriffswert von 294-334?",True],
	["Hat das Rubin Schwert +7 einen Angriffswert von 296-336?",False],
	["Hat die Magnetische Klinge +2 einen Angriffswert von 164-204?",True],
	["Hat die Magnetische Klinge +2 einen Angriffswert von 154-194?",False],
	["Hat die Magnetische Klinge +4 einen Angriffswert von 168-208?",True],
	["Hat die Magnetische Klinge +4 einen Angriffswert von 178-218?",False],
	["Hat der Terranen Spalter +0 einen Angriffswert von 220-260?",True],
	["Hat der Terranen Spalter +0 einen Angriffswert von 210-250?",False],
	["Hat der Terranen Spalter +9 einen Angriffswert von 238-278?",True],
	["Hat der Terranen Spalter +9 eienn Angriffswert von 240-280?",False],
	["Hat der Somnium Spalter +3 einen Angriffswert von 286-326?",True],
	["Hat der Somnium Spalter +3 einen Angriffswert von 276-316?",False],
	["Hat der Somnium Spalter +8 einen Angriffswert von 296-336?",True],
	["Hat der Somnium Spalter +8 einen Angriffswert von 306-346?",False],
	["Hat der Credo Spalter +5 einen Angrifswert von 330-370?",True],
	["Hat der Credo Spalter +5 einen Angriffswert von340-380?",False],
	["Hat der Credo Spalter +7 einen Angriffswert von 334-374?",True],
	["Hat der Credo Spalter +7 einen Angriffswert von 330-340?",False],
	["Hat der Damnum Spalter +6 einen Angriffswert von 272-312?",True],
	["Hat der Damnum Spalter +6 einen Angriffswert von 262-302?",False],
	["Hat der Damnum Spalter +8 einen Angriffswert von 276-316?",True],
	["Hat der Damnum Spalter +8 einen Angriffswert von 286-326?",False],
	["Hat das Teufelsflügel-Chakram +5 einen Angriffswert von 84-100?",True],
	["Hat das Teufelsflügel-Chakram +5 einen Angriffswert von 94-110?",False],
	["Hat das Teufelsflügel-Chakram +7 einen Angriffswert von 88-104?",True],
	["Hat das Teufelsflügel-Chakram +7 einen Angriffswert von 98-114?",False],
	["Haben die Auxilium Dolche +5 einen Angriffswert von 144-160?",True],
	["Haben die Auxilium Dolche +5 einen Angriffswert von 134-150?",False],
	["Haben die Auxilium Dolche +9 einen Angriffswert von 152-168?",True],
	["Haben die Auxilium Dolche +9 einen Angriffswert von 155-171?",False],
	["Haben die Somnium Dolche +3 einen Angriffswert von 180-196?",True],
	["Haben die Somnium Dolche +3 einen Angriffswert von 172-188?",False],
	["Haben die Somnium Dolche +4 einen Angriffswert von 182-198?",True],
	["Haben die Somnium Dolche +4 einen Angriffswert von 170-186?",False],
	["Haben die Terranen Dolche +6 einen Angriffswert von 126-142?",True],
	["Haben die Terranen Dolche +6 einen Angriffswert von 136-152?",False],
	["Haben die Terranen Dolche +8 einen Angriffswert von 130-146?",True],
	["Haben die Terranen Dolche +8 einen Angriffswert von 120-136?",False],
	["Haben die Honoris Dolche +2 einen Angriffswert von 198-214?",True],
	["Haben die Honoris Dolche +2 einen Angriffswert von 208-224?",False],
	["Haben die Honoris Dolche +8 einen Angriffswert von 210-226?",True],
	["Haben die Honoris Dolche +8 einen Angriffswert von 200-216?",False],
	["Hat die Infinitum Glocke +7 einen Angriffswert von 204-234?",True],
	["Hat die Infinitum Glocke +7 einen Angriffswert von 214-244?",False],
	["Hat die Infinitum Glocke +8 einen Angriffswert von 206-236?",True],
	["Hat die Infinitum Glocke +8 einen Angriffswert von 196-126?",False],
	["Hat der Damnum Stab +4 einen Angriffswert von 258-288?",True],
	["Hat der Damnum Stab +4 einen Angriffswert von 268-298?",False],
	["Hat der Damnum Stab +6 einen Angriffswert von 262-292?",True],
	["Hat der Damnum Stab +6 einen Angriffswert von 272-302?",False],
	["Hat der Honoris Stab +9 einen Angriffswert von 308-338?",True],
	["Hat der Honoris Stab +9 einen Angriffswert von 318-348?",False],
	["Hat der Honoris Stab +8 einen Angriffswert von 306-336?",True],
	["Hat der Honoris Stab +8 einen Angriffswert von 296-326?",False],
	["Hat die Credo Glocke +3 einen Angriffswert von 316-346?",True],
	["Hat die Credo Glocke +3 einen Angriffswert von 326-356?",False],
	["Hat die Credo Glocke +5 einen Angriffswert von 320-350?",True],
	["Hat die Credo Glocke +5 einen Angriffswert von 340-370?",False],
	["Hat die Rubinrüstung +6 42% Stark gegen Monster?",True],
	["Hat die Rubinrüstung +6 40% Stark gegen Monster?",False],
	["Hat die Rubinkleidung +4 40% Stark gegen Monster?",True],
	["Hat die Rubinkleidung +4 39% Stark gegen Monster?",False],
	["Hat das PVM Schild +7 4% Stark gegen Bosse?",True],
	["Hat das PVM Schild +7 6% Stark gegen Bosse?",False],
	["Hat das Citrinschild +6 8% Stark gegen Bosse?",True],
	["Hat das Citrinschild +6 10% Stark gegen Bosse?",False],
	["Haben die Kimiko Schuhe +2 2% Stark gegen Halbmenschen?",True],
	["Haben die Kimiko Schuhe +2 3% Stark gegen Halbmenschen?",False],
	["Haben die Rubinschuhe +3 8% Stark gegen Razador?",True],
	["Haben die Rubinschuhe +3 6% Stark gegen Razador?",False],
	["Hat das Kimiko Armband +4 den Bonus +5 Angriffswert?",True],
	["Hat das Kimiko Armband +4 den Bonus +6 Angriffswert?",False],
	["Hat das Citrinarmband +5 den Bonus +16 Angriffswert?",True],
	["Hat das Citrinarmband +5 den Bonus +15 Angriffswert?",False],
	["Hat die Rubinhalskette +2 6% Stark gegen Nemere?",True],
	["Hat die Rubinhalskette +2 5% Stark gegen Nemere?",False],
	["Hat die Citrinhalskette +2 24% Zaubergeschwindigkeit?",True],
	["Hat die Citrinhalskette +2 25% Zaubergeschwindigkeit?",False],
	["Haben die Rubinohrringe +2 23% Stark gegen Untote?",True],
	["Haben die Rubinohrringe +2 25% Stark gegen Untote?",False],
	["Haben die Kimiko Ohrringe +3 4% Stark gegen Untote?",True],
	["Haben die Kimiko Ohrringe +3 5% Stark gegen Untote?",False],
	["Hat der Rubinhelm +6 17% Stark gegen Bosse?",True],
	["Hat der Rubinhelm +6 18% Stark gegen Bosse?",False],
	["Hat der Citrinhelm +7 9% Stark gegen Bosse?",True],
	["Hat der Citrinhelm +7 8% Stark gegen Bosse?",False],
	["Hat das Tritonschwert +6 einen Angriffswert von 132 bis 172?",True],
	["Hat das Tritonschwert +6 einen Angriffswert von 142 bis 182",False],
	["Hat das Imperiums Schwert +7 einen Angriffswert von 174 bis 214?",True],
	["Hat das Imperiums Schwert +7 einen Angriffswert von 184 bis 224?",False],
	["Hat das Tenebris Schwert +8 einen Angriffswert von 196 bis 236?",True],
	["Hat das Tenebris Schwert +8 einen Angriffswert von 186 bis 226?",False],
	["Hat das Quantum Schwert +9 einen Angriffswert von 238 bis 278?",True],
	["Hat das Quantum Schwert +9 einen Angriffswert von 228 bis 268?",False],
	["Hat das Lapis Schwert +7 einen Angriffswert von 254 bis 294?",True],
	["Hat das Lapis Schwert +7 einen Angriffswert von 244 bis 284?",False],
	["Hat die Halbmenschenklinge +2 einen Angriffswert von 234 bis 274?",True],
	["Hat die Halbmenschenklinge +2 einen Angriffswert von 224 bis 264?",False],
	["Hat der Bellum Spalter +3 einen Angriffswert von 256 bis 296?",True],
	["Hat der Bellum Spalter +3 einen Angriffswert von 266 bis 306?",False],
	["Hat der Tenebris Spalter +4 einen Angriffswert von 298 bis 338?",True],
	["Hat der Tenebris Spalter +4 einen Angriffswert von 308 bis 348?",False],
	["Hat der Venenum Spalter +3 einen Angriffswert von 316 bis 356?",True],
	["Hat der Venenum Spalter +3 einen Angriffswert von 326 bis 366?",False],
	["Hat der Saphir Spalter +6 einen Angriffswert von 402 bis 442?",True],
	["Hat der Saphir Spalter +6 einen Angriffswert von 392 bis 432?",False],
	["Haben die Drachenmesser +3 einen Angriffswert von 60 bis 76?",True],
	["Haben die Drachenmesser +3 einen Angriffswert von 50 bis 66?",False],
	["Haben die Bellum Dolche +4 einen Angriffswert von 102 bis 118?",True],
	["Haben die Bellum Dolche +4 einen Angriffswert von 112 bis 128?",False],
	["Haben die Tenepris Dolche +3 einen Angriffswert von 140 bis 156?",True],
	["Haben die Tenepris Dolche +3 einen Angriffswert von 150 bis 166?",False],
	["Haben die Periculum Dolche +4 einen Angriffswert von 222 bis 238?",True],
	["Haben die Periculum Dolche +4 einen Angriffswert von 212 bis 228?",False],
	["Haben die Saphir Dolche +5 einen Angriffswert von 244 bis 260?",True],
	["Haben die Saphir Dolche +5 einen Angriffswert von 234 bis 250?",False],
	["Hat der Tenepris Bogen +5 einen Angriffswert von 270 bis 380?",True],
	["Hat der Tenepris Bogen +5 einen Angriffswert von 280 bis 390?",False],
	["Hat der Imperiums Bogen +3 einen Angriffswert von 246 bis 356?",True],
	["Hat der Imperiums Bogen +3 einen Angriffswert von 256 bis 366?",False],
	["Hat der Quantum Bogen +2 einen Angriffswert von 304 bis 414?",True],
	["Hat der Quantum Bogen +2 einen Angriffswert von 314 bis 424?",False],
	["Hat der Periculum Bogen +3 einen Angriffswert von 346 bis 456?",True],
	["Hat der Periculum Bogen +3 einen Angriffswert von 336 bis 446?",False],
	["Hat das Heilige Schwert +7 einen Magischen Angriffswert von 114 bis 134?",True],
	["Hat das Heilige Schwert +7 einen Magischen Angriffswert von 104 bis 124?",False],
	["Hat die Imperiums Klinge +7 einen Magischen Angriffswert von 154 bis 174?",True],
	["Hat die Imperiums Klinge +7 einen Magischen Angriffswert von 164 bis 184?",False],
	["Hat die Tenepris Klinge +6 einen Magischen Angriffswert von 172 bis 192?",True],
	["Hat die Tenepris Klinge +6 einen Magischen Angriffswert von 182 bis 202?",False],
	["Hat die Venenum Klinge +4 einen Magischen Angriffswert von 188 bis 208?",True],
	["Hat die Venenum Klinge +4 einen Magischen Angriffswert von 198 bis 218?",False],
	["Hat die Lapis Klinge +2 einen Magischen Angriffswert von 224 bis 244?",True],
	["Hat die Lapis Klinge +2 einen Magischen Angriffswert von 214 bis 234?",False],
	["Hat die Saphir Klinge +3 einen Magischen Angriffswert von 266 bis 286?",True],
	["Hat die Saphir Klinge +3 einen Magischen Angriffswert von 256 bis 276?",False],
	["Hat der Dämonenfächer +8 einen Magischen Angriffswert von 136 bis 156?",True],
	["Hat der Dämonenfächer +8 einen Magischen Angriffswert von 126 bis 146?",False],
	["Hat der Venenum Fächer +2 einen Magischen Angriffswert von 204 bis 224?",True],
	["Hat der Venenum Fächer +2 einen Magischen Angriffswert von 214 bis 234?",False],
	["Hat der Bellum Fächer +1 einen Magischen Angriffswert von 142 bis 162?",True],
	["Hat der Bellum Fächer +1 einen Magischen Angriffswert von 152 bis 172?",False],
	["Hat der Periculum Fächer +7 einen Magischen Angriffswert von 274 bis 294?",True],
	["Hat der Periculum Fächer +7 einen Magischen Angriffswert von 264 bis 284?",False],
	["Hat der Saphir Fächer +6 einen Magischen Angriffswert von 292 bis 312?",True],
	["Hat der Saphir Fächer +6 einen Magischen Angriffswert von 282 bis 302?",False],
	["Hat die Rubinrüstung +8 44% Stark gegen Monster?",True],
	["Hat die Rubinrüstung +8 42% Stark gegen Monster?",False],
	["Hat die Rubinkleidung +9 45% Stark gegen Monster?",True],
	["Hat die Rubinkleidung +9 40% Stark gegen Monster?",False],
	["Hat das PVM Schild +8 4% Stark gegen Bosse?",True],
	["Hat das PVM Schild +8 6% Stark gegen Bosse?",False],
	["Hat das Citrinschild +9 10% Stark gegen Bosse?",True],
	["Hat das Citrinschild +9 20% Stark gegen Bosse?",False],
	["Haben die Kimiko Schuhe +4 3% Stark gegen Halbmenschen?",True],
	["Haben die Kimiko Schuhe +4 5% Stark gegen Halbmenschen?",False],
	["Haben die Rubinschuhe +6 14% Stark gegen Razador?",True],
	["Haben die Rubinschuhe +6 15% Stark gegen Razador?",False],
	["Hat das Kimiko Armband +8 den Bonus +9 Angriffswert?",True],
	["Hat das Kimiko Armband +8 den Bonus +6 Angriffswert?",False],
	["Hat das Citrinarmband +9 den Bonus +20 Angriffswert?",True],
	["Hat das Citrinarmband +9 den Bonus +19 Angriffswert?",False],
	["Hat die Rubinhalskette +5 12% Stark gegen Nemere?",True],
	["Hat die Rubinhalskette +5 15% Stark gegen Nemere?",False],
	["Hat die Citrinhalskette +4 24% Zaubergeschwindigkeit?",True],
	["Hat die Citrinhalskette +4 25% Zaubergeschwindigkeit?",False],
	["Haben die Rubinohrringe +4 25% Stark gegen Untote?",True],
	["Haben die Rubinohrringe +4 26% Stark gegen Untote?",False],
	["Haben die Kimiko Ohrringe +6 7% Stark gegen Untote?",True],
	["Haben die Kimiko Ohrringe +6 5% Stark gegen Untote?",False],
	["Hat der Rubinhelm +8 19% Stark gegen Bosse?",True],
	["Hat der Rubinhelm +8 18% Stark gegen Bosse?",False],
	["Hat der Citrinhelm +9 10% Stark gegen Bosse?",True],
	["Hat der Citrinhelm +9 8% Stark gegen Bosse?",False],
	["Hat das Tritonschwert +8 einen Angriffswert von 136 bis 176?",True],
	["Hat das Tritonschwert +8 einen Angriffswert von 146 bis 186",False],
	["Hat das Imperiums Schwert +4 einen Angriffswert von 168 bis 208?",True],
	["Hat das Imperiums Schwert +4 einen Angriffswert von 178 bis 218?",False],
	["Hat das Tenebris Schwert +3 einen Angriffswert von 186 bis 226?",True],
	["Hat das Tenebris Schwert +3 einen Angriffswert von 176 bis 216?",False],
	["Hat das Quantum Schwert +2 einen Angriffswert von 224 bis 264?",True],
	["Hat das Quantum Schwert +2 einen Angriffswert von 214 bis 254?",False],
	["Hat das Lapis Schwert +1 einen Angriffswert von 242 bis 282?",True],
	["Hat das Lapis Schwert +1 einen Angriffswert von 232 bis 272?",False],
	["Hat die Halbmenschenklinge +4 einen Angriffswert von 238 bis 278?",True],
	["Hat die Halbmenschenklinge +4 einen Angriffswert von 228 bis 268?",False],
	["Hat der Bellum Spalter +6 einen Angriffswert von 262 bis 302?",True],
	["Hat der Bellum Spalter +6 einen Angriffswert von 272 bis 312?",False],
	["Hat der Tenebris Spalter +8 einen Angriffswert von 306 bis 346?",True],
	["Hat der Tenebris Spalter +8 einen Angriffswert von 316 bis 356?",False],
	["Hat der Venenum Spalter +5 einen Angriffswert von 320 bis 360?",True],
	["Hat der Venenum Spalter +5 einen Angriffswert von 330 bis 370?",False],
	["Hat der Saphir Spalter +8 einen Angriffswert von 406 bis 446?",True],
	["Hat der Saphir Spalter +8 einen Angriffswert von 396 bis 436?",False],
	["Haben die Drachenmesser +5 einen Angriffswert von 64 bis 80?",True],
	["Haben die Drachenmesser +5 einen Angriffswert von 54 bis 70?",False],
	["Haben die Bellum Dolche +8 einen Angriffswert von 110 bis 126?",True],
	["Haben die Bellum Dolche +8 einen Angriffswert von 112 bis 128?",False],
	["Haben die Tenepris Dolche +8 einen Angriffswert von 150 bis 166?",True],
	["Haben die Tenepris Dolche +8 einen Angriffswert von 160 bis 176?",False],
	["Haben die Periculum Dolche +9 einen Angriffswert von 232 bis 248?",True],
	["Haben die Periculum Dolche +9 einen Angriffswert von 222 bis 238?",False],
	["Haben die Saphir Dolche +8 einen Angriffswert von 250 bis 266?",True],
	["Haben die Saphir Dolche +8 einen Angriffswert von 240 bis 256?",False],
	["Hat der Tenepris Bogen +6 einen Angriffswert von 272 bis 382?",True],
	["Hat der Tenepris Bogen +6 einen Angriffswert von 282 bis 392?",False],
	["Hat der Imperiums Bogen +7 einen Angriffswert von 254 bis 364?",True],
	["Hat der Imperiums Bogen +7 einen Angriffswert von 256 bis 366?",False],
	["Hat der Quantum Bogen +9 einen Angriffswert von 318 bis 428?",True],
	["Hat der Quantum Bogen +9 einen Angriffswert von 314 bis 424?",False],
	["Hat der Periculum Bogen +5 einen Angriffswert von 350 bis 460?",True],
	["Hat der Periculum Bogen +5 einen Angriffswert von 336 bis 446?",False],
	["Hat das Heilige Schwert +9 einen Magischen Angriffswert von 184 bis 138?",True],
	["Hat das Heilige Schwert +9 einen Magischen Angriffswert von 108 bis 128?",False],
	["Hat die Imperiums Klinge +9 einen Magischen Angriffswert von 158 bis 178?",True],
	["Hat die Imperiums Klinge +9 einen Magischen Angriffswert von 168 bis 188?",False],
	["Hat die Tenepris Klinge +5 einen Magischen Angriffswert von 170 bis 190?",True],
	["Hat die Tenepris Klinge +5 einen Magischen Angriffswert von 180 bis 200?",False],
	["Hat die Venenum Klinge +6 einen Magischen Angriffswert von 192 bis 212?",True],
	["Hat die Venenum Klinge +6 einen Magischen Angriffswert von 202 bis 222?",False],
	["Hat die Lapis Klinge +8 einen Magischen Angriffswert von 236 bis 256?",True],
	["Hat die Lapis Klinge +8 einen Magischen Angriffswert von 244 bis 266?",False],
	["Hat die Saphir Klinge +1 einen Magischen Angriffswert von 262 bis 282?",True],
	["Hat die Saphir Klinge +1 einen Magischen Angriffswert von 252 bis 272?",False],
	["Hat der Dämonenfächer +6 einen Magischen Angriffswert von 132 bis 152?",True],
	["Hat der Dämonenfächer +6 einen Magischen Angriffswert von 122 bis 142?",False],
	["Hat der Venenum Fächer +4 einen Magischen Angriffswert von 208 bis 228?",True],
	["Hat der Venenum Fächer +4 einen Magischen Angriffswert von 218 bis 238?",False],
	["Hat der Bellum Fächer +3 einen Magischen Angriffswert von 146 bis 166?",True],
	["Hat der Bellum Fächer +3 einen Magischen Angriffswert von 156 bis 176?",False],
	["Hat der Periculum Fächer +5 einen Magischen Angriffswert von 270 bis 290?",True],
	["Hat der Periculum Fächer +5 einen Magischen Angriffswert von 260 bis 280?",False],
	["Hat der Saphir Fächer +9 einen Magischen Angriffswert von 298 bis 318?",True],
	["Hat der Saphir Fächer +9 einen Magischen Angriffswert von 288 bis 308?",False]
]

class OXBoard(ui.ScriptWindow):
	
	Points 	= 0 
	Time	= 0
	Round	= 0
	Q_List	= {}
	Q_Index	= 0
	Active	= 0
	
	isCheck = False
	
	QuestIndex = 0
	
	GetOut	= 0
	QuestionCount = 0
	
	FullRoundTime = 0
	# StandartPointAdd 	= 0 # <- Muss von Server kontrolliert werden!
	StandartTimer	= 6 
	maxQuestions 	= 30
	
	
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LoadUI()

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		self.Board.Hide()
			
	def Destroy(self):
		self.__del__()
	
			
	def LoadUI(self):
		self.Board = ui.BoardWithTitleBar()
		self.Board.SetSize(330, 180)
		self.Board.SetPosition(wndMgr.GetScreenWidth()/2-165,wndMgr.GetScreenHeight()-wndMgr.GetScreenHeight()+100)
		# self.Board.AddFlag("movable")
		self.Board.AddFlag("float")
		self.Board.SetTitleName("OX-Wettbewerb") # - [ Runde 1 / 50 ]")
		self.Board.SetCloseEvent(self.__GiveUP)
		self.Board.Hide()
		
		self.OXBG = ui.Bar()
		self.OXBG.SetParent(self.Board)
		self.OXBG.SetPosition(15,35)
		self.OXBG.SetSize(300,130)
		self.OXBG.SetColor(grp.GenerateColor(0.0, 0.0, 0.0, 0.5))
		self.OXBG.Show()
		
		self.MainDialog = ui.TextLine()
		self.MainDialog.SetParent(self.Board)
		self.MainDialog.SetPosition(165,50)
		self.MainDialog.SetText("- Dies ist eine Frage? Ist das so? -")
		self.MainDialog.SetHorizontalAlignCenter()
		self.MainDialog.SetFontColor(0.9607, 0.2392, 0.0)
		self.MainDialog.Show()
	
		self.MainTimerDialog = ui.TextLine()
		self.MainTimerDialog.SetParent(self.Board)
		self.MainTimerDialog.SetPosition(165,65)
		self.MainTimerDialog.SetText("Du hast noch 00:34 Sekunden!")
		self.MainTimerDialog.SetHorizontalAlignCenter()
		self.MainTimerDialog.Show()
		
		self.GiveUPButton = ui.Button()
		self.GiveUPButton.SetParent(self.Board)
		self.GiveUPButton.SetPosition(121,95)
		self.GiveUPButton.SetText("")
		self.GiveUPButton.SetUpVisual("d:/ymir work/ui/public/Large_Button_01.sub")
		self.GiveUPButton.SetOverVisual("d:/ymir work/ui/public/Large_Button_02.sub")
		self.GiveUPButton.SetDownVisual("d:/ymir work/ui/public/Large_Button_03.sub")
		self.GiveUPButton.SetEvent(self.__GiveUP)
		self.GiveUPButton.Show()

		self.GiveUPButtonTextLine = ui.TextLine()
		self.GiveUPButtonTextLine.SetParent(self.Board)
		self.GiveUPButtonTextLine.SetPosition(165,98)
		self.GiveUPButtonTextLine.SetText("Aufgeben")
		self.GiveUPButtonTextLine.SetHorizontalAlignCenter()
		self.GiveUPButtonTextLine.Show()
		
		self.MainPointsDialog = ui.TextLine()
		self.MainPointsDialog.SetParent(self.Board)
		self.MainPointsDialog.SetPosition(165,120)
		self.MainPointsDialog.SetText("[ Punkte: 0 ]")
		self.MainPointsDialog.SetHorizontalAlignCenter()
		self.MainPointsDialog.Show()
		
		self.itemBuyQuestionDialog = None
		
		# self.GAME_Init()
		# self.GAME_Points(10)
		# self.GAME_Points(10)
		# self.GAME_Points(10)
	
	def GAME_Init(self):
		self.Q_List	= {}
		self.Active = 1
		self.Board.Show()
		
		self.QuestionCount = len(QUESTIONS)
		# self.SetRound()
		
		self.MainDialog.SetText("- Warte auf Frage... -")
		self.isWait = True
		self.GAME_StartTimer()
		
	def GAME_SetLUAQuestIndex(self,qid):
		self.QuestIndex = int(qid)
	
	def GAME_Answer(self,answer):
		if answer == "o":
			if QUESTIONS[self.Q_Index][1] == True:
				self.GAME_Success()
				# self.SetRound()
				self.MainDialog.SetText("- Warte auf nächste Frage... -")
				self.isWait = True
				self.isCheck = False
				self.GAME_StartTimer()				
			else:
				self.GAME_Fail()
			
			
		elif answer == "x":
			if QUESTIONS[self.Q_Index][1] == False:
				self.GAME_Success()
				# self.SetRound()
				self.MainDialog.SetText("- Warte auf nächste Frage... -")
				self.isWait = True
				self.isCheck = False
				self.GAME_StartTimer()				
			else:
				self.GAME_Fail()
				
		elif answer == "m":
			self.GAME_Fail()
			
	def GAME_Points(self,points):
		# self.Points = self.Points + points
		self.Points = self.Points + int(points)
		self.MainPointsDialog.SetText("[ Punkte: " + str(self.Points) + " ]")
		
	def GAME_StartTimer(self):
		if self.isWait:
			self.Time = app.GetGlobalTimeStamp() + 5
		else:
			self.Time = app.GetGlobalTimeStamp() + self.StandartTimer
		self.UpdateTimer()
		
	# def GAME_SetQuestIndex(self):
	
	def __SetQuestion(self):
		# self.GAME_Fail()
		if len(self.Q_List) == self.maxQuestions:
			self.Board.Hide()
			self.Active = 0
			constInfo.INPUT_CMD = "getout#"
			event.QuestButtonClick(self.QuestIndex)			
		else:
			if len(QUESTIONS) == len(self.Q_List):
				self.MainDialog.SetText("~ Alle Fragen wurden beantwortet! ~")
				self.Time = 0
				self.UpdateTimer()
				self.SuperCheer()
			else:
			
			
				i = 0
				while i < 1:
					selQuestion = app.GetRandom(0,len(QUESTIONS))
					if selQuestion not in self.Q_List:
						i = 1
						self.Q_Index = selQuestion
						self.Q_List[len(self.Q_List)] = selQuestion
						self.MainDialog.SetText(QUESTIONS[selQuestion][0])
						return		
			
				# for i in xrange(len(QUESTIONS)):
					# if i not in self.Q_List:
						# self.Q_Index = i
						# self.Q_List[len(self.Q_List)] = i
						# self.MainDialog.SetText(QUESTIONS[i][0])
						# return
						
				self.MainDialog.SetText("~ Es wurde keine Frage gefunden! ~")
		
	def GAME_Time(self,time):
		self.FullRoundTime = time
		
	def UpdateTimer(self):
		timeLeft = self.Time - app.GetGlobalTimeStamp()
		if timeLeft <= 0:
			self.MainTimerDialog.SetText("")
		
		else:
			timeString = "Minuten"
			if timeLeft < 60:
				timeString = "Sekunden"
			
			if self.isWait:
				self.MainTimerDialog.SetText("Nächste Frage in " + str(self.FormatTime(timeLeft)) + " " + timeString + "!")
			else:
				self.MainTimerDialog.SetText("Du hast noch " + str(self.FormatTime(timeLeft)) + " " + timeString + "!")


	def FormatTime(self, time):
		m, s = divmod(time, 60)
		h, m = divmod(m, 60)
		return "%d:%02d:%02d" % (h, m, s)
		
	def SetRound(self):
		self.Round = self.Round + 1
		self.Board.SetTitleName("OX-Wettbewerb - [ Runde " + str(self.Round) + " / " + str(self.QuestionCount) + " ]")
		
	def GAME_OnUpdate(self):
		
		if self.Active == 1:
			if self.FullRoundTime < app.GetGlobalTimeStamp():
				self.Board.Hide()
				self.Active = 0
				constInfo.INPUT_CMD = "roundend#"
				event.QuestButtonClick(self.QuestIndex)			
			
			else:
				if self.GetOut > 0:
					if self.GetOut < app.GetGlobalTimeStamp():
						self.Board.Hide()
						self.Active = 0
						constInfo.INPUT_CMD = "getout#"
						event.QuestButtonClick(self.QuestIndex)
				
				else:
					if self.isWait:
						self.UpdateTimer()
						if self.Time < app.GetGlobalTimeStamp():
							self.isWait = False
							self.__SetQuestion()
							self.GAME_StartTimer()
					else:
						self.UpdateTimer()
						if self.Time < app.GetGlobalTimeStamp():
							if not self.isCheck:
								self.isCheck = True
								constInfo.INPUT_CMD = "check#"
								event.QuestButtonClick(self.QuestIndex)
						

		
		# else:
		
	def GAME_Success(self):
		constInfo.INPUT_CMD = "success#"
		event.QuestButtonClick(self.QuestIndex)
		self.Cheer()
		
	def GAME_Fail(self):
		self.Fail()
		self.Board.Hide()
		self.GetOut = app.GetGlobalTimeStamp() + 3
		
		
	def SuperCheer(self):
		GFHhg54GHGhh45GHGH.SendChatPacket("/cheerup")
		self.GetOut = app.GetGlobalTimeStamp() + 5
		
	def Cheer(self):
		GFHhg54GHGhh45GHGH.SendChatPacket("/cheer1")
	
	
	def Fail(self):
		GFHhg54GHGhh45GHGH.SendChatPacket("/sad")
		
		
	def __GiveUP(self):
		itemBuyQuestionDialog = uiCommon.QuestionDialog()
		itemBuyQuestionDialog.SetText("Bist du sicher, das du jetzt aufgeben willst?")
		itemBuyQuestionDialog.SetAcceptEvent(lambda arg=True: self.RequestGiveUp(arg))
		itemBuyQuestionDialog.SetCancelEvent(lambda arg=False: self.RequestGiveUp(arg))
		itemBuyQuestionDialog.Open()
		self.itemBuyQuestionDialog = itemBuyQuestionDialog

	def RequestGiveUp(self,answer):
		if not self.itemBuyQuestionDialog:
			return	
	
		if answer:	
			self.Board.Hide()
			constInfo.INPUT_CMD = "getout#"
			event.QuestButtonClick(self.QuestIndex)
		
			
		self.itemBuyQuestionDialog.Close()
		self.itemBuyQuestionDialog = None	
		