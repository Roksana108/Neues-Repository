"""
CSV-Reader
"""

import csv
from pathlib import Path


# klassischer CSV-READER
with open(Path(__file__).parent / "data.csv") as f:
    reader = csv.reader(f, delimiter=",")
    print(reader)     # ein Iterator über eine CVS-Datei
    #  print(next(reader)) ['12','2','3','4']
    #  print(next(reader)) ['hamburg', 'berlin, tiergarden','dresden','leipzig']
    #  print(next(reader))
    header = next(reader)
    print("Header:", header)

    for row in reader:
        print(row)

# nur anwenden, wenn ein Header vorhanden ist!
# Dict-Reader erstellt Dict. Erste Zeile ist der 
# jeweilige Key
with open(Path(__file__).parent / "data.csv") as f:
    reader = csv.DictReader(f, delimiter=",")
    for row in reader:
        print(row)