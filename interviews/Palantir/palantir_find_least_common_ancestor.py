"""

236. Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

"""




Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return

        has_q, has_q, node = self.find_lca(root, p, q, 0, 0)

        return node

    def find_lca(self, node, p, q, has_p, has_q):
        # print("node", node.val, p, q)

        if not node:
            return 0, 0, None

        if node.val == p.val:
            has_p = 1

        if node.val == q.val:
            has_q = 1

        # print("1_check p:{}, q{}".format(has_p, has_q))

        if not has_p or not has_q:
            l_has_p, l_has_q, r_has_p, r_has_q = 0, 0, 0, 0

            if node.left:
                l_has_p, l_has_q, node_l = self.find_lca(node.left, p, q, 0, 0)
                # print("left p{} q{} node{}".format(l_has_p, l_has_q, node_l))
                if node_l:
                    return 1, 1, node_l

            if node.right:
                r_has_p, r_has_q, node_r = self.find_lca(node.right, p, q, 0, 0)
                # print("right p{} q{} node{}".format(r_has_p, r_has_q, node_r))
                if node_r:
                    return 1, 1, node_r

            has_p = max(has_p, l_has_p, r_has_p)
            has_q = max(has_q, l_has_q, r_has_q)

            if has_p and has_q:
                return 1, 1, node
            else:
                return has_p, has_q, None
