'''
Step 1: Copy the following code into your IDE.

Step 2: Instantiate an instance of the class Villager, which represents characters in Animal Crossing. 
Store the instance in a variable named apollo.

The Villager object created should have the name "Apollo", the species 
"Eagle", and the catchphrase "pah".

UPI Plan

UNDERSTAND:
Input - a Villager object and the name of the player to greet
Output - a greeting string in the format: "VillagerName: Hey there, PlayerName! How's it going, catchphrase!"
Edge Cases - if the player name is empty or the catchphrase is missing, the method should still format the string consistently

PLAN:
- Add a greet_player(self, player_name) method to the Villager class
- Use self.name for the villager's name
- Use self.catchphrase for the personalized greeting
- Return the formatted message as a string
- Create a second Villager named Bones with "Dog" and "yip yip"
- Call greet_player() with your name and print the result

IMPLEMENT:
- (implemented below)

'''


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