""" 
Aus einer Liste von Strings einen String bilden (mit einem definierten Trennzeichen (Glue))

["top", "gut", "whatever"] => top-gut-whatever
"""

SEPARATOR = "-"

# ---------------------------------------------------
# schlechter Weg
# ---------------------------------------------------
words = ["top", "gut", "whatever"]
new_str = ""
for word in words:
    new_str = new_str + word + SEPARATOR

print(new_str)

# ---------------------------------------------------
# guter Weg (join)
# Join (Iterable von Strings zu einem String zusammenzügen)
# ---------------------------------------------------
words = ["top", "gut", "whatever"]
new_str = SEPARATOR.join(words)
print(new_str)

# Str ist eine Sequenz (H-a-m-b-u-r-g)
city = "Hamburg"
print(SEPARATOR.join(city))