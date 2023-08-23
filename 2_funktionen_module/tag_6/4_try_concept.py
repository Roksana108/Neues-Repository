""" 
Fehler sollten spezifiziert werden!
"""

# Gezielt auf Zerodivision-Error eingehen

zahl = 3
x = "0"

try:
    zahl / x
except ZeroDivisionError:
    print("Es ist ein Zero-Divisionerror aufgetreten")
except TypeError:
    print("Es ist ein TypeError aufgetreten")

# Schreibe eine funktion is_float() -> bool, die prüft, ob ein String nach float parsebar ist
# is_float("3.3") => True
# is_float("3.3a") => False
try:
    y = 4  # alles, was VOR der Exceptions passiert, bleibt erhalten.
    x = float("a")
except ValueError:
    print("Preisfrage: was steht in y?", y)