""" 
ein unveränderliches Set, das frozenset
"""
a = {1, 2}

# ein Set kann kein key eines Dicts sein
# TypeError: unhashable type: 'set'
# d = {
#     (1, 2): [1, 2, 3]
# }

# Frozenset als Key eines Dicts
b = frozenset([2, 3, 4, 5])
print(b, type(b))

d = {
    b: [1, 2, 3]
}

# Zugriff auf Dictionary via Frozenset
print(d[frozenset([2, 3, 5, 4])])