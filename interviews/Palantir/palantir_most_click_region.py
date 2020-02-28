class Solution:

  def __init__(self, matrix):
    """
    inputs:
      matrix: list[[int]]
    """
    self.max_clicks = 0
    self.matrix = matrix

  def most_click_region(self):
    """
    output:
      self.max_clicks: int
    """
    if not self.matrix:
      return None

    for i in range(len(self.matrix)):
      for j in range(len(self.matrix[0])):
        total = self.check_grid(i, j)
        if total > self.max_clicks:
          self.max_clicks = total

    return self.max_clicks

  def check_grid(self, r, c):
    # print("check [{}][{}]: {}".format(r, c, self.matrix[r][c]))
    # if r < 0 or r >= len(self.matrix) or c < 0 or c >= len(self.matrix[0]):
    #   return 0

    clicks = self.matrix[r][c]

    if clicks == 0:
      return 0

    if clicks != 0:
      self.matrix[r][c] = 0
      neighbors = [[r - 1, c], [r, c + 1], [r + 1, c], [r, c - 1]]
      for neighbor in neighbors:
        r1, c1 = neighbor
        if r1 < 0 or r1 >= len(self.matrix) or c1 < 0 or c1 >= len(
            self.matrix[0]):
          continue
        else:
          clicks += self.check_grid(r1, c1)

    return clicks


matrix = [[1, 0], [2, 0]]

s = Solution(matrix)
# r = s.most_click_region()
# print(r)
s.most_click_region() == 3

################

matrix = [[0]]

s = Solution(matrix)
# r = s.most_click_region()
# print(r)
s.most_click_region() == 0

##############

matrix = []

s = Solution(matrix)
# r = s.most_click_region()
# print(r)
s.most_click_region() == None

###############

matrix = [[1, 0], [0, 3]]

s = Solution(matrix)
# r = s.most_click_region()
# print(r)
s.most_click_region() == 3