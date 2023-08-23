def summe(a: float, b: float) -> float:
    return a + b


def division(a: float, b: float) -> float:
    return a / b


OPERATIONS = {
    "+": summe,
    "/": division
}

def controller(operation: str, a: float, b: float) -> float:
    """Controller Main Function.
    
    Args:
        operation (str): Operator
        a (str): Operand
        b (str): Operand

    Raises:
        NotImplementedError
    """
    try:
        operator = OPERATIONS[operation]
    except KeyError:
        raise NotImplementedError("Diese Operation ist nicht implementiert")
    return operator(a, b)


try:
    result = controller("*", 3, 0)
    print(result)
except NotImplementedError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)