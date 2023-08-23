""" 
Dictionary Comprehension
"""
value_list = [("a", 1), ("b", 2)]
d = {key: value for key, value in value_list}
print(d)

# über dict
d2 = dict(value_list)
print(d2)