"""
Datentyp bool

Wahrheitswert, kennt nur zwei Zustände wahr (1) oder falsch (0)
"""
a = True
b = False

print("Typ a: ", type(a))  # objekt der Klasse <class 'bool'>

"""
boolsche Operatoren / Operatorenpräzedenz
NOT
AND
OR
"""
a = True
b = False
c = True

"""
AND
a  b  AND
1  0   0
1  1   1 
0  0   0
0  1   0

OR
a  b  OR
1  0   1
1  1   1 
0  0   0
0  1   1

https://de.wikipedia.org/wiki/Kurzschlussauswertung
"""
a = True
b = False

if a and b:
    print("a und b ist wahr")
    print("das wird auch ausgeführt")

if a or b:
    print("a oder b ist wahr")


"""
NOT (Negation) not
"""
if not a:
    print("nicht a ist False")

if not a or not b:
    print("nicht a oder nicht b ist true")

a = True
b = False

if not a and not b:
    print("nicht a und nicht b ist false")