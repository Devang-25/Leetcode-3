"""
684. Redundant Connection
Medium

641

190

Favorite

Share
In this problem, a tree is an undirected graph that is connected and has no cycles.

The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), with one additional edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] with u < v, that represents an undirected edge connecting nodes u and v.

Return an edge that can be removed so that the resulting graph is a tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array. The answer edge [u, v] should be in the same format, with u < v.

Example 1:
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given undirected graph will be like this:
  1
 / \
2 - 3
Example 2:
Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
Output: [1,4]
Explanation: The given undirected graph will be like this:
5 - 1 - 2
    |   |
    4 - 3


解题思路：
使用union find 来解决这个题目：
当两个已经在同一个subset里（或者拥有同样的root)的两个节点要连接在一起的时候，cycle发生。


- 利用dict来存储每个节点的跟root. 
- 每当一条边来的时候，有3种情况：
1）两个都是新节点（a, b)：a当是root,另外一个的节点b的root存储a
2）一个是新的(a)，一个是旧的(b): 把b的root存成a
3)两个都是旧的节点：1）如果两个的根节点一样的话，返回这两个节点；2）union这两个节点的根节点

- 3个函数：
1)执行上面的主要逻辑
2）find_parent函数
3）union函数


"""

from collections import defaultdict


class Solution(object):

  def findRedundantConnection(self, edges):
    """
    :type edges: List[List[int]]
    :rtype: List[int]
    """
    self.vertex_root_dict = defaultdict(int)

    for edge in edges:
      a, b = edge
      if a not in self.vertex_root_dict and b not in self.vertex_root_dict:
        self.vertex_root_dict[a] = a
        self.vertex_root_dict[b] = a
      elif a in self.vertex_root_dict and b not in self.vertex_root_dict:
        self.vertex_root_dict[b] = self.vertex_root_dict[a]
      elif a not in self.vertex_root_dict and b in self.vertex_root_dict:
        self.vertex_root_dict[a] = self.vertex_root_dict[b]
      elif a in self.vertex_root_dict and b in self.vertex_root_dict:
        if self.find_parent(a) == self.find_parent(b):
          return [a, b]
        else:
          self.union(a, b)

  def find_parent(self, v):
    if self.vertex_root_dict[v] == v:
      return v
    if self.vertex_root_dict[v] != v:
      return self.find_parent(self.vertex_root_dict[v])

  def union(self, a, b):
    a_set = self.find_parent(a)
    b_set = self.find_parent(b)
    self.vertex_root_dict[a_set] = b_set


s = Solution()

edges = [[1, 2], [1, 3], [2, 3]]
# Output: [2,3]
print("edges", edges, "\nresult", s.findRedundantConnection(edges))

edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
# Output: [1,4]
print("edges", edges, "\nresult", s.findRedundantConnection(edges))

edges = [[3, 4], [1, 2], [2, 4], [3, 5], [2, 5]]
# output = [2, 5]
print("edges", edges, "\nresult", s.findRedundantConnection(edges))
