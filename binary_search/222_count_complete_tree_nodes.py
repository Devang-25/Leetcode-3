debug = True


def dprint(*args, **kwargs):
  if debug:
    print(*args, **kwargs)


class Node:

  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


class Solution(object):

  def countNodes_naive_recursive(self, root):
    """
    :type root: TreeNode
    :rtype: int

    naive_solution: 
    - use recursion to count every nodes at every level
    - for each left and right node:
    - pass into that

    Time Complexity: O(N)
    where N is the number of nodes
    """
    self.numOfNodes = 0

    self._count(root)

    return self.numOfNodes

  def _count(self, node):
    if not node:
      return

    # dprint("val", node.val)
    self.numOfNodes += 1
    self._count(node.left)
    self._count(node.right)
    """
    # binary_search solution

    1) should know what is the depth of the tree
    2) then assume that you have nodes full at the last level of the tree
    3) number all the 2^d nodes (exist or non-exist) in the last level from 0 ~ 2^d-1
    4) check the mid-index nodes exist or not. 
      Q:How do I know where is the i-th index is located in the last level? 
      4.1) use binary seach to guide your move.
      4.2) For exmple, if you want to find 4th index in the last level. 
      4.3) 0, 1, 2, 3, |  4, 5, 6, 7  Go Right
      4.4) 4, 5, | 6, 7 Go Left
      4.5) 4, | 5  Go Left
    5) if 4 exist, you search in the range of 5-7.
    6) if 4 do NOT exist, you seach in the range of 0 - 3.

    Q: for each search of the exisitance of a node, how much time needs?
    A: we need O(d) time. Because we need to go d levels for each search. 

    Q: How many times we have to search before we find the target leaf node?
    A: at most we have to seach d times. Because:
    1) We have 2^d nodes in the last level of the tree. 
    2) Using binary search, we at most have to search Log(2^d) = d times. 

    Q: So what the overall time complexity for this solution? 
    A: The overall solution is O(d^2), where d is the depth of the tree


    Edge cases:
    - where all the nodes in the last level is full.

    """

  def countNodes(self, root):
    if not root:
      return 0

    self.root = root
    self.depth = self.find_depth(root)

    left = 0
    right = 2**(self.depth - 1) - 1
    first_empty_node = self.find_empty_node(left, right)
    dprint("first empty_nodes:{}".format(first_empty_node))

    if first_empty_node == 0:  # full tree
      dprint("full Tree")
      return 2 * 2**(self.depth - 1) - 1
    total_nodes = 2**(self.depth - 1) - 1 + first_empty_node
    return total_nodes

  def find_empty_node(self, left, right):
    """
    purpose: find the 1st empty node

    return: int, the index of the first empty node in the last level
    """
    # if only one index is left in the search range, return it.
    if left == right:
      dprint("equal! {}".format(left))
      node_not_empty = self.check_node(left)
      if node_not_empty:
        return 0
      else:
        return left

    mid = (left + right) // 2
    dprint("left:{}, right:{}, mid:{}".format(left, right, mid))

    node_not_empty = self.check_node(mid)
    dprint("Node {} is not empty: {}".format(mid, node_not_empty))
    if node_not_empty:  # if node is not empyty, go right
      return self.find_empty_node(mid + 1, right)
    else:  # if mid node is empty, search in the left half, including the mid node
      return self.find_empty_node(left, mid)

  def find_path(self, target_index, left, right, steps):
    if left == right:
      dprint("find_path: equal! left:{}, right:{}".format(left, right))
      return steps

    mid = (left + right) // 2
    dprint("find_path: left:{}, right:{}, mid:{}".format(left, right, mid))

    if target_index <= mid:
      steps.append("left")
      return self.find_path(target_index, left, mid, steps)
    elif target_index > mid:
      steps.append("right")
      return self.find_path(target_index, mid + 1, right, steps)

  def check_node(self, target_index):
    """
    inputs:
    steps: list of str [str]
    
    output: bool
    if node is Not empty: return True
    if node is empty
    """
    start = 0
    end = 2**(self.depth - 1) - 1
    steps = self.find_path(target_index, start, end, [])

    node = self.root

    for step in steps:
      if step == "left":
        node = node.left
      elif step == "right":
        node = node.right

    return (node is not None)

  def find_depth(self, node):
    if not node:
      return 0

    return 1 + (self.find_depth(node.left) or self.find_depth(node.right))


node0 = Node(0)
node10 = Node(10)
node11 = Node(11)
node20 = Node(20)
node21 = Node(21)
node22 = Node(22)

root1 = None
root = node0

node0.left = node10
node0.right = node11

# node10.left = node20
# node10.right = node21
# node11.left = node22

s = Solution()
s.depth = s.find_depth(root)
print("depth:", s.depth)

# target_index = 1
# left = 0
# right = 2**(s.depth - 1) - 1
# print("start:{}, {}".format(left, right))
# print(s.find_path(target_index, left, right, []))

total_nodes = s.countNodes(root)
print("total nodes:{}".format(total_nodes))

# print(s.countNodes(root))
