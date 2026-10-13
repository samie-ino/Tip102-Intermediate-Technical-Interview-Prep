# Problem 6: Print Inventory
# Implement print_inventory() to display the quantity of each furniture item.


class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

    def print_inventory(self):
        pass


if __name__ == "__main__":
    alice = Villager("Alice", "Koala", "guvnor")
    alice.print_inventory()
    alice.furniture = ["acoustic guitar", "ironwood kitchenette", "kotatsu", "kotatsu"]
    alice.print_inventory()