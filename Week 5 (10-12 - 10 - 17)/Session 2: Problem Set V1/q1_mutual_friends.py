# Problem 1: Mutual Friends
# In the Villager class below, each villager has a friends attribute, which is a list of other
# villagers they are friends with.
# Write a method get_mutuals() that takes one parameter, a Villager instance new_contact,
# and returns a list with the name of all friends the current villager and new_contact have in common.


class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.friends = []

    def get_mutuals(self, new_contact):
        pass
