# Problem 3: Catchphrase
# Write a function print_catchphrase() that accepts a string character as a parameter and prints the catchphrase
# of the given character as outlined in the table below.
#
# Character | Catchphrase
# "Pooh" | "Oh bother!"
# "Tigger" | "TTFN: Ta-ta for now!"
# "Eeyore" | "Thanks for noticing me."
# "Christopher Robin" | "Silly old bear."
#
# def print_catchphrase(character):
#     pass
#
# Example Usage:
#
# print_catchphrase("Tigger")
#
# Example Output:
#
# TTFN: Ta-ta for now!

"""
UNDERSTAND:
Input: 1 catchphrase table string
Output: 1 string catchphrase printed 

Edge Cases:
- if there is an unknown character

PLAN:
- create a function print_catchphrase that accepts the parameter character
- seperate the character from the string 
- return the string 

IMPLEMENT: (below)
"""

def print_catchphrase(character):
    if character == "Pooh":
        return "Oh bother!"
    if character == "Tigger":
        return "TTFN: Ta-ta for now!"
    if character == "Eeyore":
        return "Thanks for noticing me."
    if character == "Christopher Robin":
        return "Silly old bear."
    return f"sorry! I don't know {character}'s catchphrase!"

