import unittest
from unittest.mock import MagicMock, patch

from src.external_api import get_transaction_amount_in_rub  # правильный импорт


class TestGetAmountInRub(unittest.TestCase):

    def test_rub_currency(self):
        transaction = {"amount": "1000.50", "currency": "RUB"}
        result = get_transaction_amount_in_rub(transaction)
        self.assertEqual(result, 1000.50)

    @patch('src.external_api.requests.get')  # правильный путь
    def test_usd_success(self, mock_get):
        transaction = {"amount": "100", "currency": "USD"}
        mock_get.return_value.json.return_value = {"success": True, "result": 7500.50}

        result = get_transaction_amount_in_rub(transaction)
        self.assertEqual(result, 7500.50)

    @patch('src.external_api.requests.get')  # правильный путь
    def test_api_failure(self, mock_get):
        transaction = {"amount": "50", "currency": "EUR"}
        mock_get.return_value.json.return_value = {"success": False}

        result = get_transaction_amount_in_rub(transaction)
        self.assertEqual(result, 50.0)

    @patch('src.external_api.requests.get')  # правильный путь
    def test_network_error(self, mock_get):
        transaction = {"amount": "200", "currency": "USD"}
        mock_get.side_effect = Exception("Network error")

        result = get_transaction_amount_in_rub(transaction)
        self.assertEqual(result, 200.0)

    def test_unknown_currency(self):
        transaction = {"amount": "500", "currency": "GBP"}
        result = get_transaction_amount_in_rub(transaction)
        self.assertEqual(result, 500.0)

    def test_missing_fields(self):
        result = get_transaction_amount_in_rub({})
        self.assertEqual(result, 0.0)