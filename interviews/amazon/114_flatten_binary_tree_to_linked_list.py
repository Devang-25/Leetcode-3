# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

  def flatten(self, root):
    """
    :type root: TreeNode
    :rtype: void Do not return anything, modify root in-place instead.
    """
    self.helper(root)

  def helper(self, node):
    if not node:
      return

    if node.left:
      self.helper(node.left)

    if node.left and node.right:
      right = node.right
      node.right = node.left
      node.left = None
      while node.right:
        node = node.right
      node.right = right

      self.helper(right)

    elif node.left:
      node.right = node.left
      node.left = None

    elif node.right:
      self.helper(node.right)

    return