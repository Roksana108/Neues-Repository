"""
Tic Tac Toe - Feld Analyse

Spieler X hat begonnen.

Gegeben ist eine 3x3 Matrix, die das Spielfeld repräsentiert.
Das Spielfeld ist gefüllt mit den zwei Farben der Spieler, also X und O sowie den leeren Feldern NONE.

Aufgabe:
-------------
Wir wollen in dieser Aufgabe einige Funktionen implementieren, die das Spielfeld überprüfen. Dazu gehört neben der fachlich richtigen
Implementierung auch das Angeben der Datentypen (Type-Hints)

Wir gehen zu jeder Zeit von einem gültigen Spielfeld aus (zwei sieg-
reiche Spieler kann es zum Beispiel nicht geben)

0) Das Spielfeld:

board = [
        [X, X, O],
        [O, _, X],
        [O, X, _]
    ]

An den Feldern X und O haben die Spieler bereits gesetzt, die beiden _-Felder
sind noch ungenutzt.

Die Funktionen sollen ordentlich mit Type-Hints, Rückgabewerten und Doc-Strings beschrieben werden.

Folgende Funktionen sind zu implementieren:

------------------------------------------------------------------------------
1) player()

Welcher Spieler ist als nächstes am Zug? Wir gehen davon aus, dass
immer Spieler mit der Farbe X das Spiel begonnen hat. Implementiere diese
Funktion so, dass der aktuelle Spielstand erkannt und der nächste
Spieler berechnet wird.

Beispiel:

board = [
    [X, O, _],
    [_, _, _],
    [_, _, _]
]
Spieler X darf den nächsten Zug ausführen.


------------------------------------------------------------------------------
2) actions()
Erzeuge ein Set von allen freien Feldern der Matrix. in Form von Tupeln, die
Reihe und Spalte angegeben. Beispiel:

board = [
    [X, X, O],
    [O, _, _],
    [O, X, _]
]

Result: set{(1, 1), (1, 2), {2, 2}}

------------------------------------------------------------------------------

3) winner()

Prüft, ob es einen Gewinner gibt.
Gewinner ist die Farbe, der drei Steine in einer Reihe hat: Horizontal, Vertikal
oder diagonal

board = [
    [X, O, O],
    [X, _, _],
    [X, _, _]
]

X hat gewonnen. X wird zurückgegeben.

4) terminal()

Prüft, ob sich das Board im Endzustand befindet. Entweder,
winner() ist True
oder das Board voll belegt ist und keine Züge mehr möglich sind.

board = [
    [X, O, O],
    [X, _, _],
    [X, _, _]
]

Gibt true zurück, weil winner() True ist (X)

board = [
    [X, O, _],
    [_, _, _],
    [_, _, _]
]

gibt False zurück, weil weder winner() True noch Board voll.

"""

X = "X"
O = "O"
_ = None


def player(board: list):
    """
    Welcher Spieler ist als nächstes am Zug? Wir erinnern uns: X hat das Spiel
    begonnen.
    """
    pass


def actions(board: list):
    """
    Return ein Set aller möglichen freien Felder in Form von Tupeln.
    Gibt ein leeres Set zurück, wenn keine freien Felder mehr existieren.
    """
    pass


def winner(board: list):
    """
    Return winner, falls existiert. Prüfe dazu alle Spalten, Reihen und die zwei
    Hauptdiagonalen. Ansonsten return None

    """
    pass


def terminal(board: list):
    """
    gibt True zurück, wenn a) das Board voll ist oder b) ein gewinner existiert.
    (Prüft das Ergebnis von Funktion winner())

    if winner():
        return True

    Ansonsten return False
    """


if __name__ == "__main__":
    board = [
        [X, X, O],
        [O, _, X],
        [O, X, _],
    ]

    player(board)  # welcher Spiele ist als nächstes am Zug?
    actions(board)  # gib mir eine Liste aller möglichen Spielzüge
    winner(board)  # gibt es einen Gewinner? Wer ist es?
    terminal(board)  # ist das Spiel zu Ende, weil Gewinner oder alles voll?



"""
Tic Tac Toe
"""
GRIDS = 3
X = "X"
O = "O"
_ = None

matrix = list[list[str | None]]


def player(board: matrix) -> str:
    """Returns player who has the next turn on board.

    if actions count is odd, next player is O, because X player started
    the game.

    count_ = 0 => X
    count_ = 1 => O
    count_ = 2 => X
    ...
    count_ = 9 => O

    Args:
        Board

    Returns:
        (str): next player
    """
    count = sum([sum([bool(e) for e in row]) for row in board])
    return O if count % 2 else X


def actions(board: matrix) -> set:
    """Returns set of all possible actions.

    Args:
        Board

    Returns:
        (set): tuple with all available actions on the board.
    """
    length = range(len(board))
    return {(i, j) for i in length for j in length if not board[i][j]}


def check_horizontal(board: matrix) -> str | None:
    """Check for same color in a row.

    Args:
        board: the game board
    Returns:
        str: Winner color or None
    """
    for row in board:
        # eg. set([X, X, X]) => {X} => len({X}) = 1
        if row[0] and len(set(row)) == 1:
            return row[0]
    return None


def check_vertical(board: matrix) -> str | None:
    """Check for same color in a column.

    Transpose matrix and return X, O or None if no winner vertical

    Args:
        board: the game board
    Returns:
        str: Winner color or None
    """
    m = [list(row) for row in zip(*board)]
    return check_horizontal(m)


def check_diagonal(board: matrix) -> str | None:
    """Check for same color diagonal.

    Args:
        board: the game board

    Returns:
        Winner color or None
    """

    left_right_diag = [row[i] for i, row in enumerate(board)]
    right_left_diag = [row[-i - 1] for i, row in enumerate(board)]
    return check_horizontal([left_right_diag, right_left_diag])


def check_board_full(board: matrix) -> bool:
    '''check if Board is full and no actions left to play.'''
    return not bool(actions(board))


def winner(board: matrix) -> str | None:
    """Returns the winner of the game, if there is any.
    """
    return (
        check_diagonal(board) or
        check_vertical(board) or
        check_horizontal(board)
    )


def terminal(board: matrix) -> bool:
    """Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True

    return check_board_full(board)


if __name__ == '__main__':

    board_1: matrix = [[X, O, _],
                       [X, O, O],
                       [X, _, _]]

    board_2: matrix = [[X, O, X],
                       [_, X, O],
                       [_, X, O]]

    board_3: matrix = [[_, _, _],
                       [_, _, _],
                       [_, _, _]]

    boards = [board_1, board_2, board_3]

    for board in boards:
        print(f"player {board}:", player(board))
        print(f"actions {board}:", list(actions(board)))
        print(f"actions count {board}:", len(actions(board)))
        print(f"WINNER {board}:", winner(board))
        print(f"Terminal {board}:", terminal(board))
