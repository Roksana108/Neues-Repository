class Dog:
    # Konstruktor
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # Setter
    # Notation in Form von Snakecase
    def set_name(self, name):
        self.__name = name

    # Getter
    # Notation in Form von Snakecase
    def get_name(self):
        return self.__name
    
katze = Dog("Heinz", 7)
katze.set_name("Karl")
print(katze.get_name())
