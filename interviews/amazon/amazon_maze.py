"""### 12: 迷宫 (2019.1)

Find Path in 2D matrix.
输入一个2D的int array，其中有0，1，9。
0为墙壁 1为可以通过，9 为需要找的结果.

返回true or false，表示可以找到9或者没有办法找到。9不一定只有一个。


这道题如果真是1是路，找9比较好，可以直接用大于符号。
一亩三分地里面也有人说0是可以通过，1是墙壁，只能看着来了。出生点我定为（0,0）因为我不确定OA中给的是不是（0,0）
需要注意的特殊情况是第一个就是需要找的9，eg. {{9}}


想了一下，应该是上下左右都可以活动才对，所以又加了两个方向。感觉可以把Korsh原来写的炫酷的迷宫游戏写出来了。还是做面试准备先。
原文：https://blog.csdn.net/lycorislqy/article/details/49202651
"""
import heapq

def maze(matrix):
  """
  input matrix: [[int]]
  output: True / False
  """
  visited = set()

  candidates = [[0, 0, 0]]
  visited.add((0, 0))
  while candidates:
    candidate = heapq.heappop(candidates)
    print("candidate", candidate)
    d, r, c = candidate

    neighbors = [[r+1, c], [r, c+1], [r-1, c], [r, c-1]]
    print("neighbors", neighbors)

    for neighbor in neighbors:
      r1, c1 = neighbor

      # check neighbor boundary
      if r1 < 0 or r1 >= len(matrix) \
      or c1 < 0 or c1 >= len(matrix[r1]):
        print("out of boundary")
        continue

      print("neighbor, row{}, col{}, val{}".format(r1, c1, matrix[r1][c1]))

      if matrix[r1][c1] == 9:
        print("found", neighbor)
        return True

      elif matrix[r1][c1] == 1:
        if (r1, c1) not in visited:
          print("process new neighbor")
          visited.add((r1, c1))
          distance = r1 * r1 + c1 * c1
          neighbor = (distance, r1, c1)
          heapq.heappush(candidates, neighbor)
  return False

matrix = [
  [1,1, 1],
  [1,0, 1],
  [0,0, 9]]

# matrix = [
#   [1,1, 1],
#   [1,0, 1],
#   [0,0, 0]]

print(maze(matrix))
