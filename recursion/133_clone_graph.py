# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        nodes = {}

        def clone_node(node):
            if not node:
                return None
            if node.label in nodes:
                return nodes[node.label]

            cnode = UndirectedGraphNode(node.label)
            nodes[node.label] = cnode
            cnode.neighbors = [clone_node(neighbor) for neighbor in node.neighbors]
            # for neighbor in node.neigbors:
            #   clone_node(neighbor)
            return cnode

        return clone_node(node)
