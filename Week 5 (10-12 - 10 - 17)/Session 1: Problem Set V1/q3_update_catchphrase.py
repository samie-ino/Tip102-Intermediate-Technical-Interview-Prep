'''
In Animal Crossing, as players become friends with villagers, the villagers might ask the player to suggest a new catchphrase.

Adding on to your existing code, update bones so that his catchphrase is "ruff it up" instead of its current value, "yip yip".


UPI Plan

UNDERSTAND:
Input - a Villager object and a new catchphrase
Output - the villager's catchphrase is updated to the new value
Edge Cases - if the catchphrase is changed to something like "ruff it up", the greeting should reflect the updated value

PLAN:
- Start with the Villager class from the previous question
- Create a Bones villager with the original catchphrase "yip yip"
- Update the catchphrase attribute to "ruff it up"
- Print the greeting using the updated catchphrase

IMPLEMENT:
- (implemented below)

'''


class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []
    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"


apollo = Villager("Apollo", "Eagle", "pah")
bones = Villager("Bones", "Dog", "ruf it up!")


if __name__ == "__main__":
    print(apollo.name)
    print(apollo.species)
    print(apollo.catchphrase)
    print(apollo.furniture)
    print(bones.greet_player("Samia"))