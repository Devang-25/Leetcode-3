"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself
             according to the LCA definition.

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # pass in a node: see if there is p or q in it
        # return: 1) number of common ancestor 2) the node if # of common ancestor is >= 2 else return None
        def find(node):
            if not node:
                return 0, None

            count_left, ancestor_left = find(node.left)

            if count_left >= 2:
                return count_left, ancestor_left

            count_right, ancestor_right = find(node.right)

            if count_right >= 2:
                return count_right, ancestor_right

            # count if: 1) node = p 2) node = q 3) count from node.left 4)count from node.right
            # comparing the address of the node here, not the integer
            count = (node == p) + (node == q) + count_left + count_right

            return count, node

        count, ancestor = find(root)
        return None if count < 2 else ancestor
