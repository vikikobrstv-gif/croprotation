# === Stage 5: Удаление и восстановление ===
# Project: CropRotation
def soft_delete_garden(garden, garden_store, recovery_log):
    """Мягкое удаление грядки: сохраняем данные и помечаем как удалённые."""
    if garden is None:
        return False
    recovery_log.append({"name": garden.name, "area": garden.area, "crop": garden.crop, "season": garden.season})
    garden.deleted = True
    return True


def restore_garden(garden, garden_store):
    """Восстановить удалённую грядку."""
    if garden.deleted:
        garden.deleted = False
        garden_store.add_garden(garden)
        return True
    return False


def delete_garden(garden, garden_store):
    """Удалить грядку из списка с возможностью восстановления."""
    if garden is None:
        return False
    garden_store.remove_garden(garden)
    return True


class GardenStore:
    def __init__(self):
        self.gardens = []
        self.recovery_log = []

    def add_garden(self, garden):
        self.gardens.append(garden)

    def remove_garden(self, garden):
        if garden in self.gardens:
            self.gardens.remove(garden)

    def get_active_gardens(self):
        return [g for g in self.gardens if not g.deleted]

    def get_deleted_gardens(self):
        return [g for g in self.gardens if g.deleted]

    def restore_all(self):
        for garden in self.gardens:
            if garden.deleted:
                garden.deleted = False
        return True


class Garden:
    def __init__(self, name, area, crop, season):
        self.name = name
        self.area = area
        self.crop = crop
        self.season = season
        self.deleted = False

    def __repr__(self):
        return f"Garden(name={self.name}, area={self.area}, crop={self.crop}, season={self.season}, deleted={self.deleted})"


if __name__ == "__main__":
    store = GardenStore()
    g1 = Garden("Грядка 1", 5, "томат", "лето")
    g2 = Garden("Грядка 2", 3, "морковь", "осень")
    store.add_garden(g1)
    store.add_garden(g2)
    print("Активные:", store.get_active_gardens())
    soft_delete_garden(g1, store, store.recovery_log)
    print("После удаления:", store.get_active_gardens())
    print("Удалённые:", store.get_deleted_gardens())
    restore_garden(g1, store)
    print("После восстановления:", store.get_active_gardens())
