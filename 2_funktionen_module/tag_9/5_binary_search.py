""" 
Binary Search Suchalgorithmus rekursiv
https://de.wikipedia.org/wiki/Bin%C3%A4re_Suche

"""
import random
from time import perf_counter
import bisect

N = 10_000_000


def get_ordered_dataset(n):
    k = n // 2
    return sorted(random.sample([i for i in range(n)], k=k))



# book = [1, 3, 5, 8, 12, 21, 23, 78, 129, 782]
# print("78 ist im Buch vorhanden und an Index: ", book.index(78))

def binary_search(array: list[int], target: int, lo: int, hi: int) -> int:
    """Recursive implementation of binary search."""
    
    # Element wurde nicht gefunden
    if lo > hi:
        return -1

    # Mitte finden, bzw. mittlerer Index
    mid = (lo + hi) // 2

    # Element gefunden, mid ist der Index des gefundenen 
    if array[mid] == target:
        return mid
    
    if target < array[mid]:
        return binary_search(array, target, lo, mid - 1)
    else:
        return binary_search(array, target, mid + 1, hi)


dataset = get_ordered_dataset(N)
target = dataset[-1]

# Suche nach einem Wert per Binary Search
start = perf_counter()
result = binary_search(dataset, target, lo=0, hi=len(dataset) - 1)
print(f"Das Target {target} befindet sich am Index: {result}")
end = perf_counter()
print(f"Der Binary Search hat {end - start:.2f} Sekunden gebraucht")

# Suche per index-Methode nach einem Wert
start = perf_counter()
print(f"Das Target {target} befindet sich am Index: {dataset.index(target)}")
end = perf_counter()
print(f"Der Index-search hat {end - start:.2f} Sekunden gebraucht")

# per bisect (noch schneller geht es mit:)
bisect.bisect_left(dataset, target)