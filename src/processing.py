def filter_by_state(dicts_, state='EXECUTED'):
    filtered_dicts = []
    for i in range(len(dicts_)):
        if dicts_[i]['state'] == state:
            filtered_dicts += [dicts_[i]]
    return filtered_dicts
print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                       {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], state='EXECUTED'))


def sort_by_date(dicts_, reverse=True):
    """
    Сортирует список операций по дате.

    Args:
        transactions: список словарей с операциями
        reverse: порядок сортировки (True - убывание, False - возрастание)

    Returns:
        list: отсортированный список операций
    """
    return sorted(dicts_, key=lambda x: x['date'], reverse=reverse)

print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], reverse=True))










    #if sort_type == 'Decrease':
     #   for i in range(len(dicts_)):
