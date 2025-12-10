import re
import pandas as pd
import random
from collections import Counter
from src.files_loaders import read_excel_file
from src.dictionary import transactions


def process_bank_search(dict_: list[dict], string_for_search: str) -> list[dict]:
    transactions = []
    for i in dict_:
        if string_for_search in i["description"]:
            transactions.append(i)
        else:
            print("check your string for search")
    return transactions


def process_bank_operations(dict_:list[dict], categories:list)->dict:
    transactions = []
    for i in dict_:
        if i["description"] in categories:
            transactions.append(i["description"])
    return dict(Counter(transactions))













