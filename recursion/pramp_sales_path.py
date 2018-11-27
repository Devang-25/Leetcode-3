"""
A path from Honda’s factory to a car dealership, which is a path from the root to a leaf in the tree, is called a Sales Path. The cost of a Sales Path is the sum of the costs for every node in the path. For example, in the tree above one Sales Path is 0→3→0→10, and its cost is 13 (0+3+0+10).

Honda wishes to find the minimal Sales Path cost in its distribution tree. Given a node rootNode, write a function getCheapestCost that calculates the minimal Sales Path cost in the tree.

Implement your function in the most efficient manner and analyze its time and space complexities.

For example:

Given the rootNode of the tree in diagram above

Your function would return:

7 since it’s the minimal Sales Path cost (there are actually two Sales Paths in the tree whose cost is 7: 0→6→1 and 0→3→2→1→1)

"""

def get_cheapest_cost(rootNode):
    if not rootNode.children:
        return rootNode.cost
    else:
        min_cost = float('inf')
        for child in rootNode.children:
            temp_cost = get_cheapest_cost(child)
            if temp_cost < min_cost:
                min_cost = temp_cost
        # return the min_cost from its children + its own cost
        return min_cost + rootNode.cost

# A node
class Node:
    def __init__(self, cost):
        self.cost = cost
        self.children = []
        self.parent = None

root = Node(0)
a = Node(5)
b = Node(3)
c = Node(6)
root.children = [a, b,c]
d = Node(4)
e = Node(1)
f = Node(9)
a.children = [d]
b.children = [e]
c.children = [f]

get_cheapest_cost(root)
