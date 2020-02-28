"""
323. Number of Connected Components in an Undirected Graph
Medium

400

12

Favorite

Share
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

Example 1:

Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4 

Output: 2
Example 2:

Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

     0           4
     |           |
     1 --- 2 --- 3
Output:  1

解题思路：





"""


class Node(object):

  def __init__(self, v):
    self.parent = v
    self.rank = 0


class Solution(object):

  def countComponents(self, n, edges):
    """
    :type n: int
    :type edges: List[List[int]]
    :rtype: int
    """
    self.nodes = {}
    for i in range(n):
      self.nodes[i] = Node(i)
    parents = [self.nodes[i].parent for i in range(n)]
    # print("parents", parents)

    for v1, v2 in edges:
      self.union(v1, v2)
      parents = [self.nodes[i].parent for i in range(n)]
      # print("parents", parents)

    checks = [1 if self.nodes[i].parent == i else 0 for i in range(n)]
    # print("checks", checks)

    return sum(checks)

  def find_parent(self, v):
    if self.nodes[v].parent != v:
      self.nodes[v].parent = self.find_parent(self.nodes[v].parent)
    return self.nodes[v].parent

  def union(self, v1, v2):
    p1 = self.find_parent(self.nodes[v1].parent)
    p2 = self.find_parent(self.nodes[v2].parent)
    if p1 != p2:
      r1 = self.nodes[p1].rank
      r2 = self.nodes[p2].rank
      if r1 > r2:
        self.nodes[p2].parent = p1
      elif r2 > r1:
        self.nodes[p1].parent = p2
      elif r1 == r2:
        r1 += 1
        self.nodes[p2].parent = p1