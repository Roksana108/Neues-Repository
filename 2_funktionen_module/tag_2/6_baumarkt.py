"""
Baumarkt: zwei Artikel: Schrauben (7 ct) und Muttern (4 ct)

python 6_baumarkt.py --schraube=10 --mutter=20
"""
import argparse

PRICES = {
    "schraube": 7,
    "mutter": 20
}


def setup_parser():
    """Konfiguriere den Commandline-Parser."""
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--schraube", "-S", type=int, help="Anzahl Schrauben" 
    )

    parser.add_argument(
        "--mutter", "-M", type=int, help="Anzahl Muttern"
    )

    args = parser.parse_args()
    return args


def calculate_itemprice(name, amount):
    """Berechne den Preis eines Items."""
    return PRICES[name] * amount


def order(args):
    """Bestellung verwalten."""
    prices = []

    for name, value in args.__dict__.items():
        prices.append(
            calculate_itemprice(name, value)
        )

    # if args.schraube is not None and args.schraube > 0:
    #     prices.append(
    #         calculate_itemprice("schraube", args.schraube)
    #     )

    # if args.mutter is not None and args.mutter > 0:
    #     prices.append(
    #         calculate_itemprice("mutter", args.mutter)
    #     )
    
    return prices


def display_price(prices):
    """Stellt den finalen Preis dar."""
    total = sum(prices)
    print(f"der Gesamtpreis der Bestellung ist {(total / 100):.2f} Euro")


def hauptprogramm():
    """hauptprogramm ist der Einstiegspunkt des Programms."""
    args = setup_parser()
    prices = order(args)
    display_price(prices)


hauptprogramm()