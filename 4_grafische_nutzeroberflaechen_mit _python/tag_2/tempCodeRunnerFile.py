class Animal:
    def __init___(self, name, age, species):
        self.name = name
        self.age = age
        self.spiecies = species

    def give_sound(self):
            result = "Miaahu"
            return result


class Cat(Animal):
    def __init__(self, name, age, species, color)
    Animal.__init__(self, name, age, species)
    self.color = color

    def is_moving(self):
        result = "Cat is moving"
        return result
tiger = Cat("Laurusi", 8, "carnivora", "brown")
print(tiger.age)
print(tiger.color)
print(tiger.give_sound())
print(tiger. is_moving())