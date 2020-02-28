"""
30. Kth Smallest Element in a BST
Medium

988

39

Favorite

Share
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# inorder traveral: left root right


class Solution:

  def __init__(self):
    self.result = []

  def kthSmallest(self, root: TreeNode, k: int) -> int:
    self.inorder(root)
    return self.result[k - 1]

  def inorder(self, root):
    if not root:
      return

    self.inorder(root.left)

    self.result.append(root.val)

    self.inorder(root.right)


'''
The solution above use the inorder traversal of the tree to solve this quesiton. 

The time complexity:
for this above solution is O(N), N = num of nodes in the tree.

The space complexity:
is also O(N), where N = num of node in the tree.

'''

#########  Solution 2 ######


class Solution:

  def kthSmallest(self, root: TreeNode, k: int) -> int:
    self.k = k
    self.result = None
    self.inorder(root)
    return self.result

  def inorder(self, node):
    if not node:
      return

    self.inorder(node.left)

    self.k -= 1
    if self.k == 0:
      self.result = node.val

    self.inorder(node.right)


'''
The solution above use the inorder traversal of the tree to solve this quesiton. 

The time complexity:
for this above solution is O(N), N = num of nodes in the tree.

The space complexity:
is also O(1)

'''
