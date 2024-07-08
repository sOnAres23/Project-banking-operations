import logging

"""Создаем логгер для логирования функций и записываем логи в директорию logs"""
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s: %(name)s %(funcName)s - %(levelname)s - %(message)s',
                    filename='../logs/masks.log', # Запись логов в файл
                    filemode='w') # Перезапись файла при каждом запуске
logger = logging.getLogger("masks.py")


def get_mask_card_number(card_number: str) -> str | None:
    """Функция, которая принимает номер карты и
    возвращает маскированный номер карты пользователя"""

    logger.info("Маскировка карты клиента")

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(bank_account: str) -> str | None:
    """Функция, которая принимает номер счета и
    возвращает маскированный номер счета пользователя"""

    logger.info("Маскировка номера счёта клиента")

    return f"**{bank_account[-4:]}"


if __name__ == "__main__":
    print(get_mask_card_number("7000792289606368"))
if __name__ == "__main__":
    print(get_mask_account("73654108430135874305"))
