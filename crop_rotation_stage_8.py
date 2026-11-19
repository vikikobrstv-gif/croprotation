# === Stage 8: Генерация идентификаторов ===
# Project: CropRotation
import uuid

PROJECT_PREFIX = "CR"


def generate_unique_id():
    """Генерация уникального идентификатора с префиксом проекта и проверкой коллизий."""
    used_ids = set()

    def is_unique(candidate):
        return candidate not in used_ids

    def generate():
        while True:
            candidate = f"{PROJECT_PREFIX}-{uuid.uuid4().hex[:8]}"
            if is_unique(candidate):
                used_ids.add(candidate)
                return candidate

    return generate()


def main():
    id1 = generate_unique_id()
    id2 = generate_unique_id()
    print(f"Первый идентификатор: {id1}")
    print(f"Второй идентификатор: {id2}")
    print(f"Уникальны: {id1 != id2}")


if __name__ == "__main__":
    main()
