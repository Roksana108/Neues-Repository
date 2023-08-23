def f():
    """
    Raises:
        Zero-Division Error
    """
    3 / 0


def g():
    f()
    

def main():
    g()

try:
    main()
except ArithmeticError:
    print("das ging schief")