"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum1(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def preorder(node, path_sum, path):
            if not node:
                return

            path_sum += node.val
            path.append(node.val)

            if node.left == None and node.right == None and path_sum == sum:
                result.append(path[:])

            preorder(node.left, path_sum, path)
            preorder(node.right, path_sum, path)

            path.pop()

        # result need to be a global name
        result = []
        preorder(root, 0, [])
        return result

    def pathSum2(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """

        # sultion 2
        path_value = 0
        path = []
        result = []

        self.preorder(root, path_value, sum, path, result)
        return result

    def preorder(self, node, path_value, sum, path, result):
        if not node:
            return

        path_value += node.val
        path.append(node.val)
        # print("number: {}, path:{}, result:{}".format(node.val, path, result))

        if node.left == None and node.right == None and path_value == sum:
            result.append(path[:])
            # print("append result", result)

        self.preorder(node.left, path_value, sum, path, result)
        self.preorder(node.right, path_value, sum, path, result)

        # you don't need to deduct the node.val because integers are passed by value, NOT by reference of address
        # integers, float and strings are all passed by value
        # path_value -= node.val
        print("node value", node.val, "pop", path.pop())

        return result
