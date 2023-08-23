class Dog:
    __slot__ = ("name")

    def __init__(self, name) -> None:
        self.name = name



dog = Dog("Lassie")
print(Dog.__dict__)
print(dog.__dict__)
print

__dict__ = {}