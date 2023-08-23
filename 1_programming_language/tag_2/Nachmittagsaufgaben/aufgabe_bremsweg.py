"""
Anhalteweg:

Es gibt folgende Faustformeln zur Berechnung von Anhaltewegen:

Reaktionsweg (in Metern) = (Geschwindigkeit (in km/h) geteilt durch 10) mal 3

Bremsweg (in Metern) = (Geschwindigkeit (in km/h) geteilt durch 10) mal (Geschwindigkeit (in km/h) geteilt durch 10)

Anhalteweg (in Metern) = Reaktionsweg plus Bremsweg

km/h über input eingeben. Gebe den Reaktionsweg, den Bremsweg und den Anhalteweg entsprechend der km/h aus. Hinweis: 124.4 ist ein gültiger Eingabewert.
"""
speed = float(input("Geschwindikeit km/h eingeben: "))

reaction_distance = (speed / 10) * 3
breaking_distance = (speed / 10) ** 2
stopping_distance = reaction_distance + breaking_distance

print("Bei einer Geschwindikeit von", speed, "km/h ist:")
print("der Reaktionsweg:", reaction_distance, "Meter")
print("der Bremsweg:", breaking_distance, "Meter")
print("der Anhalteweg:", stopping_distance, "Meter")
