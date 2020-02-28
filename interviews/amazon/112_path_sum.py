# Definition for a binary tree node.
class TreeNode:

  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


class Solution:

  def hasPathSum(self, root, sum):
    self.sum = sum
    return self.helper(root, 0)

  def helper(self, node, total):
    if not node:
      if total == self.sum:
        return True
      return False

    if total > self.sum:
      return False

    left = self.helper(node.left, total + node.val)
    right = self.helper(node.right, total + node.val)
    return (left or right)


a = TreeNode(3)
b = TreeNode(1)
c = TreeNode(2)
a.left = b
a.right = c

s = Solution()
r = s.hasPathSum(a, 4)
print("r", r)
