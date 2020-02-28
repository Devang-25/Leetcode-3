"""
3. 给一堆(x, y)的二维坐标，每一个坐标对应一个整形的score。以原点为圆心的，会有很多圆存在。需要找出一个圆，使得这个圆内的（包括圆上）所有score的和最大。

- 有些score可能是负数，因此并不是圆圈越大越好
- 打算用dynamic programming
- ith's core = (i-1)th score + new scores

问题：有办法很快的算一个点given (x, y)坐标的位置吗？
- 正常算法：radius = (x^2 + y^2)^(1/2) ==> O(1)

问题：如何找到在界定内的点？
- 1）dict (radius): score1, score2,...
- 2) heap(sorted radius) - min-heap: so pop would returnt the smallest radius - O(nlogn)
- or list(sorted radius) - O(Nlog(N))
"""

from collections import defaultdict
import heapq

def largest_score(coordinates, scores):
  if not coordinates or not scores:
    return "empty"

  cache = defaultdict(list)
  radius = set()

  for i, coord in enumerate(coordinates):
    r = (coord[0]**2 + coord[1]**2) ** (1/2)
    cache[r].append(scores[i])
    radius.add(r)
  radius = sorted(list(radius))

  max_area = 0
  max_r = 0
  area = 0

  for r in radius:
    new_area = sum(cache[r])
    area += new_area
    if area > max_area:
      max_area = area
      max_r = r

  return (max_area, max_r)

#########################Test cases ###########

# coordinates = [(0, 0), (1, 1), (1, 1.5), (2, 2)]
# scores = (5, -2, 6, -7)

coordinates = []
scores = ()

coordinates = [(0, 0), (1, 1), (-2, 2), (2, 2)]
scores = (5, -2, 7, 6)

result = largest_score(coordinates, scores)
print("max_area: {}, optimal_radius: {}".format(result[0], result[1]))
