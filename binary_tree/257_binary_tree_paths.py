"""
257. Binary Tree Paths
Easy

794

63

Favorite

Share
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

  def binaryTreePaths(self, root):
    """
    :type root: TreeNode
    :rtype: List[str]
    """

    if not root:
      return []

    self.paths = []
    self.results = []

    self.travel(root, [])

    # ["1->2->5","1->3"]
    for path in self.paths:
      path = "->".join(path)
      self.results.append(path)

    return self.results

  def travel(self, node, path):
    """
    inputs: 
      nodes: TreeNode object
      path: List[int]
    
    outputs:
      None
    """
    if not node.left and not node.right:
      self.paths.append(path + [str(node.val)])
      return

    if node.left:
      self.travel(node.left, path + [str(node.val)])
      # self.travel(node.left, path + "->" + str(node.val))

    if node.right:
      self.travel(node.right, path + [str(node.val)])
      # self.travel(node.right, path + "->" + str(node.val))
