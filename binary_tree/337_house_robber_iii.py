"""
337. House Robber III
Medium

1271

28

Favorite

Share
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1

Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.


Since I only travel each node once, the time complexity is O(N), where N is the number of nodes in the tree.

"""



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.max_rob = 0

    def rob_or_not(self, node):
        if not node:
            return (0, 0)

        else:
            left = self.rob_or_not(node.left)
            right = self.rob_or_not(node.right)

            # rob = node.val + max_without_left + max_without_right
            rob = node.val + left[1] + right[1]

            # not_rob = max_with_left + max_with_right
            # Be cautious here: Not rob this node does NOT mean you have to rob the next left or next right node.
            # You can choose to NOT rob the next left or next right, but rob next Next left or next next right if that give you more rob money
            # you can not rob this level but
            not_rob = (max(left[0], left[1]) + max(right[0], right[1]))

            if self.max_rob < max(rob, not_rob):
                self.max_rob = max(rob, not_rob)

        return (rob, not_rob)


    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        rob, not_rob = self.rob_or_not(root)
        return self.max_rob
