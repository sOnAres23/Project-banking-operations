from src.generators import card_number_generator, filter_by_currency, transaction_descriptions, transactions


def test_filter_by_currency():
    generator = filter_by_currency(transactions, "USD")
    assert next(generator) == 939719570
    assert next(generator) == 142264268
    assert next(generator) == 895315941


def test_transaction_descriptions():
    generator = transaction_descriptions(transactions)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод с карты на карту"
    assert next(generator) == "Перевод организации"


def test_card_number_generator():
    generator = card_number_generator(1, 4)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"
