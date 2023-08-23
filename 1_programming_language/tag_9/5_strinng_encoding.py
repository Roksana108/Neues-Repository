""" 
unicode codepoints eingeben
"""
print("\u0041")  # 16 bit Darstellung
print("\U0001F40D")  # 32 bit Darstellung
x = "\U0001F40D"
print(len(x))
print(len(bytes(x, encoding="utf-8")))

# zusammengesetztes Zeichen:
spock = "\U0001F596\U0001F3FB"
print(spock)

#  CRDL Character Resorvoir Description Language
print("\N{GOTHIC LETTER AHSA}")

print("\U0001F1E9\U0001F1F0")  # flag of denmark

# Aus Frau zero und Rocket einen weiblichen Astronaut zusammenbauen
frau = "\U0001F469"
zero = "\u200d"
rocket = "\U0001F680"
astro = "\U0001F469\u200d\U0001F680"
print(frau)
print(zero)
print(rocket)
print(astro)  # weiblicher Astronaut
print("astro len:", len(bytes(astro, encoding="utf-8")))

if "а" == "a":
    print("die Zeichen sind gleich")
else:
    print("die beiden a sind unterschliedlich!")