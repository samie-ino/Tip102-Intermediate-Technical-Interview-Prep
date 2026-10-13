# Problem 2: Greet Player
# Add greet_player() and create bones as a Villager instance.


class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

    def greet_player(self, player_name):
        pass


bones = Villager("Bones", "Dog", "yip yip")


if __name__ == "__main__":
    print(bones.greet_player("Samia"))