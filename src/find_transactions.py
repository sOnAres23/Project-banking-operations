import json
import re
from collections import Counter


def find_transactions(list_of_operations: list[dict], enter_user: str) -> list[dict]:
    """
    Функция, которая принимает список с данными о банковских операциях и строку поиска,
    и возвращает список словарей, у которых в описании есть данная строка.
    """
    new_list_filter = []
    for operation in list_of_operations:
        if "description" in operation and re.search(enter_user, operation["description"], flags=re.IGNORECASE):
            new_list_filter.append(operation)

    return new_list_filter


def filtering_operations(list_of_operations: list[dict], list_of_categories: list) -> dict:
    """
    Функция, которая принимает список с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории.
    """
    filter_ = [operation["description"] for operation in list_of_operations if operation.get("description", "") in list_of_categories]

    return dict(Counter(filter_))


if __name__ == "__main__":
    with open("../data/operations.json", encoding="UTF-8") as f:
        operations = json.load(f)

# print(find_transactions(operations, "открытие"))
