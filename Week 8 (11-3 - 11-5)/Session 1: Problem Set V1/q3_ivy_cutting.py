# Problem 3: Ivy Cutting
# Return a list of the values on the path from the root to the rightmost leaf.
# At each node, follow its right child when one exists. If it has no right
# child, stop there; in particular, a root with no right child gives a
# one-element list containing only the root value.
#
# UPI
# Understand:
# - Input: The root of a binary tree.
# - Output: Values along the root-to-rightmost path, in order.
# - Edge cases: If the root has no right child, return only its value.
# Plan:
# - Start at the root, record each visited value, and follow right children.
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
