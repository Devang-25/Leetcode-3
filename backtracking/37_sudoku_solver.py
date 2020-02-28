debug = True


def dprint(*args, **kwargs):
  if debug == True:
    print(*args, **kwargs)


class Solution(object):

  def __init__(self, board):
    self.board = board

  def solveSudoku(self, board):
    """
    :type board: List[List[str]]
    :rtype: None Do not return anything, modify board in-place instead.

    steps:
    1) when is given a sudoku, check if it has any unfilled.
      2) if it is filled, check if it is solved.
        3)if it is solved, return (True, solved board).
        3.1) if it is not solved, return to (False, board)
      4) if it has unfilled:
        5) find candidates for this pos
        6) find the pos with one of the candidates. (using for loop):
          7) return: repeat step 1-6 by recursively called the function:
            8) if step 7 return: (True, solved sudoku)
            9) if step 7 return: (False, wrong sudoku):

    """
    # self.board = board
    pos = self.find_unfilled()
    candidates = self.find_candidates(pos)
    s = self._solve(pos, candidates)
    dprint("solution", s)
    dprint("board:")
    for row in self.board:
      dprint(row)
    return

  def _solve(self, pos, candidates):
    dprint("\n")
    dprint("pos: {}, candidates:{}".format(pos, candidates))
    for row in self.board:
      dprint(row)
    x, y = pos
    for candidate in candidates:
      dprint("let's try pos {} with candidate {}".format(pos, candidate))
      self.board[x][y] = candidate
      solve_sudoku = self.is_solved()
      if solve_sudoku:
        dprint("solved sudoku", self.board)
        return True
      elif not self.find_unfilled() and not solve_sudoku:
        dprint("filled but not solved", pos, candidate)
        # self.board[x][y] = "."
      elif self.find_unfilled():
        new_pos = self.find_unfilled()
        new_candidates = self.find_candidates(new_pos)
        dprint("still has empty space {} with candidates {}".format(
            new_pos, new_candidates))
        if not new_candidates:
          dprint("has empty space {} has no candidate".format(new_pos))
        elif new_candidates:
          solution = self._solve(new_pos, new_candidates)
          if solution:
            return True
    self.board[x][y] = "."
    return False

  def find_unfilled(self):
    for row in range(9):
      for col in range(9):
        if self.board[row][col] == ".":
          return row, col
    dprint("sudoku is filled")
    return False

  def is_solved(self):
    """
    purpose: check if a sudoku board is solved.

    inputs: None
    outputs: bool

    Approach: 
    1) check each row
    2) check each col
    3) check each 3x3 square
    """

    if self.find_unfilled():
      return False

    # row
    for row in self.board:
      row_i = [n for n in row if n != "."]
      row_i = set(row_i)
    if len(row_i) == 9:
      row_check = True
    else:
      dprint("row has problem")
      return False

    # check col
    for c in range(len(self.board[0])):
      col_i = [
          self.board[r][c]
          for r in range(len(self.board))
          if self.board[r][c] != "."
      ]
      col_i = set(col_i)
    if len(col_i) == 9:
      col_check = True
    else:
      dprint("col has problem")
      return False

    # check square
    for r in range(0, len(self.board), 3):
      for c in range(0, len(self.board[0]), 3):
        # r = 0, c = 0
        square_i = [
            self.board[rr][cc]
            for rr in range(r)
            for cc in range(c)
            if self.board[rr][cc] != "."
        ]
        square_i = set(square_i)
    if len(square_i) == 9:
      square_check = True
    else:
      dprint("square has problem")
      return False

    if row_check and col_check and square_check:
      return True
    else:
      return False

  def find_candidates(self, pos):
    x, y = pos
    assert self.board[x][y] == "."
    candidates = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}

    # row
    for col in range(9):
      if self.board[x][col] != "." and self.board[x][col] in candidates:
        candidates.remove(self.board[x][col])

    for row in range(9):
      if self.board[row][y] != "." and self.board[row][y] in candidates:
        candidates.remove(self.board[row][y])

    square_x = int(x / 3)
    square_y = int(y / 3)
    dprint("square x: {}, square y:{}".format(square_x, square_y))
    for row in range(square_x * 3, square_x + 3):
      for col in range(square_y * 3, square_y + 3):
        if self.board[row][col] != "." and self.board[row][col] in candidates:
          candidates.remove(self.board[row][col])

    return candidates


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

board1 = [
    ["5", "3", ".", ".", "7", "8", "9", "1", "2"],
    ["6", ".", ".", "1", "9", "5", "3", "4", "8"],
    ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
    ["8", ".", "9", "7", "6", "1", "4", "2", "3"],
    ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
    ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
    ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
    ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
    ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
]

board_ans = [
    ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
    ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
    ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
    ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
    ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
    ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
    ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
    ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
    ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
]

solved_sudoku = [
    ['5', '3', '4', '9', '7', '6', '8', '1', '2'],
    ['6', '2', '7', '1', '9', '5', '4', '3', '8'],
    ['1', '9', '8', '2', '3', '7', '5', '6', '4'],
    ['8', '4', '9', '7', '6', '2', '1', '5', '3'],
    ['4', '7', '2', '8', '5', '3', '6', '9', '1'],
    ['7', '1', '3', '5', '2', '8', '9', '4', '6'],
    ['9', '6', '5', '3', '4', '1', '2', '8', '7'],
    ['3', '8', '6', '4', '1', '9', '7', '2', '5'],
    ['2', '5', '1', '6', '8', '4', '3', '7', '9'],
]

# s = Solution()
# sol = s.solveSudoku(board)
# assert s.board == board_ans

# print("my solution is:")
# for row in s.board:
#   print(row)
# print("my solution is", sol)

s = Solution(solved_sudoku)
# s.solveSudoku(solved_sudoku)
print(s.is_solved())
