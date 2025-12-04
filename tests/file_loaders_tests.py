import unittest
from unittest.mock import patch, Mock

from src.files_loaders import read_csv_file, read_excel_file


class TestFileLoaders(unittest.TestCase):

    @patch('src.files_loaders.pd.read_csv')
    def test_csv(self, mock):
        mock.return_value = Mock()
        result = read_csv_file('test.csv')
        self.assertIsNotNone(result)
        mock.assert_called_once_with('test.csv')

    @patch('src.files_loaders.pd.read_excel')
    def test_excel(self, mock):
        mock.return_value = Mock()
        result = read_excel_file('test.xlsx')
        self.assertIsNotNone(result)
        mock.assert_called_once_with('test.xlsx')


if __name__ == '__main__':
    unittest.main()