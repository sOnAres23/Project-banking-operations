import os
import requests
from typing import Any, Dict

from dotenv import load_dotenv

load_dotenv('../.env')


def convert_amount_to_rubles(transaction: Dict[str, Any]) -> float:
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции
    в RUB, если транзакция была в USD или EUR, происходит обращение к внешнему API
    для получения текущего курса валют и конвертации суммы операции в рубли"""
    amount = float(transaction['operationAmount']['amount'])
    currency = transaction['operationAmount']['currency']['code']

    if currency == 'RUB':
        return amount
    elif currency in ['USD', 'EUR']:
        api_key = os.getenv('API_KEY')
        response = requests.get(
            'https://api.apilayer.com/exchangerates_data/convert',
            headers={'apikey': api_key},
            params={'from': currency, 'to': 'RUB', 'amount': amount}
        )

        if response.status_code == 200:
            data = response.json()
            if 'result' in data:
                amount = data['result']
            else:
                raise ValueError(f'Exchange rate for {currency} not found in API response')

    return amount


transaction = {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }

print(convert_amount_to_rubles(transaction))
