import random
from typing import Any, Dict, Generator

from src.dictionary import *


def filter_by_currency(transactions_list: list, currency: str = "USD") -> Generator[Dict[str, Any], None, None]:
    '''поочередно возврощает библеотеку с транзакцией если переменная "code" равна задаваемой переменной "currency"'''
    for transaction in transactions_list:
        if transaction.get("currency") == currency:
            yield transaction
        elif "operationAmount" in transaction:
            if transaction["operationAmount"]["currency"]["code"] == currency:
                yield transaction






def transaction_descriptions(transactions_list: list) -> Generator[str, None, None]:
    '''поочередно возврощает информация о транзакции'''
    for i in range(len(transactions_list)):
        yield transactions_list[i]["description"]







def card_number_generator(start: int = 1, end: int = 9999999999999999) -> Generator[str, None, None]:
    '''генерирует случайный номер банковской карты взависимости от указанных значений'''
    number = random.randint(start, end)
    number_str = str(number).zfill(16)
    formatted = f"{number_str[:4]} {number_str[4:8]} {number_str[8:12]} {number_str[12:16]}"
    yield formatted


