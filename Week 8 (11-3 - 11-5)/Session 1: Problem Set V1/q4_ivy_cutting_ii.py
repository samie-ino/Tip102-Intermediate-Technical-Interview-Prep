# Problem 4: Ivy Cutting II
# Implement right_vine() again using the opposite approach from Problem 3:
# if Problem 3 is iterative, make this version recursive; if Problem 3 is
# recursive, make this version iterative. Return the values from the root
# through the rightmost path, stopping when there is no right child.
#
# UPI
# Understand:
# - Input: The root of a binary tree.
# - Output: Values along the root-to-rightmost path, in order.
# - Edge cases: A root with no right child produces a one-element list.
# Plan:
# - Use a different traversal technique from the one chosen for Problem 3,
#   following only right children and collecting their values.
# Implement:
# - Complete right_vine below. For a balanced tree, the path takes O(log n)
#   time and O(log n) space for its result.

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def right_vine(root):
    pass
