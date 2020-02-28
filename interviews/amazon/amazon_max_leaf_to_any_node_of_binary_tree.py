"""
Q: find a path from leaf to any of its parent node in the tree that it has the max sum

"""


class TreeNode:

  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


class Solution:

  def maxSumPath(self, root):
    """
    inputs:
      roots: a TreeNode object

    outputs:
      max_sum: int

    """
    self.max_sum = None
    self.helper(root)

    return self.max_sum

  def helper(self, node):
    if not node:
      return 0

    left_total = self.helper(node.left)
    right_total = self.helper(node.right)

    new_total = max(left_total, right_total) + node.val
    if not self.max_sum or new_total > self.max_sum:
      self.max_sum = new_total

    return new_total


# a = TreeNode(-1)
# b = TreeNode(1)
# c = TreeNode(4)
# a.left = b
# a.right = c

# s = Solution()
# r = s.maxSumPath(a)
# print("r", r)

###################

a = TreeNode(-1)
# b = TreeNode(1)
# c = TreeNode(4)
# a.left = b
# a.right = c

s = Solution()
r = s.maxSumPath(a)
print("r", r)