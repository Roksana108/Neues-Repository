# Lese die Datei worldcities.csv mit dem CSV - Reader ein,
# sortiere die Einträge nach city_ascii und speichere sie in einer
# neuen Daten worldcities_sorted.csv ab.
# Schreibe dazu die Funktion load_cities, sort_cities_by_ascii_name und
# save_cities_to_file.

# 1.b) Länder-Filter
# Erweitere die Aufgabe um einen Länder-Filter: es sollen nur Einträge
# in die neue Datei kommen, die einem eingegebenen Land entsprechen (zb. India)

import csv
from pathlib import Path

with open(Path(__file__).parent / "worldcities.csv ") as f:
    reader = csv.reader(f, delimiter=",")
    print(reader)   


def load_cities():
    ...


def sort_cities_by_ascii_name():
    ...


def save_cities_to_file():
    ...


def main():
    load_cities()
    ...
