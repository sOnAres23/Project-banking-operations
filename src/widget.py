from src import masks
import logging


# """Создаем логгер для логирования функций и записываем логи в директорию logs"""
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s: %(name)s %(funcName)s - %(levelname)s - %(message)s',
#                     filename='../logs/widget.log', # Запись логов в файл
#                     filemode='w') # Перезапись файла при каждом запуске
logger = logging.getLogger("widget.py")


def mask_account_card(client_information: str) -> str:
    """Функция, которая принимает номера счёта или название и номер карты
    и возвращает строку с названием и с замаскированным номером карты или счета"""

    if "Счет" in client_information:
        logger.info("Маскировка счёта клиента")
        return client_information[:-20] + masks.get_mask_account(client_information)
    else:
        logger.info("Маскировка карты клиента")
        name = client_information[-16:]
        new_name = masks.get_mask_card_number(name)
        new_card = client_information[:-16] + new_name
        return new_card


if __name__ == "__main__":
    print(mask_account_card("Счет 73654108430135872304"))
    print(mask_account_card("Visa Gold 5999414228426358"))


def get_data(date: str) -> str:
    logger.info("Преобразование даты операции")
    """Функция которая принимает строку с данными даты/времени
    и возвращает строку с преобразованием даты"""
    new_date = f"{date[8:10]}.{date[5:7]}.{date[:4]}"
    return new_date


if __name__ == "__main__":
    print(get_data("2018-07-11T02:26:18.671407"))
