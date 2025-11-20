import unittest
from unittest.mock import patch, mock_open
import json

from src.UTILS import load_transactions


class TestLoadTransactions(unittest.TestCase):

    @patch('os.path.exists', return_value=True)
    @patch('builtins.open', mock_open(read_data='[{"id": 1}, {"id": 2}]'))
    def test_success(self, mock_exists):
        result = load_transactions("data/transactions.json")
        self.assertEqual(result, [{"id": 1}, {"id": 2}])

    @patch('os.path.exists', return_value=False)
    def test_file_not_found(self, mock_exists):
        result = load_transactions("data/transactions.json")
        self.assertEqual(result, [])

    @patch('os.path.exists', return_value=True)
    @patch('builtins.open', mock_open(read_data='invalid json'))
    def test_json_error(self, mock_exists):
        result = load_transactions("data/transactions.json")
        self.assertEqual(result, [])

    @patch('os.path.exists', return_value=True)
    @patch('builtins.open', mock_open(read_data='{"id": 1}'))
    def test_not_list(self, mock_exists):
        result = load_transactions("data/transactions.json")
        self.assertEqual(result, [])

    @patch('os.path.exists', return_value=True)
    @patch('builtins.open', mock_open(read_data=''))
    def test_empty_file(self, mock_exists):
        result = load_transactions("data/transactions.json")
        self.assertEqual(result, [])