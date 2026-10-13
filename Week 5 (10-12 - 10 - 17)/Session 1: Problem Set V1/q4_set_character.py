# Problem 4: Set Character
# Implement set_catchphrase() with the validation rules in the prompt.


class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

    def set_catchphrase(self, new_catchphrase):
        pass


if __name__ == "__main__":
    alice = Villager("Alice", "Koala", "guvnor")
    alice.set_catchphrase("sweet dreams")
    print(alice.catchphrase)
    alice.set_catchphrase("#?!")
    print(alice.catchphrase)