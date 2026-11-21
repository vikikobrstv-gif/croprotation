# === Stage 9: Сортировка записей ===
# Project: CropRotation
sort_growbeds.py

from datetime import datetime


def parse_date(value):
    """Преобразует строку даты в объект datetime для сравнения."""
    if isinstance(value, datetime):
        return value
    return datetime.strptime(value, "%Y-%m-%d")


def sort_growbeds(growbeds, by="name", ascending=True):
    """Сортирует список записей «грядка» по указанному полю.

    Поле name — строка, сравнивается лексикографически.
    Поле created — дата в формате YYYY-MM-DD, сравнивается по хронологии.
    Направление — возрастание или убывание.
    """
    key_map = {
        "name": lambda gb: str(gb["name"]).lower(),
        "created": lambda gb: parse_date(gb["created"]),
    }

    if by not in key_map:
        raise ValueError("Неизвестное поле для сортировки: {}".format(by))

    key_func = key_map[by]

    return sorted(growbeds, key=key_func, reverse=not ascending)


def sort_by_created(growbeds, ascending=True):
    """Специальная обёртка для сортировки по дате создания грядки."""
    return sort_growbeds(growbeds, by="created", ascending=ascending)
