"""
解题思路：

- 判断是否是一个有效的树，这取决于：
  - 不能有cycle
  - 只能有一个root
  - edges的数量 = nodes的数量 - 1

"""


class Solution(object):

  def validTree(self, n, edges):
    """
    :type n: int
    :type edges: List[List[int]]
    :rtype: bool
    """
    self.edges_dict = {}

    i = 0
    for e1, e2 in edges:
      if e1 not in self.edges_dict:
        self.edges_dict[e1] = e1
      if e2 not in self.edges_dict:
        self.edges_dict[e2] = e2
      p1 = self.find_parent(e1)
      p2 = self.find_parent(e2)
      if p1 == p2:
        return False
      else:
        self.union(e1, e2)
      i += 1

    if i != n - 1:
      # print("i", i)
      return False

    checks = [
        1 if self.find_parent(e) == e else 0 for e in self.edges_dict.keys()
    ]
    # print("checks", checks)
    return (sum(checks) == 1 or i == n - 1)

  def find_parent(self, e):
    if self.edges_dict[e] == e:
      return e
    return self.find_parent(self.edges_dict[e])

  def union(self, e1, e2):
    e1_set = self.find_parent(e1)
    e2_set = self.find_parent(e2)
    if e1_set != e2_set:
      self.edges_dict[e1_set] = e2_set