# from typing import List

# class Solution:

#   def __init__(self):
#     self.min_steps = float("inf")

#   def racecar(self, target: int) -> int:
#     self.recursion_update([0], [1], target, [0], [""])
#     return self.min_steps

#   def update_status(self, p0, s0, action0):
#     # print("\np0:{}, s0:{}, action0:{}".format(p0, s0, action0))
#     if action0 == "A":
#       p1 = p0 + s0
#       s1 = s0 * 2

#     elif action0 == "R":
#       p1 = p0
#       s1 = -1 if s0 > 0 else 1
#     # print("p1: {}, s1: {}".format(p1, s1))
#     return p1, s1

#   def recursion_update(self, positions, speeds, target, steps, routes):
#     if not positions or not speeds:
#       return

#     new_positions = []  # List[int]
#     new_speeds = []  # List[int]
#     new_steps = []  # List[int]
#     new_routes = []  # List[str]

#     ps = list(zip(positions, speeds))
#     print("ps", ps)
#     for i, (p0, s0) in enumerate(ps):
#       # print("index:{}, position: {}, speed: {}, target:{}, step:{}, route:{}".
#       #       format(i, positions[i], speeds[i], target, steps[i], routes[i]))
#       if p0 == target:
#         if steps[i] < self.min_steps:
#           self.min_steps = steps[i]
#           continue

#       actions = ["A", "R"]
#       for action in actions:
#         if steps[i] + 1 < self.min_steps:
#           p1, s1 = self.update_status(p0, s0, action)
#           step = steps[i] + 1
#           new_positions.append(p1)
#           new_speeds.append(s1)
#           new_steps.append(step)
#           print("new_route", routes[i] + action)
#           new_routes.append(routes[i] + action)

#     self.recursion_update(new_positions, new_speeds, target, new_steps,
#                           new_routes)

# # sol = Solution()
# # actions = "AAARA"
# # p = 0
# # s = 1
# # print("p0:{}, s0:{}".format(p, s))
# # for action in actions:
# #   p, s = sol.update_status(p, s, action)

# # sol = Solution()
# # print(sol.recursion_update([], [], 3, [], []))

# sol = Solution()
# # print(sol.recursion_update([0], [1], 3, [0], [""]))
# target = 3
# print(sol.racecar(target))

# sol = Solution()
# # print(sol.recursion_update([0], [1], 3, [0], [""]))
# target = 6
# print(sol.racecar(target))

#################################################
import math
from collections import defaultdict


class Solution:

  def __init__(self):
    # distance_i: here is from 0 to i, speed from 1 and toward i
    self.cache = defaultdict(int)  # {distance: min_steps}
    self.cache[0] = 0

  def racecar(self, target: int) -> int:
    if target in self.cache:
      return self.cache[target]

    n = target.bit_length()
    if (2**n - 1) == target:
      self.cache[target] = n
    else:
      # exceed target and return
      self.cache[target] = self.racecar(2**n - 1 - target) + n + 1
      for m in range(n):
        for k in range(m):
          # print("original", self.cache[target])
          # print("1stA:{}, 2ndA:{}".format(m, k))
          self.cache[target] = min(
              self.cache[target],
              m + 1 + k + 1 + self.racecar(target - 2**m + 2**k))
    # print("cache", self.cache)
    # print([item for item in self.cache.items()])
    return self.cache[target]


sol = Solution()
print(sol.racecar(3))  # 2
print(sol.racecar(4))  # 5
print(sol.racecar(6))  # 5
