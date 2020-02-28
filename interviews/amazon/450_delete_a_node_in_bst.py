# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

  def deleteNode(self, root, key):
    """
    :type root: TreeNode
    :type key: int
    :rtype: TreeNode

    idea is the find the value, and replace it with the minimum value in the right subtree
    """
    if not root:
      return None

    elif key < root.val:
      root.left = self.deleteNode(root.left, key)

    elif key > root.val:
      root.right = self.deleteNode(root.right, key)

    else:  #if we found the node
      if not root.left:
        return root.right
      elif not root.right:
        return root.left

      temp = root.right
      mini = temp.val
      while temp.left:
        temp = temp.left
        mini = temp.val
      root.val = mini
      root.right = self.deleteNode(root.right, mini)
    return root
