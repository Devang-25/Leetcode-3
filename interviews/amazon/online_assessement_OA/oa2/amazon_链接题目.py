"""

1. 给你一个棋盘 int[][] board, 你可以交换任何一个棋子和它的邻居（横向或者竖向相邻的棋子），如果交换后，在横向或者竖向产生了大于等于三个连续的一样的棋子 e.g. 4 4 4
5
5
5
那么就算交换有效。(就是一个比较常见的游戏，忘记叫啥名字了)
请你写一个函数返回所有可以有效交换的棋子的坐标对。 比如 （（0， 0）， （1， 0）） ， （（3,2），（3,3））.


input = [[1,2,2],
          [2,0,2],
          [0,2,0]]
output = [[[0,0],[1,0]], [[3,2],[3,3]]]

"""

import copy
from operator import itemgetter

def board_game(board):
  results = set()

  for i in range(len(board)):
    for j in range(len(board[i])):
      candidates = [[i-1, j], [i, j+1], [i+1, j], [i, j-1]]
      for (r,c) in candidates:
        candidate = sorted([(i, j), (r, c)], key=itemgetter(0, 1))
        if tuple(candidate) not in results:
          r = check_valid(i, j, r, c, board)
          if r:
            print(type(r))
            results.add(r)


  return results

def check_valid(i, j, r, c, board):
  print("\n{}{}/{}{}".format(i, j, r, c))

  if r < 0 or r >= len(board) or c < 0 or c >= len(board[r]):
    print("no1")
    return []

  if board[i][j] == board[r][c]:
    print("no2")
    return []

  nb = copy.deepcopy(board)
  nb[i][j] = board[r][c]
  nb[r][c] = board[i][j]

  print("board")
  for row in board:
    print(row)
  print("{}{}/{}{}: {}/{}".format(i, j, r, c, board[i][j], board[r][c]))


  for ii in range(i-2, i):
    if ii >= 0 and (ii+2) < len(board):
      if nb[ii][j] == nb[ii+1][j] and nb[ii+1][j] == nb[ii+2][j]:
        print("yes1", ii)
        print("newboard")
        for row in nb:
          print(row)

        r = [(i, j), (r, c)]
        r = sorted(r, key=itemgetter(0,1))
        print(tuple(r))
        return tuple(r)

  for jj in range(j-2, j):
    if jj >=0 and (jj+2) < len(board[i]):
      if nb[i][jj] == nb[i][jj+1] and nb[i][jj+1] == nb[i][jj+2]:
        print("yes2", jj)
        print("newboard")
        for row in nb:
          print(row)

        r = [(i, j), (r, c)]
        r = sorted(r, key=itemgetter(0,1))
        print(tuple(r))
        return tuple(r)

  return []


board = [[1,2,2],
          [2,0,2],
          [0,2,0]]

print(board_game(board))
