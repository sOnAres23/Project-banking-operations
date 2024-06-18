from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(number_card):
    assert get_mask_card_number("7000792289606368") == number_card


def test_get_mask_account(number_account):
    assert get_mask_account("73654108430135874305") == number_account
