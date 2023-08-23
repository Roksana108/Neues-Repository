"""
Kopie einer collection bearbeiten.
lokal eine Kopie der collection machen
"""
from copy import deepcopy

d = {
    "a": 2,
    "b": 4
}


def nullify_entries(container):
    container_kopie = deepcopy(container)

    for key in container_kopie:
        container_kopie[key] = 0
    
    return container_kopie


d2 = nullify_entries(d)
print(d2)
print(d)
