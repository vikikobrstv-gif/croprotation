# === Stage 4: Редактирование записей ===
# Project: CropRotation
from copy import deepcopy


ALLOWED_FIELDS = ("name", "area", "crop", "season")


class BedError(Exception):
    """Ошибка редактирования грядки."""


def edit_bed(bed, changes):
    """Редактирует грядку по идентификатору.

    Проверяет, что меняются только допустимые поля, и что значения
    соответствуют типу исходного описания грядки. Возвращает
    обновлённую копию грядки.

    Сущность «грядка» описывается полями:
      name  - строка (название)
      area  - число (площадь)
      crop  - строка (культура)
      season - строка (сезон)
    """
    if not isinstance(changes, dict):
        raise BedError("Изменения должны быть словарём")

    unknown = set(changes) - ALLOWED_FIELDS
    if unknown:
        raise BedError("Недопустимые поля: " + ", ".join(sorted(unknown)))

    new_bed = deepcopy(bed)
    for field, value in changes.items():
        current = new_bed.__dict__.get(field, None)
        if not _is_valid_value(field, value, current):
            raise BedError(
                "Недопустимое значение для поля " + repr(field) +
                ": " + repr(value))
        setattr(new_bed, field, value)
    return new_bed


def _is_valid_value(field, value, current):
    if field == "name" or field == "crop" or field == "season":
        return isinstance(value, str)
    if field == "area":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    return True


class Bed:
    """Грядка огорода."""

    def __init__(self, name, area, crop, season):
        self.name = name
        self.area = area
        self.crop = crop
        self.season = season

    def __repr__(self):
        return "Bed(name={!r}, area={!r}, crop={!r}, season={!r})".format(
            self.name, self.area, self.crop, self.season)


if __name__ == "__main__":
    bed = Bed("Рассада", 0.5, "томат", "весна")
    updated = edit_bed(bed, {"crop": "огурец"})
    print("Изменено:", updated)

    try:
        edit_bed(bed, {"area": "много"})
    except BedError as exc:
        print("Ошибка:", exc)

    try:
        edit_bed(bed, {"weird": "поле"})
    except BedError as exc:
        print("Ошибка:", exc)
