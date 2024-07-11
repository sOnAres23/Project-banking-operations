import csv
import logging

from typing import Any, Dict, List

import pandas as pd

"""Создаем логгер для логирования функций и записываем логи в директорию logs"""
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s: %(name)s %(funcName)s - %(levelname)s - %(message)s',
                    filename='../logs/readers.log',  # Запись логов в файл
                    filemode='w')  # Перезапись файла при каждом запуске
logger = logging.getLogger("readers.py")


def read_transactions_from_csv(file_path: str) -> List[Dict[str, Any]]:
    """Функция считывающая информацию CSV формата с заданного файла,
    и возвращающая список словарей с данными"""
    transactions = []
    try:
        logger.info("Открываем файл...")
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            logger.info("Файл корректный, возвращаем его содержимое")
            for row in reader:
                transactions.append(dict(row))

        return transactions

    except FileNotFoundError:
        logger.warning("Файл не найден, неверный путь до файла")
        return []


def read_transactions_from_xlsx(file_path: str) -> List[Dict[str, Any]]:
    """Функция считывающая информацию XLSX формата с заданного файла,
    и возвращающая список словарей с данными"""
    transactions = []
    try:
        logger.info("Открываем файл...")
        excel_transactions = pd.read_excel(file_path).head()
        logger.info("Файл корректный, возвращаем его содержимое")
        for index, row in excel_transactions.iterrows():
            transactions.append(dict(row))

        return transactions

    except FileNotFoundError:
        logger.warning("Файл не найден, неверный путь до файла")
        return []


print(read_transactions_from_csv("../data/transactions.csv"))
print(read_transactions_from_xlsx("../data/transactions_excel.xlsx"))

# В других частях  проекта, где нужно считать данные из CSV
# или XLSX файлов, импортировать эти функции следующим образом:
#
# from readers import read_transactions_from_csv, read_transactions_from_xlsx
