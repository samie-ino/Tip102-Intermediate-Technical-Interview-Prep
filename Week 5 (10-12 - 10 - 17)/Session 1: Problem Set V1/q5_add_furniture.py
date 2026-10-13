'''
layers and villagers in Animal Crossing can add furniture to their inventory to decorate their house.

Update the Villager class with a new method add_item() that takes in one parameter, item_name.

The method should validate the item_name.

If the item is valid, add item_name to the player’s furniture attribute.
The method does not need to return any values.
item_name is valid if it has one of the following values: "acoustic guitar", "ironwood kitchenette", 
"rattan armchair", "kotatsu", or "cacao tree".

UPI Plan 

UNDERSTAND:
Input - 
OUtput - 
Edge Cases -

PLAN:


IMPLEMENT: 
- (implemented below)



'''


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