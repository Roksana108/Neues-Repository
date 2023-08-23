""" 
Eine Datei einlesen
"""
from pathlib import Path

# ganz einlesen mit read()
with open(Path(__file__).parent / "data.txt", mode="r", encoding="utf-8") as f:
    data = f.read()
    print(data)

# zeilenweise einlesen
with open(Path(__file__).parent / "data.txt", mode="r", encoding="utf-8") as f:
    data = f.readlines()
    print(data)

# Zeilen-Iterator
with open(Path(__file__).parent / "data.txt", mode="r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())