

# Problem 1: Counting Iron Man's Suits
# Tony Stark, aka Iron Man, has designed many different suits over the years.
# Given a list of strings suits where each string is a suit in Stark's
# collection, count the total number of suits in the list.
# 1. Implement the solution iteratively without the use of the len() function.
# 2. Implement the solution recursively.
# 3. Discuss: what are the similarities between the two solutions? What are the
#    differences?
#
# def count_suits_iterative(suits):
#     pass

# def count_suits_recursive(suits):
#     pass
#
# Example Usage:
# print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
# print(count_suits_recursive(["Mark I", "Mark II", "Mark III"]))
#
# Example Output:
# 3
# 3

# UPI Plan
#
# UNDERSTAND:
# Input - A list of strings 
# Output - The total number from the list of strings 
# Edge Cases - If the list is empty
#
# PLAN:
#
# IMPLEMENT:
# - (implemented below)
#

def count_suits_iterative(suits):
    i=0
    for suit in suits:
        i=i+1
    return i
#O(n)  Space Complexity: O(1)

def count_suits_recursive(suits):
    if not suits:
        return 0
    else:
        return 1+count_suits_recursive(suits[1:])

#O(n)  Space Complexity: O(1)

print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark II", "Mark III"]))
