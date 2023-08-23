""" 
In Operator

prüft, ob eine Sequenz in einer anderen Sequenz vorhanden ist
"""

a = "aa"
b = "aabbaabb"

if "aa" in b:
    print("aa ist in b enthalten")


city = "hamburg"
user_input = "ja, ich komme aus HAmburg"

if city not in user_input.lower():
    print("Hamburg ist in Userinput enthalten")