'''
The Villager constructor has been updated to include an additional attribute neighbor. 
A villager's neighbor is another Villager instance and represents their closest neighbor. 
By default, a Villager's neighbor is set to None.

Given two Villager instances start_villager and target_villager, write a function message_received() 
that returns True if you can pass a message from the start_villager to the target_villager through a 
series of neighbors and False otherwise.

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
    def __init__(self, name, species, personality, catchphrase, neighbor=None):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
        self.neighbor = neighbor


def message_received(start_villager, target_villager):
    pass
