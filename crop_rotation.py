# === Stage 1: Каркас модуля ===
# Project: CropRotation
import random

Bed = namedtuple("Bed", ["name", "area", "crop", "season"])


def make_demo_beds():
    return [
        Bed("Северная", 2.5, "морковь", "осень"),
        Bed("Южная", 3.0, "томаты", "лето"),
        Bed("Западная", 1.8, "укроп", "лето"),
        Bed("Центральная", 4.0, "картофель", "лето"),
    ]


def report(beds):
    for bed in beds:
        print(f"Грядка «{bed.name}»: {bed.area} м², культура — {bed.crop}, сезон — {bed.season}")


if __name__ == "__main__":
    print("CropRotation: севооборот огорода")
    print("-" * 30)
    beds = make_demo_beds()
    print(f"Всего грядок: {len(beds)}")
    print()
    report(beds)
    print()
    print("Добро пожаловать в систему учёта севооборота!")
