import json
from typing import Any, Dict, List


def read_transactions_from_json(json_file_path: str) -> List[Dict[str, Any]]:
    """Функция считывающая информацию JSON формата с заданного файла"""
    try:
        with open(json_file_path, encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
    except FileNotFoundError:
        return []


read_transactions_from_json('../data/operations.json')
