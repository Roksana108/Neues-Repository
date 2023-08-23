"""
man kann map auch mehrere Iterables übergeben 
"""

prices = [10, 20, 30]
sells = [100, 89, 120]

# imperative Denkenweise 
result_comp = [a * b for a, b in zip(prices, sells)]
print(result_comp)

# funktinale Denkweise 
result = map(lambda x, y: x * y, prices, sells)
print(list(result))

# Aufagabe 
# jedes Element von monty so unwandeln, dass der erste 
# Buchstabe groß geschrieben ist. map benutzen!
# [eggs", "spam whomp", "cheese", "ham"]  
monty = ["eggs", "spam whomp", "cheese", "ham"] 
monty_up = map(lambda c: c.capitalize(), monty)
monty_up = map(str.title, monty)  # dazu mehr in OOP
print(list(monty_up))
# print(str.title("x"))
# als Lisr Coprehension

# als Lsit Comprehesion
print([word.title() for ])