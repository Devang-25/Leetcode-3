"""
Time Complexity: O(N) , where n = length of stones

"""

from collections import defaultdict


class Solution:
  # def __init__(self):
  #   self.visited = defaultdict(list) # {position: [speed]}

  def canCross(self, stones):
    # self.visited = defaultdict(list)
    self.visited = set()  # set(tuple(pos, speed))
    self.destination = stones[-1]
    self.stones = set(stones)

    return self.find_next_steps([0], [1])

  def find_next_steps(self, cur_positions, cur_speeds):
    if cur_positions and cur_speeds:
      next_positions = []
      next_speeds = []
      assert len(cur_positions) == len(cur_speeds)
      for i in range(len(cur_positions)):
        cur_pos = cur_positions[i]
        cur_speed = cur_speeds[i]
        if cur_pos == 0 and cur_speed == 1:
          speeds = [1]
        else:
          speeds = [cur_speed - 1, cur_speed, cur_speed + 1]
        # note: speed cannot be 0 or negative

        for s in speeds:
          if s > 0:
            next_pos = cur_pos + s
            if next_pos in self.stones:
              if (next_pos, s) not in self.visited:
                next_positions.append(next_pos)
                next_speeds.append(s)
                self.visited.add((next_pos, s))

      if self.arrived(next_positions):
        return True
      if not next_positions and not next_speeds:
        return False
      else:
        return self.find_next_steps(next_positions, next_speeds)

  def arrived(self, next_positions):
    if self.destination in next_positions:
      return True
    return False


stones = [0, 1, 3, 5, 6, 8, 12, 17]
s = Solution()
r = s.canCross(stones)
print("stones:{}, r:{}".format(stones, r))

stones = [0, 1, 2, 3, 4, 8, 9, 11]
s = Solution()
r = s.canCross(stones)
print("stones:{}, r:{}".format(stones, r))

stones = [0, 2]
s = Solution()
r = s.canCross(stones)
print("stones:{}, r:{}".format(stones, r))

stones = [0, 1]
s = Solution()
r = s.canCross(stones)
print("stones:{}, r:{}".format(stones, r))
