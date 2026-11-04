# === Stage 2: Проверка полей ===
# Project: CropRotation
import re


def normalize_field_value(value):
    if value is None:
        return ""
    text = str(value).strip()
    if text == "":
        return ""
    return text.title()


def normalize_area(value):
    if value is None:
        return 0.0
    try:
        return float(str(value).replace(",", ".").strip())
    except ValueError:
        return 0.0


def normalize_season(value):
    if value is None:
        return ""
    text = str(value).strip().lower()
    valid = {
        "весна",
        "лето",
        "осень",
        "зима",
        "весенне-летняя",
        "летне-осенняя",
        "осенне-зимняя",
    }
    return text if text in valid else ""


def validate_name(name):
    if not name:
        return "Название грядки не может быть пустым."
    if len(name) > 50:
        return "Название грядки не должно превышать 50 символов."
    if not re.search(r"[А-Яа-яA-Za-z0-9 _-]", name):
        return "Название грядки содержит недопустимые символы."
    return None


def validate_area(area):
    if area < 0:
        return "Площадь грядки не может быть отрицательной."
    if area != area and area != 0:  # float('nan')
        return "Площадь грядки должна быть числом."
    if area > 1000:
        return "Площадь грядки не должна превышать 1000 квадратных метров."
    return None


def validate_crop(crop):
    if not crop:
        return "Культура не может быть пустой."
    if len(crop) > 40:
        return "Наименование культуры не должно превышать 40 символов."
    return None


def validate_season(season):
    if not season:
        return "Сезон посадки не может быть пустым."
    valid = {
        "весна",
        "лето",
        "осень",
        "зима",
        "весенне-летняя",
        "летне-осенняя",
        "осенне-зимняя",
    }
    if str(season).strip().lower() not in valid:
        return "Неверный сезон. Допустимые значения: весна, лето, осень, зима, весенне-летняя, летне-осенняя, осенне-зимняя."
    return None


def validate_bed(fields):
    errors = []
    name_error = validate_name(fields.get("name"))
    if name_error:
        errors.append(name_error)

    area_error = validate_area(fields.get("area"))
    if area_error:
        errors.append(area_error)

    crop_error = validate_crop(fields.get("crop"))
    if crop_error:
        errors.append(crop_error)

    season_error = validate_season(fields.get("season"))
    if season_error:
        errors.append(season_error)

    return errors
