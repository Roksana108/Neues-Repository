"""
Functools
"""

from functools import reduce
import operator


# hier findet man alle Operator ( Opearto Library der Python standard-Bibliothek)
# https://docs.python.org/3/library/operator.html</link></u>

operator.mul


numbers = [1, 2, 34, 4, 12]
print(reduce(lambda x, y: x * y, numbers))
print(reduce(operator.mul, numbers))

# Aufgabe: Schreibe als Reduce.
sentences = [
    "Mary read a story to Sam and Isla.",
    "Isla cuddled Sam.",
    "Sam chortled.",
]

sam_count = 0
for sentence in sentences:
    sam_count = sam_count + sentence.count("Sam")
print("Sam count ohne reduce:", sam_count)

def add_ccount(count, sentence):
    return count + sentence.count("Sam")

print("Sam count:", reduce(add_ccount, sentence, 0))
print(reduce(lambda acc, f: acc + f.count("Sam"), sentences, 0))



# Welche Buchtaben kommen in allen Elemten des Tupels
input_list = ("america xxx", "puerto rico xx", "muy rico xx")

result = reduce(set.intersection, map(set, input_list))
print(set(input_list[0]))
print(list(result))


