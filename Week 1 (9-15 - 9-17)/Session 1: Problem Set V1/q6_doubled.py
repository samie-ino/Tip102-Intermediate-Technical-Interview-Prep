# Problem 6: Double Trouble
# Help Winnie the Pooh double his honey! Write a function doubled() that accepts a list of integers hunny_jars as a parameter and
# multiplies each element in the list by two. Return the doubled list.
#
# def doubled(hunny_jars):
#     pass
#
# Example Usage:
#
# hunny_jars = [1, 2, 3]
# print(doubled(hunny_jars))
#
# Example Output:
#
# [2, 4, 6]

"""
UNDERSTAND:
Input: 1 list of integers representing honey jar amounts
Output: 1 new list where every value is doubled

Edge Cases:
- empty list should return an empty list
- negative numbers should become more negative after doubling

PLAN:
- create a new empty list
- loop through each number in hunny_jars
- multiply each number by 2
- append the doubled value to the new list
- return the new list

IMPLEMENT: (below)
"""


def doubled(hunny_jars):
    hunny_two = []
    for num in hunny_jars:
        hunny_two.append(num * 2)
    return hunny_two
