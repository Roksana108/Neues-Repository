from abc import abstractmethod, ABC


class My_Abstract_Class(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name
        
    # Weitere abstrakte Methoden bauen


class Human(My_Abstract_Class):
    def __init__(self, name):
        self.name = name


class Animal(My_Abstract_Class):
    def __init__(self, name):
        self.name = name


tony = Human("Tony")
print(tony.name)
lassie = Animal("Lassie")
print(lassie.name)
