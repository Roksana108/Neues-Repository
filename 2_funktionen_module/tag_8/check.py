""" 
Modul check

The module contains the following functions:

- `checker()`: prints something
"""
print(f"Name des checks-Modul: {__name__}")

def checker():
    print("i am the checker from module check!")


def _secret():
    # sobald das mit _ anfängt
    # wird nicht via from check import *
    print("some secret function")

def petname(name: str):
    print(f"My name is {name}")


def test_programm():
    print("Hallo, ich liege hier in check!")
    checker()
    petname("pete")


if __name__ == "__main__":
    # LÄuft nur, wenn die Datei check.py direkt
    # ausgeführt wird
    print(f"Name des checks-Modul: {__name__}")
    test_programm()