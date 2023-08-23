""" 
Truthy Values / Falsy Values

Folgende Werte werden als falsch gewertet:
()
[]
0
{}
set()
"" (leerer String)
"""

a = 0

if a:
    print("ja, a ist nicht nicht 0")

user_input = ""

if user_input:
    print("ich speichere den Userinput ab, wenn er existiert.")