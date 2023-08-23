""" 
Hauptprogramm: wird mit python app.py ausgeführt.
Wir importieren das Modul check in das Programm
"""
import sys
# import check
from check import petname, checker as checkit
#   # Warnung: mit Vorsicht zu genießen! 

# aus Package library importieren.
# ganzes Modul inf

from library import infos
# Funktion operating_system aus infos-Modul
from library.infos import operating_system
import library
import numpy  # pip install numpy

# print(sys.modules)  # dict aus modules
# print("*" * 40)
# print(sys.path)  # Wenn in modules nicht gefunden, sucht Python hier.

print(library.cpu())

def checker():
    print("my private checker!")


# die Funktionen mit dem check-Namespace
# check.checker()  # liegt im Namespace check (aus modul check)
# checker()
# check.petname("otto")
# ----------------------------------------

# Funktionen, die mit from geladen wurden


def main():
    checker()
    petname("Otto")
    print("Mein Computer heisst:", infos.computers_name())
    print(operating_system())
    # Underline Funktionen werden 
    # _secret() 
    # checkit()


print(f"Name des app-Modul: {__name__}")
    
if __name__ == "__main__":
    main()