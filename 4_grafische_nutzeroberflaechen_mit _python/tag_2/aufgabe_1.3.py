class Human:
  
# Kontrolle von Anzhal Benennung von Attributen 
  __slots__ = ("mortality", "name", "age")
  
  def__init(self, name, age):
  self.name = name
  self.age = age
  self.mortality = True
  self.size = 45


# Magic Methode
def __call__(slef):
    return"A human named" + slef.name


billy=Human("Billy", 47)
print(billy.name)
print(billy.age)
print(billy.mortality)
print(billy())













