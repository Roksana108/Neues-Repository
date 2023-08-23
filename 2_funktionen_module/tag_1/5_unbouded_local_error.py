"""
Unbound Local Error
"""
y = 22.2


def fn():
    # y = y + 2  # Unbound local error
    y_neu = y + 2
    print(y_neu)


fn()
