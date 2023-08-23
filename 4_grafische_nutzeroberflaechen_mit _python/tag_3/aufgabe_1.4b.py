class Animal:
    # Konstruktor
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species 

    # Methoden
    def give_sound(self):
        result = "It is an Animal"
        return result
# Kindklasse wird erstellt


class Dog(Animal):
    def __init__(self, name, age, species, color, weight):
        Animal.__init__(self, name, age, species)
        self.color = color
        self.weight = weight

    # Methoden werden definiert 
    def doggy_food(self, portion):
        self.portion = portion
        return portion 

    def moving(self):
        return self.name + "wants to move!"

# ein Objekt von der Kalsse Dog erstellen
carnivora = Dog("Lauruisia", 8, "mix_bread", "brown", 11)

# alle Atribitte ausgeben
print(carnivora.name)
print(carnivora.age)
print(carnivora.species)
print(carnivora.color)
print(carnivora.weight)
  
print(carnivora.doggy_food("3 portions"))



        