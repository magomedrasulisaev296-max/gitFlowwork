


def filter_by_state(transactions: list[dict], state: str = "EXECUTED") -> list[dict]:
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
            filtered_dicts.append(transactions[i])
    return filtered_dicts


def sort_by_date(transactions: list[dict], reverse: bool = True) -> list[dict]:
    """
    Сортирует список операций по дате.

    Args:
        transactions: список словарей с операциями
        reverse: порядок сортировки (True - убывание, False - возрастание)

    Returns:
        list: отсортированный список операций
    """
    return sorted(transactions, key=lambda x: x["date"], reverse=reverse)
