# Problem 2: Flower Finding
# Given the root of a binary search tree organized alphabetically by plant
# name and a target name, return True if the name is present and False
# otherwise. Assume the tree is balanced when analyzing time complexity.
#
# UPI
# Understand:
# - Input: The root of a binary search tree of plant names and a target name.
# - Output: True if the target name is in the tree; otherwise, False.
# - Edge cases: An empty tree does not contain the target.
# Plan:
# - Start at the root and compare its name with the target.
# - If they match, the target is present.
# - Otherwise, use alphabetical ordering to choose the left or right subtree.
# - Continue until the target is found or there are no more nodes to check.
# Implement:
# - Write the search in find_flower. Assume the tree is balanced for
#   time-complexity analysis.

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

def find_flower(inventory, name):
    pass
