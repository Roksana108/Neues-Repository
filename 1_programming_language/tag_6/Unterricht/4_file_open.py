""" 
Dateien öffnen mit Python
"""
from pathlib import Path
import os 

# Name / Pfad der aktuellen Datei, die ausgeführt wird.
print(__file__)   # Dunder (Double Under)

# aktuelles Arbeitsverzeichnis
print("aktuelles Arbeitsarbeitsverzeichnis: ", Path.cwd())

# Path-Objekt erzeugen
path_object = Path(__file__)  # absoluter Pfad
print("Path Objekt:", path_object)
print("Verzeichnis der Datei:", path_object.parent)


# mit os.chdir das aktuelle Arbeitsverzeichnis wechseln
# # open öffnet Datei auf der Harddisk
os.chdir(path_object.parent)
f = open("data.txt", mode="r", encoding="utf-8")
print(f)
f.close()

print("*" * 50)

# oder open direkt mit dem Pfad-Objekt
# mode=r => READ
f = open(Path(__file__).parent / "data.txt", mode="r", encoding="utf-8")
data = f.read()
print(data)
f.close()

# Besser mit Context-Manager lösen (dann wird f sicher geschlossen)
with open(Path(__file__).parent / "data.txt", mode="r", encoding="utf-8") as f:
    data = f.read()
    print(data)

