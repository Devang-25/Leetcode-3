"""
110. Balanced Binary Tree
Easy

1010

90

Favorite

Share
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7



Time Complexity:

- O(N) b/c you travel each node once
   """


   # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

########### Soluion 1 ################

class Solution1(object):
    def check_balanced(self, root):
        """
        :type root: TreeNode
        :rtype depth: int or -1 if not balanced

        Solution:
        - alwasy int: -1 or depth
        - if not balanced: use -1 to represent
        - int from 0 to N represent depth
        """
        if not root:
            return 0

        left_depth = self.check_balanced(root.left)
        if left_depth == -1:
            return -1

        right_depth = self.check_balanced(root.right)
        if right_depth == -1:
            return -1

        if abs(left_depth - right_depth) > 1:
            return -1

        else:
            return max(left_depth, right_depth) + 1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return False if self.check_balanced(root) == -1 else True



############### Solution 2 ####################

class Solution2(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check_depth_recursion(node):
            """
            I pass in a node:
            return the depth from this node
            """
            if not node:
                return 0

            left_depth = 0
            right_depth = 0

            if node.left:
                left_depth = check_depth_recursion(node.left)
                if not left_depth:
                    return False

            if node.right:
                right_depth = check_depth_recursion(node.right)
                if not right_depth:
                    return False

            if abs(left_depth - right_depth) > 1:
                return False
            else:
                return max(left_depth, right_depth) + 1

        if not root:
            return True

        depth = check_depth_recursion(root)
        return True if depth else False
