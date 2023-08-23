"""
Berechne den Bodymass Index Body-Mass-Index:

Der Body-Mass-Index (kurz: BMI) ist eine Zahl, mit der man abschätzen kann, 
ob man Unter-, Normal oder Übergewicht hat. Man berechnet diese Zahl nach der folgenden Formel:

          Gewicht(kg)
BMI = ---------------
       Größe(m) * Größe(m)

Dabei wird das Gewicht in kg und die Größe in m angegeben.
Runde auf zwei Nachkommastellen

über Input wird das Gewicht in Gramm eingegeben und die Höhe in cm:
"""
weight = int(input("Bitte das Gewicht in Gramm eingeben zb. 80000: "))
height = int(input("Bitte die Grösse in cm eingeben: zb. 180: "))

# Umrechnen der Werte in kg und m
weight_kg = weight / 1000
height_m = height / 100

# BMI ausrechnen
bmi = round(weight_kg / (height_m * height_m), 2)
print("BMI: ", bmi)
