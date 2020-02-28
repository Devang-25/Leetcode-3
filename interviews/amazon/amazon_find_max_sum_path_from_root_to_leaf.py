# Definition for a binary tree node.
class TreeNode:

  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


class Solution:

  def maxPathSum(self, root):
    self.max_sum = 0
    self.max_path = []
    self.helper(root, [], 0)

    return self.max_path

  def helper(self, node, path, total):
    if not node:
      if total > self.max_sum:
        self.max_sum = total
        self.max_path = path
      return

    print("node", node.val)
    if node.left:
      print("left", node.left.val)

    if node.right:
      print("right", node.right.val)
    self.helper(node.left, path + [node.val], total + node.val)
    self.helper(node.right, path + [node.val], total + node.val)


a = TreeNode(3)
b = TreeNode(1)
c = TreeNode(4)

a.left = b
a.right = c

s = Solution()
r = s.maxPathSum(a)
print("1 result", r)

##########

# a = TreeNode(3)
# b = TreeNode(1)

# a.left = b

# s = Solution()
# r = s.maxPathSum(a)
# print("3 result", r)
