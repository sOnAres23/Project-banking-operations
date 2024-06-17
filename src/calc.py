def add(x: int, y: int) -> int:
    return x + y


def subtract(x: int, y: int) -> int:
    return x - y


def multiply(x: int, y: int) -> int:
    return x * y


def divide(x: int, y: int) -> float:
    if y == 0:
        raise ZeroDivisionError('Деление на ноль невозможно')
    return x / y
