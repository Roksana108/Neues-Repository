"""
Modul check

The module contains the following functions:

- checker() : print something
"""

print("Hallo ich liege hier in check!")


def checker():
    print("i am the checker from moduel check!")


def petname(name: str):
    print(f"My names is {name}")


def test_programm():
    print("Hallo, ich leige hier in check!")
    checker()
    petname("pete")


if __name__ == "__main__":
    # Läuft nur, wenn die Datai check.py deirect
    # ausgeführt wird 
    print(f"Name des checks-Modul: {__name__}")
    test_programm()
