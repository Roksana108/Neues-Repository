""" 
Funktionsreferenzen
"""

def summe(a, b):
    """klassische Funktion."""
    return a + b

print(summe)
summe_neu = summe

# Funktionen sind first class citizens (genauso benutzbar wie andere Variablen)
print(summe_neu)  # Printe die Funktionreferenz
print(summe_neu(3, 4))  # Printe das Result der Funktion

# ------------------------------------------------------
# Funktionsreferenzen weiterreichen
# Beispiel: Sortierfunktionen übergeben
# ------------------------------------------------------

def fn(f):
    """erwartet eine Funktionsreferenz."""
    f()  # hier wird g aufgerufen

def g():
    print("hello i am g")

def gn():
    print("hello i am gn")


fn(g)
fn(gn)
