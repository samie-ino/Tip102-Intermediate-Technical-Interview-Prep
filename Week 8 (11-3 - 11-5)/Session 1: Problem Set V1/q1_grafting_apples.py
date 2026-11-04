# Problem 1: Grafting Apples
# Build the binary tree rooted at "Trunk" with "Mcintosh" on the left and
# "Granny Smith" on the right. Give both of those children two children:
# "Fuji" and "Opal" under "Mcintosh", and "Crab" and "Gala" under
# "Granny Smith".
#
# UPI
# Understand:
# - Input: The provided root node, TreeNode("Trunk").
# - Output: The completed tree with the specified values and parent-child links.
# - Edge cases: None; all seven nodes are specified.
# Plan:
# - Create the remaining nodes and connect each one to its parent.
# Implement:
# - Build the tree below, then check its links and values.

from collections import deque

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


root = TreeNode("Trunk")

# TODO: Build the tree shown in the exercise.

root.left = TreeNode("Mcintosh")
root.right = TreeNode("Granny Smith")

root.left.left = TreeNode("Fuji")
root.left.right = TreeNode("Opal")

root.right.left = TreeNode("Crab")
root.right.right = TreeNode("Gala")

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)

print_tree(root)
