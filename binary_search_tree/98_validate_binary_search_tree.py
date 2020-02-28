"""
98. Validate Binary Search Tree
Medium

1589

243

Favorite

Share
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:

Input:
    2
   / \
  1   3
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value is 5 but its right child's value is 4.


"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
- pass the upper and lower boundary to the next level
- use a helper function to do that
- if valid: value within the boundary:
    - then pass the value into the next recursion check_validity function
"""

class Solution(object):
    def check_validity(self, node, left_bound, right_bound):
        if not node:
            return True

        if left_bound < node.val < right_bound:
            left_validity = self.check_validity(node.left, left_bound, node.val)
            right_validity = self.check_validity(node.right, node.val, right_bound)
            if not left_validity or not right_validity:
                return False
        else:
            return False

        return True

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.check_validity(root, -float("inf"), float("inf"))
