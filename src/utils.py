import json
import logging
from typing import Any, Dict, List

"""Создаем логгер для логирования функций и записываем логи в директорию logs"""
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s: %(name)s %(funcName)s - %(levelname)s - %(message)s',
                    filename='../logs/utils.log', # Запись логов в файл
                    filemode='w') # Перезапись файла при каждом запуске
logger = logging.getLogger("utils.py")


def read_transactions_from_json(json_file_path: str) -> List[Dict[str, Any]]:
    """Функция считывающая информацию JSON формата с заданного файла"""
    try:
        logger.info("Открываем файл...")
        with open(json_file_path, encoding='utf-8') as file:
            data = json.load(file)
            logger.info("Cмотрим содержимое файла, ждем формат list()")
            if isinstance(data, list):
                logger.info("Файл корректный, возвращаем его содержимое")
                return data
            else:
                logger.warning("Файл не формата list()")
                return []
    except FileNotFoundError:
        logger.warning("Файл не найден, неверный путь до файла")
        return []


read_transactions_from_json("../data/operations.json")
