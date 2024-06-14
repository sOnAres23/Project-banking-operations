def get_mask_card_number(card_number: str) -> str | None:
    """Функция маскирующая номер карты пользователя"""
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(bank_account: str) -> str | None:
    """Функция маскирующая номер счёта пользователя"""
    return f"**{bank_account[-4:]}"


if __name__ == "__main__":
    print(get_mask_card_number("7000792289606368"))
if __name__ == "__main__":
    print(get_mask_account("73654108430135874305"))
