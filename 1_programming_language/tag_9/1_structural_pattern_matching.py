"""
der "switch-case" in Python
Structural Pattern Matching (seit 3.10)

https://peps.python.org/pep-0636/

Softkeyword
match ['_', 'case', 'match']

import keywords
keywords.kwlist
keywords.softkwlist
"""
weekday = 1
weekday_name = ""

# klassische Python
if weekday == 1:
    weekday_name = "Monday"
elif weekday == 2:
    weekday_name = "Tuesday"
else:
    weekday_name = "undefined"

match = "34,2"
case = 9
_ = 3

# Pattern matching: match
# 
match weekday:
    case 1:
        weekday_name = "Monday"
    case 2:
        weekday_name = "Tuesday"
    case _:
        weekday_name = "undefined"

# Liste von Werten
name = "Captain Jean Luc Picard".split()
match name:
    case ["Captaini", *args]:
        print(f"Captain args: {args}")
    case ["Captain", "Jean", *args]:
        print(f"Captain Jeans args: {args}")
    case _:
        print("konnte nicht erkannt werden")

input_string = "+ 3 3 4 5 6"
match input_string.split():
    case ["+", *args]:
        print("Values: ", [float(v) for v in args])

# Textadventure
command = "go north"
command = "north"
command = "pick sword up"  # get sword / pick sword up
command = "go sword"

match command.split():
    case ["north"] | ["go", "north"]:
        print("user is going north")
    case ["get", obj] | ["pick", "up", obj] | ["pick", obj, "up"]:
        print("user is picking up", obj)
