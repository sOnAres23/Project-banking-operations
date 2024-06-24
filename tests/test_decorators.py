import pytest
from src.decorators import log


def test_log(capsys):
    @log(filename="test_log.txt")
    def my_function(a, b):
        return a + b
# Проверка корректного выполнения функции
    my_function(5, 3)
    captured = capsys.readouterr()
    assert "my_function ok. Result: 8\n" in captured.out
# Проверка ошибки при выполнении функции
    try:
        my_function("f", 2)
    except TypeError as e:
        captured = capsys.readouterr()
        assert "my function error: " in captured.out
