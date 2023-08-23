""" 
mapping: für jedes Element der Sequenz eine Funktion ausführen
"""

for _ in range(2):
    print("Hallo Welt")

print("*" * 50)

# fragwürdig
x = [print("hallo neue welt") for _ in range(2)]
print(x)  # [None, None]