""" 
Eine Datei schreiben
"""
from pathlib import Path

# ----------------------------------------------------------
# 1. Fall: Die zu schreibende Datei existiert noch nicht
# modus w (write), überschreibt immer alles
# ----------------------------------------------------------
text = "das ist ein Text, den ich gerne in eine Datei schreiben würde."
file_name = "data2.txt"

# falls Datei nicht exisitert, wird sie mit mode=w angelegt (mode=w ist der Schreibmodus)
with open(Path(__file__).parent / file_name, mode="w", encoding="utf-8") as f:
    f.write(text)

# ----------------------------------------------------------
# 2. Fall: Die zu schreibende Datei existiert und wir wollen anhängen
# modus a (append), hängt an
# ----------------------------------------------------------
spaceships = ["Enterprise\n", "Discovery\n"]

file_name = "data3_append.txt"
# falls Datei nicht exisitert, wird sie mit mode=a angelegt (mode=a ist der Appendmodus)
with open(Path(__file__).parent / file_name, mode="a", encoding="utf-8") as f:
    f.write(text + "\n")
    f.writelines(spaceships)


# Lesen in Schreibmodus bei Append und Write geht NICHT!
with open(Path(__file__).parent / file_name, mode="a", encoding="utf-8") as f:
    # f.read() => würde einen IO Error auslösen
    ...


# Aus einer Datei lesen, in eine andere Schreiben
with open(Path(__file__).parent / file_name) as f1, open(Path(__file__).parent / "neu.txt", mode="w") as f2:
    content = f1.read()
    f2.write(content)
