# Textadventure
objects = ["shovel", "sword", "knife", "candle"]

command = "go north"
command = "go south"
command = "go sword"
command = "go north"
command = "pick fork"  # get sword / pick sword up
command = "pick candle"
command = "go south"

match command.split():
    case ["go", ("north" | "south" | "west" | "east") as direction]:
        print(f"Player goes {direction}")
    # guard: prüft Wert auf Bedingung
    case ["pick", obj] if obj in objects:
        print(f"User is picking up {obj}")
    case ["pick", _]:
        print("This object cannot be picked up!")

# Check Datentyp
val = "33"
match val:
    case str():
        print("Val ist ein String")
    case int() | float():
        print("Val ist ein numerischer wert")
