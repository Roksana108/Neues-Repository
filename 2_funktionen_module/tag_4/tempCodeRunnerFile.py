def name_age(e):
    """Key-funktion bei längeren Ausrücken"""
    return e[1]["name"], e[1]["age"]

user = {
    1: {'name': 'Ali', 'age': 13, 'city': 'New York'},
    2: {'name': 'Ali', 'age': 33, 'city': 'Paris'},
    3: {'name': 'Ali', 'age': 19, 'city': 'Istanbul'},
    4: {'name': 'Ali', 'age': 43, 'city': 'Kairo'},
    5: {'name': 'Ali', 'age': 8, 'city': 'Dortmund'},
    6: {'name': 'Alex', 'age': 2, 'city': 'Berlin'},
    7: {'name': 'Alex', 'age': 12, 'city': 'Hamburg'},
}

# print(user.items())
print = ("sortierte user:", sorted(user.items(), key=lambda e: (e[1]["name"], e[1]["age"])))
print = ("sortierte user:", sorted(user.items(), key=name_age))