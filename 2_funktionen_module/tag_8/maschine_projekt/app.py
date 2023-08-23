"""
Hauptprogramm: wird mit python app.py ausgeführt
Wir importieren das Modul check in das Programm
"""

import sys
#  import check
from check import checker
#  # Warnung: mit Vorsicht zu genißen!
# from check import petname, checker as checkit
from library import infos
#  Funktion operatig_system aus infos-Modul
from library.infos import operating_system

# import random

# print(sys.modules["contextlib"])  # dickt aus modules
# print("*" * 40)
# print(sys.path)  # Wenn in modules nicht gefunden, sucht Python hier


def checker():
    print("my private checker!")


# die Funktion mit dem check-Namespace
#  check.checker()  # liegt im Namespace check (aus module check)
checker()
# check.petname("otto")
# ----------------------------------------------


# die Funktionen, die mit from gelanden wurde

def main():
    checker("Otto")
    petname("Mein Computer heisst:", infos.computer.name())
    # Underline Funktion werden 
    # secret()
    # checkit()
print(f"name des app-Modul: {__name__}")



if __name__ == "__main__":
    hauptprogramm()    

