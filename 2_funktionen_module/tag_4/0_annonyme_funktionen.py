"""
Lamdba-Expression / lambda Funtion 
==> Annonyme Funktion
"""


def fn(f):
    """erwartet einen Funtionsreferenz."""
    f()  # hier wird g aufgerufen


def summe(a,b): 
     """klasische Funktion."""
     return a + b 


print(summe)
summe_neu = summe

# Funktion sind first class citizens (genauso benuztbar wie anadere Variablen)
print(summe_neu)  # Printe die  Funtionsreferenz
print(summe_neu(3, 4))  # Prionte das Resulatat der Funtion

# Funktionsreferenz weiter


def fn(f):

    f()

def g():
    print("hello i am g")


def gn():
    print("hello i am gn") 

fn(g)
fn(gn)