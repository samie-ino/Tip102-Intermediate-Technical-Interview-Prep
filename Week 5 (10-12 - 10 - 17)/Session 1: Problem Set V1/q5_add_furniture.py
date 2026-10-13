# Problem 5: Add Furniture
# Implement add_item() to add only valid furniture to the inventory.


class Villager:
    VALID_ITEMS = {
        "acoustic guitar",
        "ironwood kitchenette",
        "rattan armchair",
        "kotatsu",
        "cacao tree",
    }

    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

    def add_item(self, item_name):
        pass


if __name__ == "__main__":
    alice = Villager("Alice", "Koala", "guvnor")
    alice.add_item("acoustic guitar")
    print(alice.furniture)