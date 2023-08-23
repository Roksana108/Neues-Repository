class Child():

    __slots__ = ("name", "age")

    def __init__(self, name, age):
        self.name = name
        self.age = age


bob = Child("bob", 5)
# print(bob.__dict__)
# print(bob.__dict__["age"])
# print(Child.__dict__)
print(Child.__dict__["age"])

