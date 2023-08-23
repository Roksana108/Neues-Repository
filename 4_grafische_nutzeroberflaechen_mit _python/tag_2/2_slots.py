from typing import Any


class Dog:

    # # Kontrolle über die Anzahl und die Benennung von Attributen
    __slots__ = ("name", "__age")

    # # Konstruktor
    # Magic Methode laufen im Hintergrund
    def __init__(self, name):
        self.name = name

    def __call__(self) -> Any:
        return self.name


dog = Dog("Lassie")
print(dog())
