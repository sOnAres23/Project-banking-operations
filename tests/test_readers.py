from src.readers import read_transactions_from_csv, read_transactions_from_xlsx
from unittest.mock import patch, mock_open, Mock
import pandas as pd


@patch("tests.test_readers.pd.read_csv")
def test_read_transactions_from_csv(test_info_csv):
    Mock.return_value = pd.DataFrame()
    assert read_transactions_from_csv('foo') == []

    info_csv = read_transactions_from_csv("../data/transactions.csv")
    assert info_csv[0] == test_info_csv


@patch("tests.test_readers.pd.read_excel")
def test_read_transactions_from_xlsx(test_info_xlcx):
    Mock.return_value = pd.DataFrame()
    assert read_transactions_from_xlsx('foo') == []

    info_xlsx = read_transactions_from_xlsx("../data/transactions_excel.xlsx")
    assert info_xlsx[0] == test_info_xlcx
