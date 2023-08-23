"""
nonlocal Keyword: eher zurückhaltend nutzen.
"""


def outer():
    x = 1
    y = 2

    def inner():
        nonlocal x
        x += 1

        def maxinner():
            nonlocal x
            nonlocal y
            y = 33
            x += 1
        maxinner()

    inner()
    print(f"x in outer: {x=}")
    print(f"y in outer: {y=}")

outer()