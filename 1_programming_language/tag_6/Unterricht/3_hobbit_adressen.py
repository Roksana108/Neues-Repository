from pprint import pprint

address_list = [
    (
        "salutation",
        "first_name",
        "last_name",
        "street",
        "city",
    ),
    (
        "Mr.",
        "Frodo",
        "Baggins",
        "Bag End 1",
        "Hobbiton",
    ),
    (
        "Mr.",
        "Samwise",
        "Gamgee",
        "Bagshot Row 2",
        "Hobbiton",
    ),
    (
        "Mrs.",
        "Galadriel",
        "Elb",
        "189 Flower Gardens",
        "Lothlorien",
    ),
]

"""
address_dict = {
    'Frodo': {'city': 'Hobbiton',
            'first_name': 'Frodo',
            'last_name': 'Baggins',
            'salutation': 'Mr.',
            'street': 'Bag End 1'},
    'Galadriel': {'city': 'Lothlorien',
                'first_name': 'Galadriel',
                'last_name': 'Elb',
                'salutation': 'Mr.',
                'street': '189 Flower Gardens'},
    'Samwise': {'city': 'Hobbiton',
                'first_name': 'Samwise',
                'last_name': 'Gamgee',
                'salutation': 'Mr.',
                'street': 'Bagshot Row 2'}
}
# zugriff
print(address_dict["Frodo"]["street"]) => 'Bag End 1'

15 Minuten zeit! Happy Coding!
"""

head = address_list.pop(0)
address_dict = {}
for row in address_list:
    address_dict[row[1]] = dict(zip(head, row))


pprint(address_dict, depth=2)
print(address_dict["Frodo"])
print(address_dict["Frodo"]['street'])
print(address_dict["Frodo"]['last_name'])