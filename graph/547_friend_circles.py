class Solution(object):

  def findCircleNum(self, M):
    """
    :type M: List[List[int]]
    :rtype: int
    """
    self.friends_circle = {}

    for p in range(len(M)):
      if p not in self.friends_circle:
        self.friends_circle[p] = p
      for f in range(p + 1, len(M)):
        if f not in self.friends_circle:
          self.friends_circle[f] = f
        if M[p][f] == 1:
          self.union(p, f)

    circles = [
        1 if key == value else 0 for key, value in self.friends_circle.items()
    ]
    return sum(circles)

  def find_parent(self, m):
    if self.friends_circle[m] == m:
      return m
    else:
      return self.find_parent(self.friends_circle[m])

  def union(self, x, y):
    x_set = self.find_parent(x)
    y_set = self.find_parent(y)
    if x_set != y_set:
      self.friends_circle[x_set] = y_set


s = Solution()

M = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

r = s.findCircleNum(M)
print("result", r)