from src.dictionary import *
import random
from typing import Generator, Dict, Any


def filter_by_currency(transactions_list: list, currency: str = "USD") -> Generator[Dict[str, Any], None, None]:
    '''поочередно возврощает библеотеку с транзакцией если переменная "code" равна задаваемой переменной "currency"'''
    for transaction in transactions_list:
        if transaction.get("currency") == currency:
            yield transaction
        elif "operationAmount" in transaction:
            if transaction["operationAmount"]["currency"]["code"] == currency:
                yield transaction


currency_gen = filter_by_currency(transactions, "USD")
print(next(currency_gen))
print(next(currency_gen))
print(next(currency_gen))


def transaction_descriptions(transactions_list: list) -> Generator[str, None, None]:
    '''поочередно возврощает информация о транзакции'''
    for i in range(len(transactions_list)):
        yield transactions_list[i]["description"]


generator = transaction_descriptions(transactions)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))


def card_number_generator(start: int = 1, end: int = 9999999999999999) -> Generator[str, None, None]:
    '''генерирует случайный номер банковской карты взависимости от указанных значений'''
    number = random.randint(start, end)
    number_str = str(number).zfill(16)
    formatted = f"{number_str[:4]} {number_str[4:8]} {number_str[8:12]} {number_str[12:16]}"
    yield formatted


print(next(card_number_generator(1, 100)))
print(next(card_number_generator(1, 1)))