""" 
praktische Anwendung von yield
"""

def filter_numbers(numbers: list):
    filtered_numbers = []
    for number in numbers:
        if number > 10:
            filtered_numbers.append(number)
    return filtered_numbers


def filter_numbers2(numbers: list):
    for number in numbers:
        if number > 10:
            yield number
        

result = filter_numbers2([2, 23, 98, 3])
for el in result:
    print(el)