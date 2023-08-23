# Funktion Tiger
def Tiger(name, age):
    return Cat(name, age, True)


class Cat():

    # Bindung der Funktion Tiger an die Klasse Cat
    # Überladung (Overload) einer Methode
    # Zwei oder mehrere Varianten derselben Methode
    
    # KLASSENATTRIBUTE
    Tiger = staticmethod(Tiger)

    def __init__(self, name, age, endangered):
        # OBJEKTATTRIBUTE
        self.name = name
        self.age = age
        self.endangered = endangered


# Objekterstellung von tiger über die statische Methode Tiger
tiger = Tiger("Tony", 3)
print(tiger.name, tiger.endangered)

Tiger("Tom", 2)
