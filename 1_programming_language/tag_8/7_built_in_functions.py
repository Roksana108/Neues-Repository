""" 
Built in Functions: "eingebaute" Funktionen, 
die in Python ohne Import zur Verfügung stehen
https://docs.python.org/3/library/functions.html
"""

""" 
print
type 
len
id
input
help
int, str, float, list, dict, set, tuple, complex, frozenset, bin, hex, bool
open
enumerate
zip
round
range
pow
"""

# sum (erwartet Iterable), optional startwert
print(f"sum: {sum([1, 2, 3])}")
print(f"sum: {sum([1, 2, 3], start=10)}")

# abs (Absoluter wert, Betrag)
print(f"abs(-2): {abs(-2)}, {abs(-2.2)}")

# sorted()
a = [1, 2, 4, 1]
print("id a:", id(a))
a.sort(reverse=True)  # in Place sortiert
print(a)
print("id a:", id(a))

print("*" * 40)

b = [1, 2, 4, 1]
print("id b:", id(b))
b = sorted(b, reverse=True)  # erzeugt neue sortierte Liste
print(b)
print("id b:", id(b))

# max, min
b = [1, 2, 4, 1]
print(f"max von b: {max(b)}")
print(f"min von b: {min(b)}")

# pow
print(f"{pow(2, 3)}, ", 2 ** 3)

# any gibt true zurück, wenn mindestens ein Element der Menge wahr ist
print(f"any: {any([0, 0.0, False, None, {}, (), set()])}")
print(f"any: {any([0, 0.1, False, None, {}, (), set()])}") # if a == True or b > 3 or "x" in y

if any([a[0] == 1, b[0] > 3, "x" in b]):
    print("eins davon ist wahr")

# all gibt true zurück, wenn alle Elemente der Menge wahr sind
print(f"all:", all([1, 1.1, 0, "test"])) # False

# eval (Eval ist evil)
input_line = "4 + 4 * 3"  # Ausdruck
print("eval:", eval(input_line))

# exec (Exec ist nocht böser)
code = """
import sys
print(sys.executable)
"""
exec(code)

# globals() / locals(): zeigt alle globale / lokale Variablen im aktuellen 
# Kontext an
print(globals())
print(locals())

# iter
a = [1, 2, 3, 4]  # iterable for el in a. {3, 2, 1}
a_iter = iter(a)

# next (rufe das nächste Element eines Iterators auf)
p = next(a_iter)
print(p)
print("*" * 40)

# Generator Expression (Iterator)
# wird erst bei Bedarf berechnet (nextp)
list_comp = (i**2 - 1 for i in range(100_000_000_000))
print(next(list_comp))
print(next(list_comp))

# reversed
rev = reversed([1, 2, 3])
print(rev)
print("1. Element von rev:", next(rev))
for element in rev:
    print(element)

print("*" * 40)

# Iterator hat sich verbraucht (wird nix mehr ausgegeben)
for element in rev:
    print(element)

# divmod 
x = 2
y = 4
z = divmod(x, y)  # gibt tuple von // und % zurück
print("z:", z)
