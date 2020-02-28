import math
import copy


class Solution:

  def solveSudoku(self, board):
    self.board = board
    self.solve()

  def findempty(self):
    for r in range(9):
      for c in range(9):
        if self.board[r][c] == ".":
          return r, c
    return -1, -1

  def solve(self):
    r, c = self.findempty()
    if r == -1 and c == -1:
      return True
    for num in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      if self.issafe(r, c, num):
        self.board[r][c] = num
        if self.solve():
          return True
        self.board[r][c] = "."
    return False

  def issafe(self, r, c, ch):
    if self.checkrow(r, ch) and self.checkcol(c, ch) and self.checksquare(
        r, c, ch):
      return True
    return False

  def checkrow(self, r, ch):
    for c in range(9):
      if self.board[r][c] == ch:
        return False
    return True

  def checkcol(self, c, ch):
    for r in range(9):
      if self.board[r][c] == ch:
        return False
    return True

  def checksquare(self, r, c, ch):
    start_r = math.floor(r / 3)
    start_c = math.floor(c / 3)
    for rr in range(start_r * 3, start_r * 3 + 3):
      for cc in range(start_c * 3, start_c * 3 + 3):
        if self.board[rr][cc] == ch:
          return False
    return True


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

s = Solution()
r = s.solveSudoku(board)
print("r", r)