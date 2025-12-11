import pytest  # type: ignore

from src.masks import *
from src.processing import *
from src.widget import *


def test_masks() -> None:
    assert get_mask_card_number("2200 4444 3535 8800") == "2200 44** **** 8800"
    assert get_mask_card_number("2200444435358800") == "2200 44** **** 8800"
    assert get_mask_card_number("2200 4444 3535 8800 6788") == "некоректнные входные данные"
    assert get_mask_card_number("2200 6788") == "некоректнные входные данные"

    assert get_mask_account("73654108430135874305") == "**4305"
    assert get_mask_account("7365 41 08430 13587 430 5") == "**4305"
    assert get_mask_account("73654108430135874305654") == "некоректнные входные данные"
    assert get_mask_account("7365410854") == "некоректнные входные данные"


@pytest.mark.parametrize("input_data, expected", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
    ("MasterCard 1234567812345678", "MasterCard 1234 56** **** 5678"),
    ("Счет 73654108430135874305", "Счет **4305"),
    ("счет 98765432109876543210", "счет **3210"),
    ("СЧЕТ 73654108430135874305", "СЧЕТ **4305"),
])
def test_mask_account_card_valid(input_data: str, expected: str) -> None:
    assert mask_account_card(input_data) == expected


@pytest.mark.parametrize("invalid_input", [
    "",
    "   ",
    "Visa Platinum",
    "Счет",
    "Visa Platinum 123",
])
def test_mask_account_card_invalid(invalid_input: str) -> None:
    result = mask_account_card(invalid_input)
    assert isinstance(result, str)


@pytest.mark.parametrize("input_date, expected", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2023-12-25T15:30:45.123456", "25.12.2023"),
    ("2024-01-01T00:00:00.000000", "01.01.2024"),
])
def test_get_date_valid(input_date: str, expected: str) -> None:
    assert get_date(input_date) == expected


@pytest.mark.parametrize("invalid_input", [
    "11.03.2024",
    "date.a.not",
    "",
    "11.03.2024T",
])
def test_get_date_invalid(invalid_input: str) -> None:
    assert get_date(invalid_input) == invalid_input


@pytest.mark.parametrize("transactions, state, expected", [
    ([
         {"state": "EXECUTED", "id": 1},
         {"state": "PENDING", "id": 2}
     ], "EXECUTED", [{"state": "EXECUTED", "id": 1}]),
    ([
         {"state": "CANCELED", "id": 1}
     ], "CANCELED", [{"state": "CANCELED", "id": 1}]),
    ([
         {"state": "PENDING", "id": 1}
     ], "EXECUTED", []),
    ([], "EXECUTED", []),
])
def test_filter_by_state(transactions: list, state: str, expected: list) -> None:
    assert filter_by_state(transactions, state) == expected


def test_sort_by_date() -> None:
    transactions = [
        {"date": "2024-01-01"},
        {"date": "2024-03-01"}
    ]

    result_desc = sort_by_date(transactions)
    assert result_desc[0]["date"] == "2024-03-01"

    result_asc = sort_by_date(transactions, False)
    assert result_asc[0]["date"] == "2024-01-01"