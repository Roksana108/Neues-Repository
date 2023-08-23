"""
Schreibe ein Programm, welches über einen User-Input einen Planetennamen 
einliest und die Entfernung Sonne - Planet, Erde - Planet in die Ausgabe
printed. 

Falls ein unbekannter Planet eingegeben wird, soll das Programm 
den User darauf hinweisen.

Hinweis:
nutze if-else, print
wir gehen von validem Input aus
es reichen zwei Beispielplaneten mit Dummywerten aus

Beispiel
----------
Bitte gebe einen Planennamen ein: Erde 
Der Abstand des Planeten Erde zu Erde ist 0 km

Bitte gebe einen Planennamen ein: Merkur 
Der Abstand des Planeten Merkur zu Erde ist 100.000.000 km

Bitte gebe einen Planennamen ein: Melmac 
dieser Planet ist leider nicht bekannt.

"""

planet_name = input("Bitte gebe einen Planetennamen ein: ")
planet_name = planet_name.lower()

if planet_name == "merkur":
    print("Der Abstand Erde Merkur beträgt 100.000.000 km")
elif planet_name == "saturn":
    print("Der Abstand Erde Saturn beträgt 1.000.000.000 km")
else:
    print("dieser Planet ist unbekannt")
