""" 
Nested Dict players
jeder key ist ein Player, der als Dict repräsentiert wird.
"""
players = {}

players["bob"] = {
    "points": 4
}

players["alice"] = {
    "points": 3
}

# Punkte von alice
print(players["alice"]["points"], type(players["alice"]["points"]))


