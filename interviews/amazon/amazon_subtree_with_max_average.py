"""
Given a binary tree:

     1
   /   \
 -5     11
 / \   /  \
1   2 4    -2


Find the subtree with the maximum average

"""

# from statistics import mean
# import math

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

class MaxAverage:
  def __init__(self):
    # self.max_avg = float("-inf")
    self.max_avg = 0
    self.max_node = None


  def find_avg(self, node):
    """
    input node: a node
    return a tuple (int, int) = (avg, num_of_nodes)
    """
    # bottom case: just return 0
    if not node:
      return (0, 0)

    print("down", node.val)

    # if node.left, then search the average(node.left)
    # if node.left:
    #   left_avg, left_num = self.find_avg(node.left)


    # if node.right:
    #   right_avg, right_num = self.find_avg(node.right)

    left_avg, left_num = self.find_avg(node.left)
    right_avg, right_num = self.find_avg(node.right)

    print("upward", node.val)
    num_of_node = left_num + right_num + 1
    cur_total = float(left_avg * left_num + right_avg * right_num + node.val)
    new_average = cur_total / num_of_node

    if new_average > self.max_avg:
      self.max_avg = new_average
      self.max_node = node

    return new_average, num_of_node

  def max_average(self, root):
    """
    input root: node
    output node: a node whose subtree with max average
    """

    self.find_avg(root)

    # return self.max_avg
    # return self.max_node.val
	return self.max_node

######## test case 1########
# a = Node(0)
# b = Node(1)
# c = Node(2)

# a.left = b
# a.right = c



########### test case 2 ######

a = Node(3)
b = Node(-12)
c = Node(14)

a.left = b
a.right = c

####### run ######
ma = MaxAverage()
result = ma.max_average(a)
print(result)
