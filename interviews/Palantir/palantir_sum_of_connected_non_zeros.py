class Solution:

  def __init__(self, board):
    self.max_sum = 0
    self.board = board

  def max_sum(self):
    for i in range(len(self.board)):
      for j in range(len(self.board[0])):
        total = self.check_grid(i, j)
        if total > self.max_sum:
          self.max_sum = total
    return self.max_sum

  def check_grid(self, i, j):
    if self.board[i][j] == 0:
      return 0

    total = self.board[i][j]
    next_moves = [[i, j - 1], [i - 1, j], [i, j + 1], [i + 1, j]]
    for r, c in next_moves:
      total += self.check_grid(r, c)
    self.board[i][j] = 0

    return total


board = [[0, 0, 1], [1, 0, 2]]

s = Solution()
r = s.max_sum(board)
print("r", r)