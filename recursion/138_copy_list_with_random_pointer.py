# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None

        nodes = {}

        def clone_node(node):
            # if node is empty
            if not node:
                return None
            # if node already in the nodes dict
            if node in nodes:
                return nodes[node]
            # create the node
            cnode = RandomListNode(node.label)
            # store it into nodes dict
            nodes[node] = cnode
            cnode.next = clone_node(node.next)
            cnode.random = clone_node(node.random)

            return cnode

        return clone_node(head)
