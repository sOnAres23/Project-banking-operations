from typing import Any


def filter_by_state(info_users: list[dict], state: str = "EXECUTED") -> list[dict]:
    """ Функция, которая возвращает список словарей, по параметру 'state' """
    sort_info_users = []
    for info in info_users:
        if info["state"] == state:
            sort_info_users.append(info)

    return sort_info_users


def sort_by_date(info_dicts: list[dict], sorting_parameter: Any = None) -> list[dict]:
    """Функция,которая сортирует список словарей по параметру 'date',
    если второй аргумент True, то от самой новой даты до старой, если False - наоборот """
    if sorting_parameter is not None:
        return sorted(info_dicts, key=lambda date: date["date"])
    else:
        return sorted(info_dicts, key=lambda date: date["date"], reverse=True)


# print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#                        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#                        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#                        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))

# print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#                     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#                     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#                     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
