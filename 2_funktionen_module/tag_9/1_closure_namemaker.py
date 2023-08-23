"""
By definition, a closure is a nested function that references one or more
variables from its enclosing scope.
"""
def outer(n):

    def inner(name):
        print("i am the inner fn, das ist das n:", n)
        print("mein Name ist:", name)
        print(x)

    n = 99
    x = 42
    print(inner.__closure__)
    return inner


funktionsobjekt = outer(n=3)
print(funktionsobjekt.__closure__)
funktionsobjekt("Hase")   # inner()