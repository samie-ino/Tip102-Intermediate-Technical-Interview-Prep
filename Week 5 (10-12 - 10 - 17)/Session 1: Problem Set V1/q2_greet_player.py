'''
Step 1: Using the Villager class from Problem 1, add the following greet_player() method to your existing code:

def greet_player(self, player_name):
    pass
Step 2: Create a second instance of Villager in a variable named bones.

The Villager object created should have name "Bones", species "Dog", and catchphrase "yip yip".
Step 3: Call the method greet_player() with your name and print out "Bones: Hey there, <your name>! 
How's it going, yip yip!". For example, if your name is Tram, "Bones: Hey there, Tram! How's it going, yip yip?" 
would be printed out to the console.

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
    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"


apollo = Villager("Apollo", "Eagle", "pah")
bones = Villager("Bones", "Dog", "yip yip")


if __name__ == "__main__":
    print(apollo.name)
    print(apollo.species)
    print(apollo.catchphrase)
    print(apollo.furniture)
    print(bones.greet_player("Apollo"))