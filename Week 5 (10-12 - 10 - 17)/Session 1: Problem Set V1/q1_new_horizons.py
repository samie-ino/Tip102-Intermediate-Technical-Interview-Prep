'''
Step 1: Copy the following code into your IDE.

Step 2: Instantiate an instance of the class Villager, which represents characters in Animal Crossing. 
Store the instance in a variable named apollo.

The Villager object created should have the name "Apollo", the species 
"Eagle", and the catchphrase "pah".

UPI Plan 

UNDERSTAND:
Input - name of character, species of character and catchpharse 
OUtput - name of character, species of character, catchpharse, furniture
Edge Cases - N/A

PLAN:
- create an instantiation of the instance of the class and add set parameters in it


IMPLEMENT: 
- (implemented below)

'''


class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []
