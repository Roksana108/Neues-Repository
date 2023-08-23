"""
Aufgabe:
 Der optimale Puls bei Ausdauersportarten hängt vom Alter ab. 
 Er lässt sich mit der Formel P = 165 - 0.75*Alter bestimmen. 
 So ist der optimale Puls für 18 Jahre 151.5. Schreibe ein Programm, 
 das folgenden Dialog ermöglicht:

Alter: über input einzugeben
"""
age = int(input("Bitte gebe das Alter ein: "))
puls = 165 - 0.75 * age
print("Puls: ", round(puls))
