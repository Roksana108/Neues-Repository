"""
"guter" Seiteneffekt
"""
players = {
    "bilbo": {
        "life": 100,
        "power": 10,
        "weapons": {"knife", "candle"}
    },
    "gollum": {
        "life": 120,
        "power": 29,
        "weapons": set()
    },
}


def set_life_points(player, points):
    players[player]["life"] += points


set_life_points("gollum", 3)