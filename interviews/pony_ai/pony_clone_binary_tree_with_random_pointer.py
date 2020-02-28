“”“
Clone a Binary Tree with Random Pointers

Given a Binary Tree where every node has following structure.

struct node {
    int key;
    struct node *left,*right,*random;
}


https://www.geeksforgeeks.org/clone-binary-tree-random-pointers/

解题思路：
- use a dictionary to store the clonenode address of each original treenode
”“”

class Node:
    def __init__(selfk, val):
        self.val = val
        self.left = None
        self.right = None
        self.random = None

class CloneTree:
    def clone(self, root):
        """
        given the root of binary tree with random pointers,
        clone it

        input root: node
        return output clonenode: a node
        """
        nodes = {}

        def clone_node(node):
            # some node is empty
            if not node:
                return None
            # some nodes already in the nodes dict, should just return it's clone address
            if node in nodes:
                return nodes[node]

            # create new clone node
            clonenode = Node(node.val)
            nodes[node] = clonenode
            clone.next = clone_node(node.next)
            clone.random = clone_node(node.random)

            return clonenode

        return clone_node(root)
