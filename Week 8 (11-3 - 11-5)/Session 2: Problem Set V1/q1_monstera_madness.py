# Problem 1: Monstera Madness
# Given the root of a binary tree where each node represents the number of
# splits in a Monstera leaf, return the number of leaves (all nodes) with an
# odd number of splits.
#
# UPI
# Understand:
# - Input: The root node of a binary tree, or None for an empty tree.
# - Output: The number of tree nodes whose value is odd.
# - Edge cases: An empty tree has 0 odd values; even-valued nodes are not
#   counted.
# Plan:
# - If the current node is None, return 0.
# - Count odd-valued nodes in the left and right subtrees.
# - Add 1 if the current node's value is odd, then return the total.
# Implement:
# - Use recursion to count the odd values in the tree.
from collections import deque
class TreeNode:
  def __init__(self, value, key=None, left=None, right=None):
      self.key = key
      self.val = value
      self.left = left
      self.right = right

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root

def count_odd_splits(root):
    if root is None:
        return 0

    count = count_odd_splits(root.left) + count_odd_splits(root.right)

    if root.val % 2 != 0:
        count += 1

    return count
values = [2, 3, 5, 6, 7, None, 12]
monstera = build_tree(values)

print(count_odd_splits(monstera))
print(count_odd_splits(None))

'''
Time: O(n) — it visits each node once. Here, n is the number of nodes in the tree.
Space: O(h) — the recursive calls use memory as they go down the tree. Here, h is 
the tree’s height. In a balanced tree, that’s O(log n); in a very uneven tree, it 
can be O(n).
'''