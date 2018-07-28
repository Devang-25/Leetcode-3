'''
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.total_ = 0
        self.travel_tree(root)
        return root

    def travel_tree(self, node):
        if node:
            self.travel_tree(node.right)
            self.total_ += node.val
            node.val = self.total_
            self.travel_tree(node.left)

'''
learn:
- a function does not neceesirily need to return sth

- if you want to remember a global value in a recusion
function, use self.object_ , the self. making the object
link to the object in the class ClassName(object)

- no need to pass that self.object_ into the functeion as
an argument

'''
