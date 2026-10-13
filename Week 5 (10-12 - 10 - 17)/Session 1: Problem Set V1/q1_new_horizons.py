# Problem 1: New Horizons
# Create a Villager instance named apollo with the values shown below.


class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []


apollo = Villager("Apollo", "Eagle", "pah")


if __name__ == "__main__":
    print(apollo.name)
    print(apollo.species)
    print(apollo.catchphrase)
    print(apollo.furniture)