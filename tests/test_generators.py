from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency() -> None:
    transactions = [
        {"operationAmount": {"currency": {"code": "USD"}}},
        {"operationAmount": {"currency": {"code": "EUR"}}}
    ]
    result = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 1
    assert result[0]["operationAmount"]["currency"]["code"] == "USD"


def test_filter_by_currency_empty() -> None:
    transactions = [{"operationAmount": {"currency": {"code": "EUR"}}}]
    result = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 0


def test_transaction_descriptions() -> None:
    transactions = [
        {"description": "Test 1"},
        {"description": "Test 2"}
    ]
    gen = transaction_descriptions(transactions)
    assert next(gen) == "Test 1"
    assert next(gen) == "Test 2"


def test_card_number_generator() -> None:
    card = next(card_number_generator(1, 1))
    assert card == "0000 0000 0000 0001"


def test_card_number_generator_format() -> None:
    card = next(card_number_generator(1234567890123456, 1234567890123456))
    assert card == "1234 5678 9012 3456"