# Problem 7: Foraging Berries
# Each node stores a berry count. Return the sum of the values of all nodes
# whose value is strictly greater than threshold.
#
# UPI
# Understand:
# - Input: The root of a binary tree of berry counts and a threshold.
# - Output: The sum of node values greater than the threshold.
# - Edge cases: Values equal to the threshold are excluded; an empty tree
#   produces zero.
# Plan:
# - Traverse the tree and add a node's value only when it exceeds threshold.
# Implement:
# - Complete harvest_berries below. The traversal takes O(n) time and O(log n)
#   auxiliary space for a balanced tree.

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def harvest_berries(root, threshold):
    pass
