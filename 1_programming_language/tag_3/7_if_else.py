""" 
if else
"""
alter = 17

if alter >= 18:
    print("Darf in den Club")
    x = 3
    print("geheimer zugangscode", x)
else:
    print("Darf nicht in den Club und muss nach hause gehen.")


a = 5

if a > 4:
    print("die zahlt ist größer als 4")
elif a > 2:
    print("die zahlt ist größer als 2 und kleiner gleich 4")
else:
    print("die Zahl ist kleiner gleich als 2")


# user_input ist ein leerer String, wenn bei input nur Enter gedrückt wird.
user_input = input("Bitte gebe eine Zahl ein: ")
if user_input:
    print("User hat die Zahl eingegeben:", user_input)
else:
    print("Userinput ist leer")