from functools import wraps
from typing import Any, Callable


def log(filename: Any = None) -> Callable:
    """ Декоратор для логгирования вызовов функций и их результатов.
    :param filename: Путь к файлу для записи логов. Если не указан, логи выводятся в консоль.
    :return: Функция или None в случае ошибки. """
    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok. Result: {result}"
                if filename:
                    with open(filename, "a") as f:
                        f.write(log_message + "\n")
                else:
                    print(log_message)
            except Exception as e:
                error_message = f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "a") as f:
                        f.write(error_message + "\n")
                else:
                    print(error_message)
        return inner

    return wrapper


@log()
def my_function(a: int, b: int) -> int:
    return a + b


my_function(1, 7)
my_function(1, "t")
