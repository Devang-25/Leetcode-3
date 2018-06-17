"""

114. Flatten Binary Tree to Linked List
DescriptionHintsSubmissionsDiscussSolution
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6


"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        #  in preorder
        def run1(node):
            if not node:
                return None
            bottom_right = node
            right_node = node.right

            if node.left:
                # connect to the leaf of right node
                bottom_right = run(node.left)
                node.left, node.right = None, node.left

            # since node.right already change reference to previous node.left,
            # so we are checking right_node here
            if right_node:
                bottom_right.right = right_node
                return run(right_node)

            return bottom_right

        def run2(node):
            if node:
                left_bottom, right_bottom = run(node.left) or node, run(node.right)
                node.left, node.right, left_bottom.right = None, node.left, node.right

                return right_bottom or left_bottom

        run1(root)
        run2(root)
