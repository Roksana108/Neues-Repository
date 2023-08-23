class Animal():
    def __init__(self, name) -> None:
        self.name = name 



class Cat(Animal):

    def __init__(self, name, age, size) -> None:
        # Zugriff auf die Eletrnklasse
        Animal.__init__(self, name)
        # Zugriff 2 auf sie Elternklasse
        super().__init(name)
        self.age = age
        self.size = size

        tiger = Cat("Tim", 2, 30)
        print(tiger)