"""
Gegeben ist ein Gameboard mit der Dimension 200 x 200 px.
Der Ursprung des Koordinatensystems ist die
obere linke Ecke (0,0).
Das Board ist zudem unterteilt in ein 50 x 50 Raster

0     1     2    3
----|----|----|----|--
    |    |    |    |  0
----|----|----|----|--
    |    |    |    |  1
----|----|----|----|--
    |    |    |    |  2
----|----|----|----|--
    |    |    |    |  3
----|----|----|----|--

    <- X ->

Die Spielfigur befindet sich aktuell an einer zufälligen Position
auf dem Brett. Bewegt sie sich nach rechts oder links, bewegt sie
sich auf der X-Achse, vertikale Bewegungen betreffen die y-Achse.
Jeder Schritt des Spielers ist 1 Pixel.

Die Bodenart in jedem Rasterfeld ist in folgender Matrix
organisiert (1=Wiese, 2=Wasser, 3=Schlamm):
ground = [
    [1, 1, 1, 1],
    [1, 3, 1, 2],
    [1, 1, 3, 1],
    [2, 1, 1, 1],
]

1) In welchem Raster befindet sich die Spielfigur,
wenn die X- und Y- Koordinate gegeben ist (y Zählung zählt nach unten)
Beispiele:
x: 0, y: 0 => Rasterfeld 0/0

x: 50, y: 10 => Rasterfeld 1/0

x: 52, y: 50 => Rasterfeld 1/1

x: 48, y: 190 => Rasterfeld 0/3

x: 200, y: 90 => Rasterfeld: out of gameboard

2) Gebe zusätzlich die aktuelle Bodenart aus.

Lege Variablen, Konstanten (zb. für Feldgröße, Spielbrett-Dimension)
an und printe das Ergebnis mit Hilfe des f-Strings.

Die x- und y Koordinaten sollen durch Userinput gewonnen werden.
Wir erwarten nur legale x-y-Werte (positiv, nach Integer castbar)
"""
GRID_SIZE = 50

GROUND = [
    [1, 1, 1, 1],
    [1, 3, 1, 2],
    [1, 0, 3, 1],
    [2, 1, 1, 0],
]
SURFACE = ["Fels", "Wiese", "Wasser", "Schlamm"]

x, y = input("Bitte gebe x- und y Koordinate ein:").split()

x = int(x)
y = int(y)

if x < 200 and y < 200:
    x_raster = x // GRID_SIZE
    y_raster = y // GRID_SIZE

    print(f"Befindet sich in Raster {x_raster, y_raster}")
    print(f"die Bodenart ist {SURFACE[GROUND[y_raster][x_raster]]}")
else:
    print("Player befindet sich ausserhalb des Boards")
