from src.data import *
import random

def filter_by_currency(transactions_list, currency="USD"):
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


def transaction_descriptions(transactions_list):
    '''поочередно возврощает информация о транзакции'''
    for i in range(len(transactions_list)):
        yield transactions_list[i]["description"]


generator = transaction_descriptions(transactions)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))


def card_number_generator(start=1, end=9999999999999999):
    '''генерирует случайный номер банковской карты взависимости от указанных значений'''
    number = random.randint(start, end)
    number_str = str(number).zfill(16)
    formatted = f"{number_str[:4]} {number_str[4:8]} {number_str[8:12]} {number_str[12:16]}"
    yield formatted


# Примеры использования
print(generate_card_number(1, 100))
print(generate_card_number(1, 1))