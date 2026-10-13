'''
Update the Villager class with a method print_inventory() that accepts no parameters except for self.

The method should print the name and quantity of each item in a villager’s furniture list.

The name and quantity should be in the format "item1: quantity, item2: quantity, item3: quantity" 
for however many unique items exist in the villager's furniture list
If the player has no items, the function should print "Inventory empty".

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
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

    def print_inventory(self):
        pass
