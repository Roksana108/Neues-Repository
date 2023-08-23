"""
JSON: Javascript Object Notation

{
    "a": 3
}

Serialisierung:

Python                  JSON       Python
-----------------------------------------
dict                =>  object   => dict
list, tuple         =>  array    => list
str                 =>  string   => str
int, float          =>  number   => int, flaot
True                =>  true     => True
False               =>  false    => False
None                =>  null     => None
set                 => GEHT NICHT
"""

import json
from pathlib import Path

beutlins = [
    {
        "bilbo": {
            "name": "Bilbo Beutlin",
            "age": 133
        },
        "frodo": {
            "name": "Frodo Beutlin",
            "age": 67,
            "friends": ("Sam", "Merry", "Pippin")
            # "tools": {"knife", "candle"} TypeError! Set ist nicht serialisierbar!
        },
    },

    {
        "gollum": {
            "name": "gollum",
            "age": 2000
        },
    },
]

# Python- Objekt nach JSON seralisieren 
print(json.dumps(beutlins))

# ------------------------------------------------------------------
# JSON Datei schreiben
# ein Python-Obejkt nach JSON serilaisieren und als Datei sperichern 
# ------------------------------------------------------------------
with open(Path(__file__).parent / "beutlins.json", mode="w") as f:
    json.dump(beutlins, f)
    print(beutlins)