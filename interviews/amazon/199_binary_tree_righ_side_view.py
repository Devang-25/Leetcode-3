from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

  def rightSideView(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if not root:
      return []

    self.results = []
    cur_level = deque([root])
    self.helper(cur_level)

    return self.results

  def helper(self, cur_level):
    if not cur_level:
      return

    next_level = deque()

    print("cur", cur_level)
    node = cur_level.popleft()
    self.results.append(node.val)
    if node.right:
      next_level.append(node.right)
    if node.left:
      next_level.append(node.left)

    while cur_level:
      node = cur_level.popleft()
      if node.right:
        next_level.append(node.right)
      if node.left:
        next_level.append(node.left)

    self.helper(next_level)
