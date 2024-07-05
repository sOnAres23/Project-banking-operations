import json
import os
from typing import Any, Dict, List

from src.utils import read_transactions_from_json


def test_read_transactions_from_json_success():
    with open('../data/operations.json', encoding='utf-8') as json_file:
        data = json.load(json_file)
    file_path = '../data/operations.json'
    result = read_transactions_from_json(file_path)
    assert result == data


def test_read_transactions_from_json_file_not_found():
    result = read_transactions_from_json('non_existing_file.json')
    assert result == []
