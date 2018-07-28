"""
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.
"""

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
        """
        if not root:
            return root
        if key < root.val:
            print('go to root.left')
            root.left = self.deleteNode(root.left, key)
            print('return root.left')
        elif key > root.val:
            print('go to root.right')
            root.right = self.deleteNode(root.right, key)
            print('reuturn root.right')
        else:
        # elif key == root.val: # find the node
            print('else')
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            # if root.left and root.right: # find the leftmost child of right tree
            temp = root.right
            mini = temp.val
            print('mini', mini)
            while temp.left is not None:
                temp = temp.left
                mini = temp.val
            # replace the current val (the one we want to delete)
            # with the mini - leftmost child of
            root.val = mini
            # delete the minimum node in right subtree
            print('root.right')
            root.right = self.deleteNode(root.right, root.val)
        return root
