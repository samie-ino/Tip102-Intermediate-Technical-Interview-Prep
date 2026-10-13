# Problem 7: Group by Personality
# Return the names of villagers with the requested personality.


class Villager:
    def __init__(self, name, species, personality, catchphrase):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []


def of_personality_type(townies, personality_type):
    pass


if __name__ == "__main__":
    isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
    bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
    stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")
    print(of_personality_type([isabelle, bob, stitches], "Lazy"))