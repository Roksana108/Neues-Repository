""" 
Eine Datei schreiben
"""
from pathlib import Path

# ----------------------------------------------------------
# r+ => zum Lesen und Schreiben öffnen, Datei muss aber existieren
# ----------------------------------------------------------
text = "some more text."
file_name = "data2.txt"

with open(Path(__file__).parent / file_name, mode="r+", encoding="utf-8") as f:
    print("erste Zeile mit r+:", f.readline())
    f.write(text)
    f.seek(0)  # gehe zurück zu Byte 0
    print("*" * 30)
    print(f.read())