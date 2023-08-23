""" 
Docstrings: Kommentare von Modulen, Funktionen/Methoden und Klassen

1. Zeile eines Docstrings ist die Summary Line (muss < 79 Zeichen sein)
"""


def wool_amount_default(amount_sheep, wool):
    """Menge der Wolle, die eine Schafherde im Monat produziert."""
    ...


def wool_amount_google(sheep, wool):
    """Menge der Wolle, die eine Schafherde im Monat produziert.

    Die Menge Wolle, die eine Schafherde im Monat produziert bei
    gegebener Anzahl an Schafen und durchschnittlicher Wollmenge
    pro Schaf.
    https://google.github.io/styleguide/pyguide.html

    Args:
        sheep (int): die Anzahl Schafe
        wool (int): die durchschnittliche Wollmenge eines Schaf
            pro Monat.

    Raises:
        NoSheepError: wenn keine Schafe in der Herde (sheep = 0)

    Returns:
        int: durchschnittliche Menge an Wolle pro Monat
    """
    return sheep * wool


def wool_amount_numpy(sheep, wool):
    """Liefert die berechnete Wollmenge.

    Die Menge Wolle, die eine Schafherde im Monat produziert bei
    gegebener Anzahl an Schafen und durchschnittlicher Wollmenge
    pro Schaf (Numpy/Pandas Style).
    https://numpydoc.readthedocs.io/en/latest/format.html

    Parameters
    ----------
    sheep : int
        the number of `sheep`
    wool : int
        amount of `wool` per month

    Raises
    ------
    NoSheepError
        keine Schafe in der Herde (sheeps=0)

    Returns
    -------
    int
        average amount of wool per month

    str
        test dummy 

    See Also
    --------
    average : how to calculate average wool per sheep.
    URL: https://numpydoc.readthedocs.io/en/latest/format.html

    Examples
    --------
    >>> wool_amount_numpy(2, 2)
    4
    >>> wool_amount_numpy(25, 1)
    25
    >>> wool_amount_numpy(10, 1)
    10
    """
    return sheep * wool


def wool_amount_rst(sheep, wool):
    """
    Liefert die berechnete Wollmenge.

    Die Menge Wolle, die eine Schafherde im Monat produziert bei
    gegebener Anzahl an Schafen und durchschnittlicher Wollmenge
    pro Schaf (restructered text).
    https://sphinxcontrib-napoleon.readthedocs.io/en/latest/index.html

    :param sheep: Die Anzahl der Schafe
    :param int wool: Wollmenge pro Schaf pro Monat
    :raises: :class:`NoSheepError`: wenn keine Schafe in der Herde (sheeps=0)

    :returns: durchschnittliche Menge an Wolle pro Monat
    :rtype: int
    """
    return sheep * wool



wool_amount_default(3, 4)

# help(wool_amount_default) Hilfe aufrufen für Funktion wool_amount_default
print(wool_amount_default.__doc__)  # dunder_doc