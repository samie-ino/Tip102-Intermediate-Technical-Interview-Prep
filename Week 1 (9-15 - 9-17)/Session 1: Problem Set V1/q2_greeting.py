# Problem 2: Greeting
# Write a function greeting() that accepts a single parameter, a string name,
# and prints the string "Welcome to The Hundred Acre Wood <name>! My name is Christopher Robin."
#
# def greeting(name):
#     pass
#
# Example Usage:
#
# greeting("Winnie the Pooh")
#
# Example Output:
#
# Welcome to The Hundred Acre Wood Winnie the Pooh! My name is Christopher Robin.

"""
UNDERSTAND:
Input: 1 string given 
Output: 1 function that returns the given string

Edge Cases:
- if an empty name it should still return the string

PLAN:
- create a function greeting that accepts a parameter name
- return the given string and print it 

IMPLEMENT: (below)
"""

def greeting(name):
    return f"Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin."
