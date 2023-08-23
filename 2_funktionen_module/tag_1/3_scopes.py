""" 
global keyword
"""
y = 2
print(f"id von y global {id(y)}")


def fn():
    global y  # => eher vorsichtig benutzen
    y = 13  # Shadowing (Überschatten von Namen)
    print(f"y in local fn(): {y=}")
    print(f"id von y local {id(y)}")


fn()
print(f"y in globalem Scope: {y=}")