"""

input:
row * col
matrix:

return the col number you would like to flip to maximize the number of rows that have same letters throughout.



"""

import copy`


def puzzle_box(row, col, matrix):
  max_wishes = 0

  for c in range(col):
    new_matrix = copy.deepcopy(matrix)
    for r in range(row):
      new_matrix[r][c] = "T" if matrix[r][c] == "P" else "P"
    wishes = check_wishes(row, col, new_matrix)
    if wishes > max_wishes:
      max_wishes = wishes
  return max_wishes


def check_wishes(row, col, matrix):

  wishes = 0

  for r in range(row):
    pattern_1 = [matrix[r][c] == "T" for c in range(col)]
    pattern_2 = [matrix[r][c] == "P" for c in range(col)]

    if all(pattern_1) or all(pattern_2):
      wishes += 1

  return wishes


row = 5
col = 3
matrix = [
    ["T", "T", "P"],
    ["P", "T", "P"],
    ["T", "P", "P"],
    ["P", "T", "P"],
    ["T", "P", "T"],
]
# return 3

print(puzzle_box(row, col, matrix))
