# Problem 4: Return Item
# Implement a function get_item() that accepts a 0-indexed list items and a non-negative integer x
# and returns the element at index x in items. If x is not a valid index of items, return None.
#
# def get_item(items, x):
#     pass
#
# Example Usage:
#
# items = ["piglet", "pooh", "roo", "rabbit"]
# print(get_item(items, 2))
#
# Example Output:
#
# roo


"""
UNDERSTAND:
Input: 1 list of items and 1 integer index x
Output: 1 value from the list at index x, or None if the index is invalid

Edge Cases:
- x is negative
- x is greater than or equal to the length of items
- items is empty

PLAN:
- check whether x is a valid index in items
- if x is invalid, return None
- otherwise return items[x]

IMPLEMENT: (below)
"""

def get_item(items, x):
    if x < 0 or x >= len(items):
        return None
    return items[x]
