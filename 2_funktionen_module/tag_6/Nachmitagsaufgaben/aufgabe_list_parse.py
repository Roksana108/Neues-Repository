"""
Parse list

1.  Schreibe eine Funktion list_parse(), die eine Liste von Strings entgegennimmt, diese versucht als Float zu parsen und eine Liste von Floats zurückgibt. Es finden sich auch Strings in der Liste, die das Komma als Dezimaltrennzeichen nutzen, diese müssen auch berücksichtigt werden.
2.  Alle nicht zu Float parsebaren Eingabestrings werden in einer Fehlerliste gesammelt. Diese muss die Originalstrings enthalten.

Der Rückgabewert der Funkition ist ein Tupel aus resultlist. und errorlist


Beispiel:
a = ["2", "a3", "0.2", "0,4", "a01", "3", ",", "a.a", "a,"]

Result:
b = [2.0, 0.2, 0.4, 3.0]
errorlist = ['a3', 'a01', ',', 'a.a', 'a,']

Hinweise: nutze Typehints, Try except, Doc-String
"""


a = ["2", "a3", "0.2", "0,4", "a01", "3", ",", "a.a", "a,a"]
