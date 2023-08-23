"""
Gegegen ist die Datei prodcucts.csv mit drei Feldern
productid,name,date


Lese die Zeilen ein und versuche (try), das Feld date 
in ein Python-Dateobjekt zu parsen (datetime.strptime).
Manche Datefelder sind entweder leer oder kaputt, das Programm darf 
beim Konvertieren aber nicht abbrechen, soll diese Zeilen dann ignorieren.

Das Datum muss um zwei Tage nach vorne versetzt werden, dh. aus dem
18.10.2022 soll der 20.10.2022 werden. Das neue Datum erstetzt das alte Datum
in der Liste im selben Format (datetime, timedelta)

Die veränderte Liste soll dann auf Standard-Out ausgegeben werden, ein
abspeichern als CSV ist nicht nötig (Zusatzaufgabe.)

Kapsel die einzelnen Bereiche in Funktionen, nutze Typehints und 
Docstrings, wo nötig.
"""
import csv
from pathlib import Path
from datetime import datetime, timedelta

FILENAME = "products.csv"
