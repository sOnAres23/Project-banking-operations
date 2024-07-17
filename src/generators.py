from typing import Dict, Generator, List

transactions = (
    [
        {
            "id": 650703,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации"
        },
        {
            "id": 3598919,
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": 29740,
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту"
        },
        {
            "id": 593027,
            "state": "CANCELED",
            "date": "2023-07-22T05:02:01Z",
            "amount": 30368,
            "currency_name": "Shilling",
            "currency_code": "TZS",
            "from": "Visa 1959232722494097",
            "to": "Visa 6804119550473710",
            "description": "Перевод с карты на карту"
        },
        {
            "id": 366176,
            "state": "EXECUTED",
            "date": "2020-08-02T09:35:18Z",
            "amount": 29482,
            "currency_name": "Rupiah",
            "currency_code": "IDR",
            "from": "Discover 0325955596714937",
            "to": "Visa 3820488829287420",
            "description": "Перевод с карты на карту"
        },
        {
            "id": 3691525,
            "state": "EXECUTED",
            "date": "2021-03-14T07:31:40Z",
            "amount": 12576,
            "currency_name": "Ruble",
            "currency_code": "RUB",
            "from": "Discover 8455447150087314",
            "to": "Счет 70453658863403233739",
            "description": "Перевод организации"
        }
    ]
)


def filter_by_currency(info: List[Dict[str, dict]], value: str) -> Generator[str, None, None]:
    """Функция, которая принимает список словарей с банковскими операциями
    и возвращает итератор, который выдает по очереди операции, по заданной валюте"""
    for key in info:
        if key["currency_code"] == value:
            yield key


# usd_transactions = filter_by_currency(transactions, "RUB")
#
# for _ in range(3):
#     print(next(usd_transactions))


# print(len(transactions))
def transaction_descriptions(info: List[Dict[str, dict]]) -> Generator[str, None, None]:
    """Функция генератор, который принимает список словарей и
    возвращает описание каждой операции по очереди"""
    for key in info:
        yield key["description"]


# descriptions = transaction_descriptions(transactions)
#
# for _ in range(5):
#     print(next(descriptions))


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """Функция генератор номеров банковских карт, который генерирует номера  банковских
    карт в формате XXXX XXXX XXXX XXXX"""
    for number in range(start, end):
        card_number = str(number)
        while len(card_number) < 16:
            card_number = '0' + card_number
        formatted_card_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        yield formatted_card_number

# for card_num in card_number_generator(1, 9):
#     print(card_num)
