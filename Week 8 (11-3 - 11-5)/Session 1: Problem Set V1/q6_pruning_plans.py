# Problem 6: Pruning Plans
# Return a list of all node values in postorder: visit the left subtree, then
# the right subtree, then the current node.
#
# UPI
# Understand:
# - Input: The root of a binary tree.
# - Output: Node values in postorder traversal order.
# - Edge cases: An empty tree produces an empty list.
# Plan:
# - Traverse the left and right subtrees before adding the current node value.
# Implement:
# - Complete survey_tree below. The traversal takes O(n) time and O(log n)
#   auxiliary space for a balanced tree.

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def survey_tree(root):
    pass
