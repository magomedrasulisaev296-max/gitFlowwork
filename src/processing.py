from typing import Dict, List


def filter_by_state(transactions: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
     фильтрует список операций по статусу.

    Args:
        transactions: список словарей с операциями
        state: статус операции по которуму будет фильтроваться список транзакций

    Returns:
        list: отфильтрованный список транзакций
    """
    filtered_dicts = []
    for i in range(len(transactions)):
        if transactions[i]["state"] == state:
            filtered_dicts += [transactions[i]]
    return filtered_dicts


def sort_by_date(transactions: List[Dict], reverse: bool = True) -> List[Dict]:
    """
    Сортирует список операций по дате.

    Args:
        transactions: список словарей с операциями
        reverse: порядок сортировки (True - убывание, False - возрастание)

    Returns:
        list: отсортированный список операций
    """
    return sorted(transactions, key=lambda x: x["date"], reverse=reverse)
