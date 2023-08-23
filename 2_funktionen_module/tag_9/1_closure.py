""" 
Closure Beispiel 2 (Parkticket)
https://de.wikipedia.org/wiki/Currying
Currying ist eine Art von Closure (eng verwandt)
"""
from typing import Final
from functools import partial

FIX: Final = 30
VAT: Final = 1.19


def park_ticket(fix: float, vat: float, price: float) -> float:
    return (fix + price) * vat

def park_ticket_closure(fix: float, vat: float):
    def inner(price: float) -> float:
        return (fix + price) * vat
    return inner


# eher nicht, da unnötige Wiederholung von fix und Vat
park_ticket(30, 1.19, price=42.2)
park_ticket(30, 1.18, price=42.2)  # fehler schleichen sich
park_ticket(20, 1.19, price=42.2)

# gut
park_ticket(fix=FIX, vat=VAT, price=42.2)
park_ticket(fix=FIX, vat=VAT, price=22.2)
park_ticket(fix=FIX, vat=VAT, price=32.2)

# besser
ticket_price = park_ticket_closure(fix=FIX, vat=VAT)
ticket_price(price=23.2)
ticket_price(price=19.2)
ticket_price(price=3.2)

# am besten (mit partial)
ticket_price_neu = partial(park_ticket, fix=FIX, vat=VAT)
ticket_price_neu(price=23.2)