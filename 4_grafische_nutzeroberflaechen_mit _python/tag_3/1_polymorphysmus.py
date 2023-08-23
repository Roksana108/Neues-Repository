class Animal():
    def __init__(self, name) -> None:
        self.name = name 

    def move(self) -> Literal['Animal is moving']:
        return "Animal is moving"


class Cat(Animal):
    # Overwrite Mit Reffernez auf die Elternlassen 
    def __init__(self, name, age, size) -> None:
        # Refernz
        Animal.__init__(self, name)
        self.age = age
        self.size = size

    # Overwrite OHNE Refernez auf die Elternklasse 
    def move(self) -> Any:
        return self.name + "is moving"
        animal = Animal("My Animal")
        tiger = Cat("Tim", 2, 30)
        
print(animal.move())
print(tiger.move())