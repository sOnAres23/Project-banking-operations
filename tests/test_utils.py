import pytest

from src.utils import up_first, text_reverse


def test_text_reverse_():
    assert text_reverse('og123') == '321go'
    assert text_reverse('boj doog') == 'good job'


@pytest.mark.parametrize('value, expected', [
    ('og123', '321go'),
    ('boj doog', 'good job')
])
def test_text_reverse(value, expected):
    assert text_reverse(value) == expected


def test_up_first():
    assert up_first("skypro") == "Skypro"
    assert up_first(" ") == " "
