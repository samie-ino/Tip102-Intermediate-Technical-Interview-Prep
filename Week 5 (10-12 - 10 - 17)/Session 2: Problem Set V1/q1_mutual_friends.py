'''
 Problem 1: Mutual Friends
 In the Villager class below, each villager has a friends attribute, which is a list of other
 villagers they are friends with.
 Write a method get_mutuals() that takes one parameter, a Villager instance new_contact,
 and returns a list with the name of all friends the current villager and new_contact have in common.


UPI Plan

UNDERSTAND:
Input - Given a class with a given friend list
Output - A list of mutual friends that are new and common
Edge Cases - N/A

PLAN:
- Create an empty list to hold the mutual friend names
- Iterate through each friend in self.friends
- Check whether the same friend object is also in new_contact.friends
- If it is, append the friends name to the result
- Return the result

IMPLEMENT:
- Code Below!

 '''


class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.friends = []

    def get_mutuals(self, new_contact):
        mutuals = []
        
        for friend in self.friends:
            if friend in new_contact.friends:
                mutuals.append(friend.name)
        return mutuals
    
bob = Villager("Bob", "Cat", "pthhhpth")
marshal = Villager("Marshal", "Squirrel", "sulky")
ankha = Villager("Ankha", "Cat", "me meow")
fauna = Villager("Fauna", "Deer", "dearie")
raymond = Villager("Raymond", "Cat", "crisp")
stitches = Villager("Stitches", "Cub", "stuffin")

bob.friends = [stitches, raymond, fauna]
marshal.friends = [raymond, ankha, fauna]
print(bob.get_mutuals(marshal))

ankha.friends = [marshal]
print(bob.get_mutuals(ankha))