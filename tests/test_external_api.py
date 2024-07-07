from src.external_api import convert_amount_to_rubles

from unittest.mock import patch


@patch('requests.get')
def test_converting_amount_transaction(mock_get, info_trans):
    mock_get.return_value.json.return_value = 8228.59
    assert convert_amount_to_rubles(info_trans) == 8228.59
