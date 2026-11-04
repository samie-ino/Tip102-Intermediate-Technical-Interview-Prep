# Problem 8: Flower Fields
# Return True if the target flower value appears in the binary tree; otherwise
# return False.
#
# UPI
# Understand:
# - Input: The root of a binary tree and the flower value to find.
# - Output: Whether any node in the tree has the target value.
# - Edge cases: An empty tree does not contain the target.
# Plan:
# - Search the tree's nodes and stop once a matching value is found.
# Implement:
# - Complete find_flower below. In the worst case, the search takes O(n) time;
#   for a balanced tree, recursive auxiliary space is O(log n).

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def find_flower(root, flower):
    pass
