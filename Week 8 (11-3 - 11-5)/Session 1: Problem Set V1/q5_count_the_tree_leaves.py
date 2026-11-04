# Problem 5: Count the Tree Leaves
# Count the leaf nodes in a binary tree. A leaf is a node that has neither a
# left nor a right child.
#
# UPI
# Understand:
# - Input: The root of a binary tree.
# - Output: The number of leaf nodes.
# - Edge cases: A single node is one leaf; an empty tree has no leaves.
# Plan:
# - Traverse the tree; count a node when both of its children are absent.
# - Combine the counts from the left and right subtrees.
# Implement:
# - Complete count_leaves below. The traversal takes O(n) time and O(log n)
#   auxiliary space for a balanced tree.

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def count_leaves(root):
    pass
