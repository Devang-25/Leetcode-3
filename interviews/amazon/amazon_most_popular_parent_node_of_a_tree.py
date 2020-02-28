"""
第二题，most popular parent node in a tree.
给定一个多叉树的根节点，每个节点有一个值，找出一个最popular的节点。比如这样

Given a binary tree:

     1
   /   \
 -5     11
 / \   /  \
1   2 4    -2

每个节点的popular值是以自身为根节点的树中所有节点的值之和除以以自身为根节点的树的节点数量。
可以用dfs也可以用bfs，注意读清楚题的话应该不会太难。要注意的是叶子节点不考虑。

popularity = SUM_of_substree_act_as root / NUM_of_NODES_of_substree_act_as_root

"""

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


class Popularity:
  def __init__(self):
    self.max_popularity = float("-inf")
    self.max_popular_node = None

  def find_popularity(self, node):
    """
    input node: a treenode

    return cur_total: int, sum of this subtree.

    return num_of_node: int, the number of node of this subtree including this node.
    """
    if not node:
      return 0, 0

    left_total, left_nodes = self.find_popularity(node.left)

    right_total, right_nodes = self.find_popularity(node.right)

    cur_total = node.val + left_total + right_total

    node_num = 1 + left_nodes + right_nodes

    popularity = float(cur_total / node_num)
    if popularity > self.max_popularity:
      self.max_popularity = popularity
      self.max_popular_node = node

    print("now", "node.val{}, node.total{}, num_of_nodes{}".format(node.val, cur_total, node_num))

    return cur_total, node_num

  def popularity(self, root):
    self.find_popularity(root)
    return self.max_popularity, self.max_popular_node.val


a = Node(3)
b = Node(-12)
c = Node(14)

a.left = b
a.right = c

print(Popularity().popularity(a))
