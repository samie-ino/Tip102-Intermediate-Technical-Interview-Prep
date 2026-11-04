# Problem 2: Calculating Yield
# The tree has exactly three nodes. Its root stores one of "+", "-", "*", or
# "/", and its two leaves store integers. Apply the root's operation to the
# left and right leaf values and return the result.
#
# UPI
# Understand:
# - Input: The root of a three-node expression tree.
# - Output: The result of applying the root operator to its two children.
# - Edge cases: Support each listed operator; division uses the left value
#   divided by the right value.
# Plan:
# - Read the operator and the two leaf values, then select the matching
#   arithmetic operation.
# Implement:
# - Complete calculate_yield below. The tree always has three nodes, so time
#   and extra space are both O(1).

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def calculate_yield(root):
    pass
