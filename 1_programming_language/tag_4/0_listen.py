""" 
Datentyp Liste, verändlich, Sequenz

"""

string = "Hi there"
string = string.replace("Hi", "Howdy")  # erzeugt einen neuen String (nicht inplace ersetzt)
print(string)
# string[0] = "B"  # TypeError: 'str' object does not support item assignment


# Schulnoten
özgür = 1
peter = 3
armin = 2
serap = 1

notendurchschnitt = (özgür + peter + armin) / 3


noten = ["Özgür", "Peter", "Armin", "Serap"]
schulnoten = [1, 3, 2, 1]

schulnoten[1] = 1
print(schulnoten, type(schulnoten))