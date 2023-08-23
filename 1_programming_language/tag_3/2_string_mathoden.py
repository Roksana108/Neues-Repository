"""
Funktionen und String-Methoden

Funktionen: print("hello"), type(), len
"""

# --------------------------------------
# Länge eines Strings
# --------------------------------------
string = "abcdef"
#########[012345]
print("der String hat die Länge:", len(string))
print("das letzte Zeichen des Strings:", string[len(string) - 1])  # allg. Variante (f)
print("das letzte Zeichen des Strings:", string[-1])  # python (f)
 

# -----------------------------------------------------------------
# String Methoden (jede Stringmethode erzeugt einen neuen String)
# -----------------------------------------------------------------
s = "the Quick Brown Fox fox"
print("alles in Großbuchstaben", s.upper())

# -----------------------------------------------------------------
# Aufgabe
# Der User gibt einen Satz / Wort über input ein
# den eingegebenen Satz in Kleinbuchstaben wandeln
# Ergebnis ausdrucken
# Beispiel:
# Eingabe: Hallo Welt
# Ausgabe: hallo welt
# 5 Minuten zeit!
# -----------------------------------------------------------------
# s = input("Bitte gebe einen Satz ein: ")
# print(s.upper())

# s = input("Bitte gebe einen Satz ein: ").upper()
# print(s)

# -----------------------------------------------------------------
# replace: eine Zeichenkette in einem String ersetzen (string)
# -----------------------------------------------------------------
dog = s.replace("Fox", "Dog")
print(dog)

dirty_string = "##abc####234"
print(dirty_string.replace("#", ""))

# -----------------------------------------------------------------
# count: zählt Vorkommnisse in Strings (int)
# -----------------------------------------------------------------
s = "the Quick Brown Fox fox"
print("Das Wort Fox kommt in dem String so oft vor:", s.count("Fox"))
print("fox unabhängig von Großklein (caseinsensitive):", s.lower().count("fox"))


# -----------------------------------------------------------------
# count: zählt Vorkommnisse in Strings (bool)
# -----------------------------------------------------------------
country = "Andorra"
if country.startswith("An"):  # Rückgabewert ist ein bool
    print("Das Land beginnt mit An")

if country.endswith("a"):  # Rückgabewert ist ein bool
    print("Das Land endet mit a")

# -----------------------------------------------------------------
# strip: bereinigt einen String von Leer/Steuerzeichen am Anfang und Ende
# -----------------------------------------------------------------
dirty_string = "\thallo \n"
print(dirty_string.strip())

# -----------------------------------------------------------------
# Daten bereinigen mit strip und replace
# -----------------------------------------------------------------
dirty_string = "\nblabla\n \r\n blabla"
print(dirty_string.replace("\n", "").replace("\r", "").replace("  ", " ").strip())