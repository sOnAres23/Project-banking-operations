from src.decorators import log


def test_log():
    @log(filename="test_log.txt")
    def my_function(a, b):

        return a + b

    my_function(5, 3)
    assert 'my_function ok. Result: 8'


def test_log_without_filename(capsys):
    @log()
    def my_function(a, b):
        return a + b
    my_function(4, 4)
    captured = capsys.readouterr()
    assert "my_function ok. Result: 8\n" in captured.out


def test_log_if_error():
    @log()
    def my_function(a, b):
        return a + b

    my_function(1, 'f')
    assert "my_function error: unsupported operand type(s) for +: 'int' and 'str'. Inputs: (1, 'f'), {}"
