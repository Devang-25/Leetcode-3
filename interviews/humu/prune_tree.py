class Node:

  def __init__(self):
    self.children = []


def fn(node):
  return bool


class Solution:

  def main(self, root, fn):
    """
    inputs:
      root: Node object
      fn: function that return bool. If True: deelte. If False: keep.
    output:
      root: Node
      if nothing remain, return None
    """

    if not root:
      return
    if fn(root):
      return
    self.pruneTree(root, fn)
    return root

  def pruneTree(self, node, fn):
    new_children = []
    for child in node.children:
      delete = fn(child)
      if delete:
        new_grandchildren = self.relink(child, fn)
        new_chidlren += new_grandchildren
      if not delete:
        new_children.append(child)
    node.children = new_children
    for child in node.children:
      self.pruneTree(child, fn)

  def relink(self, node, fn):
    new_grandchildren = []
    grandchildren = node.children  # []
    for child in grandchildren:
      if not fn(child):
        new_grandchildren.append(child)
    return new_grandchildren
