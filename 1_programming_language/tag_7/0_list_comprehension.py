"""
Listen Abstraktion (List Comprehension): erzeugt IMMER eine neue Liste
"""

# klassisch
seq = [1, 3, 8]
new_seq = []
for element in seq:
    new_seq.append(element**2)
print(new_seq)


# als List-Comprehension (pythonisch)
# lege neue Liste an, für jedes Element 
seq = [1, 3, 8]
new_seq2 = [element**2 for element in seq]
print(new_seq2)

# x, y, r => float
# x = float(input("Bitte x eingeben"))
# y = float(input("Bitte y eingeben"))
# r = float(input("Bitte r eingeben"))

# # x, y, r => float per split
# user_input = input("Bitte Werte eingen eingeben (x y r)")
# user_input_list = user_input.split()
# float(user_input_list[0])

# mit List Comprehension
user_input_list = input("Bitte Werte eingen eingeben (x y r)").split()
x, y, r = [float(value) for value in user_input_list]
print(x, y, r)