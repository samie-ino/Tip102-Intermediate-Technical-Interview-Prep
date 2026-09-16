"""Question 1: Write a function welcome() that prints the string,
 Welcome to The Hundred Acre Wood!"""
def welcome():
    print("Welcome to The Hundred Acre Wood!")

welcome()

"""Question 2: Write a function greeting() that accepts a single parameter, 
  a string name, and prints the string "Welcome to The Hundred Acre Wood <name>! 
  My name is Christopher Robin."""

def greeting(name):
    print(f"Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin.")    

greeting("Winnie the Pooh")

"""Question 3: Write a function print_catchphrase() that accepts a string character as a parameter and prints the catchphrase 
of the given character as outlined in the table below.

Character	Catchphrase
"Pooh"	"Oh bother!"
"Tigger"	"TTFN: Ta-ta for now!"
"Eeyore"	"Thanks for noticing me."
"Christopher Robin"	"Silly old bear."
"""


def print_catchphrase(character):
    
    if character == "Pooh":
        print("Oh bother!")
    elif character == "Tigger":
        print("TTFN: Ta-ta for now!")
    
    elif character == "Eeyore":
        print("Thanks for noticing me!")
    
    elif character == "Christopher Robin":
        print("Silly old bear.")
    
    else:
        print(f'sorry! I don\'t know {character}\'s catchphrase!')


print_catchphrase("Tigger")


""" Question 4: Implement a function get_item() that accepts a 0-indexed list items and a non-negative integer x 
and returns the element at index x in items. If x is not a valid index of items, return None.
"""

def get_item(items, x):
    length = len(items)
    
    if x > length - 1:
        return None
    else:
        return items[x]
    
items = ["piglet", "pooh", "roo", "rabbit"]
print(get_item(items, 5))

""" Question 5: Winnie the Pooh wants to know how much honey he has. Write a function sum_honey() that accepts 
a list of integers hunny_jars and returns the sum of all elements in the list. Do not use the built-in function sum().
"""
def sum_honey(hunny_jars):
    honey_sum = 0
    for i in hunny_jars:
        honey_sum += i        
    return honey_sum
    
hunny_jars = [12, 7, 31, 5]
print(sum_honey(hunny_jars))

hunny_jars = []
sum_honey(hunny_jars)


""" Question 6: Help Winnie the Pooh double his honey! Write a function doubled() that accepts a list of integers hunny_jars as a parameter and 
    multiplies each element in the list by two. Return the doubled list.
"""

def doubled(hunny_jars):
    hunny_two = []
    for num in hunny_jars:
        val = num * 2 
        hunny_two.append(val)
        
    return hunny_two
    
hunny_jars = [1, 2, 3]
print (doubled(hunny_jars)) 