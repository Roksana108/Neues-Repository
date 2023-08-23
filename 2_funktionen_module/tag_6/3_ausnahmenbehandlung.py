""" 
Wie geht man mit Ausnahmen um?

Arten von Fehler:
---------------------
1. logische Fehler (zb. Endlosloops / falschen Schlüsse)
2. Syntax Fehler (kann man nicht "abfangen")
3. Runtime Error (können wir "abfangen") Exception Handling

Exception Hierachy:
https://docs.python.org/3/library/exceptions.html
"""

x = 1
print(14 / x)

names = {
    "alf": 3,
    "bob": 4
}

# Look before you leap
if "bilbo" in names:
    print(names["bilbo"])  # Keyerror

# It's easier to ask forgiveness than it is to get permission (EAFP)
# Zitat von Grace Hopper (Computerpionierin)
try:
    print(names["bilbo"])  # kritischer code
except:
    # hier wird alles aufgefangen!
    print("an error occured! this key is not valid")