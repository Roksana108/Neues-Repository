""" 
Tag 3: Strings I

Zeichenketten
"""

city = "Berlin"
print(type(city))  # city ist ein Objekt der Klasse String <class 'str'>

# per Index auf ein Zeichen zugreifen
# Zählung beginnt 0
print(city[0])  # B
print(city[5])  # n
# print(city[6])  # Index Error
print("einzelnes Zeichen: ", type(city[5]))

text = "hallo welt, peter sagte 'du bist cool'"  # einfache Anführungszeichen nutzen
text = "hallo welt, peter sagte \"du bist cool\""  # maskieren
text = 'hallo welt, peter sagte "du bist cool"'

# --------------------------------------
# Strings konkatenieren (concat)
# --------------------------------------
a = "AAA"
b = "BBB"
# zusammenfügen zu AAABBB (Additionsoperator wurde überladen)
c = a + b
print(c, type(c))

# --------------------------------------
# String mehrmals wiederholen (dazu Multiplikationsoperator nutzen)
# --------------------------------------
dash = "-"
# --------------------------------------
print(dash * 50)
print("#" * 50)

# --------------------------------------
# Zahlen in Strings konvertieren
# --------------------------------------
x = 1
x_string = str(x)
print(type(x), type(x_string), "Wert von x_string:", x_string)


# --------------------------------------
# String in Zahl konvertieren
# --------------------------------------
x = int(x_string)
print(type(x), type(x_string), "Wert von x:", x)