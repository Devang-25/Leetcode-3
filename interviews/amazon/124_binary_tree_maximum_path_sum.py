"""

124. Binary Tree Maximum Path Sum
Hard

1337

96

Favorite

Share
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42

"""


# Definition for a binary tree node.
class TreeNode:

  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


class Solution:

  def maxPathSum(self, root):
    """
      inputs:
        root: TreeNode

      outputs:
        max_sum: int

      """
    self.max_sum = None
    self.helper(root)

    return self.max_sum

  def helper(self, node):
    if not node:
      return float("-inf")

    left_max = self.helper(node.left)

    right_max = self.helper(node.right)

    # globaly max up until this points
    this_max = max(node.val, left_max, right_max, node.val + left_max,
                   node.val + right_max, node.val + left_max + right_max)

    if not self.max_sum or this_max > self.max_sum:
      self.max_sum = this_max

    # max WITH cur node
    max_with_node = max(node.val, node.val + left_max, node.val + right_max)

    return max_with_node


a = TreeNode(-1)

s = Solution()
r = s.maxPathSum(a)
assert r == -1
print("r", r)

##################

a = TreeNode(-1)
b = TreeNode(2)
c = TreeNode(3)
a.left = b
a.right = c

s = Solution()
r = s.maxPathSum(a)
assert r == 4
# 2 + -1 + 3 = 4
print("r", r)

##################

a = TreeNode(-1)
b = TreeNode(-2)
c = TreeNode(3)
a.left = b
a.right = c

s = Solution()
r = s.maxPathSum(a)
assert r == 3
# path = [3]
print("r", r)

##############

a = TreeNode(-1)
b = TreeNode(-2)
c = TreeNode(3)
d = TreeNode(4)
a.left = b
a.right = c
c.right = d

s = Solution()
r = s.maxPathSum(a)
assert r == 7
print("r", r)
