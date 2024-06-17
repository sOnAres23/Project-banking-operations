import pytest

from src.widget import get_data, mask_account_card


# Привел даже по 2 варианта данных со счётом и картой для тестирование функции
@pytest.mark.parametrize(
    "account_card, expected",
    [
        ("Счет 73654108430135872304", "Счет **2304"),
        ("Visa Gold 5999414228426358", "Visa Gold 5999 41** **** 6358"),
        ("Счет 35383033474447899259", "Счет **9259"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ],
)
def test_mask_account_card(account_card, expected):
    assert mask_account_card(account_card) == expected


@pytest.mark.parametrize(
    "data, expected_date",
    [
        ("2018-07-11T02:26:18.671407", "11.07.2018"),
        ("2024-06-17T12:26:18.671407", "17.06.2024"),  # А это добавил мою дату сдачи этого Д/з! :)
    ],
)
def test_get_data(data, expected_date):
    assert get_data(data) == expected_date
