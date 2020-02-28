class TreeNode:

  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


# need to use boundary
class Solution:

  def isValidBST(self, root):
    """
    inputs:
      root: Treenode
    
    outputs:
      result: bool

    """
    return self.helper(root, float("-inf"), float("inf"))

  def helper(self, node, left_bound, right_bound):
    """
    inputs:
      node: Treenode
      left_bound: int
      right_bound: int
    
    outputs:
      result: bool

    """
    if not node:
      return True

    if node.val <= left_bound or node.val >= right_bound:
      return False

    left_valid = self.helper(node.left, left_bound, node.val)
    right_valid = self.helper(node.right, node.val, right_bound)

    if not left_valid or not right_valid:
      return False

    return True


a = TreeNode(3)
b = TreeNode(1)
c = TreeNode(4)

a.left = b
a.right = c

s = Solution()
r = s.isValidBST(a)
print("1 result", r)

#################
# a = TreeNode(None)
# s = Solution()
# r = s.isValidBST(a)
# print("2 result", r)

##########

a = TreeNode(3)
b = TreeNode(1)

a.left = b

s = Solution()
r = s.isValidBST(a)
print("3 result", r)
