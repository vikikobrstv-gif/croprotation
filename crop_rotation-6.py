# === Stage 6: Связанная сущность ===
# Project: CropRotation
"""Модуль посадок для проекта CropRotation.

Посадка связана с грядкой по идентификатору. Каждая посадка имеет свою
дату посадки, урожайность и статус.
"""

from datetime import date


class Planting:
    """Представляет одну посадку на грядке."""

    def __init__(self, bed_id, crop_name, planting_date,
                 expected_yield, status="grown"):
        self.bed_id = bed_id
        self.crop_name = crop_name
        self.planting_date = planting_date
        self.expected_yield = expected_yield
        self.status = status

    def __repr__(self):
        return (f"Planting(bed_id={self.bed_id}, crop='{self.crop_name}', "
                f"date={self.planting_date}, yield={self.expected_yield}, "
                f"status='{self.status}')")


def add_planting(plantings, bed_id, crop_name, planting_date,
                 expected_yield, status="grown"):
    """Добавляет посадку в список и возвращает её объект.

    Args:
        plantings: список уже существующих посадок.
        bed_id: идентификатор грядки, на которой произведена посадка.
        crop_name: название культуры.
        planting_date: дата посадки в формате date.
        expected_yield: ожидаемый урожай.
        status: статус посадки, по умолчанию 'grown'.

    Returns:
        Созданный объект Planting.
    """
    planting = Planting(bed_id, crop_name, planting_date,
                        expected_yield, status)
    plantings.append(planting)
    return planting


def get_plantings_for_bed(plantings, bed_id):
    """Возвращает список посадок, принадлежащих указанной грядке."""
    return [p for p in plantings if p.bed_id == bed_id]


def get_total_yield(plantings, bed_id):
    """Возвращает суммарный ожидаемый урожай для грядки."""
    return sum(p.expected_yield for p in get_plantings_for_bed(plantings, bed_id))
