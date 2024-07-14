from src.readers import read_transactions_from_csv, read_transactions_from_xlsx
from unittest.mock import patch, mock_open, Mock
import pandas as pd


@patch("tests.test_readers.pd.read_csv")
def test_read_transactions_from_csv(test_info_csv):
    Mock.return_value = pd.DataFrame()
    assert read_transactions_from_csv(test_info_csv) == []


@patch("tests.test_readers.pd.read_excel")
def test_read_transactions_from_xlsx(mock_read_excel):
    mock_df = pd.DataFrame(
        {'id': [650703, 593027], 'state': ['EXECUTED', 'CANCELED']}
    )
    mock_read_excel.return_value = mock_df

    result = read_transactions_from_xlsx('../data/transactions_excel.xlsx')

    assert result == [
        {'id': 650703, 'state': 'EXECUTED'},
        {'id': 593027, 'state': 'CANCELED'}
    ]
    mock_read_excel.assert_called_once_with('../data/transactions_excel.xlsx')
