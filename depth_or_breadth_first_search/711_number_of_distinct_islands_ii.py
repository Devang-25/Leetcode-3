class Solution(object):

  def numDistinctIslands2(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    self.grid = grid
    self.islands = 0
    self.cache = set()

    for r in range(len(grid)):
      for c in range(len(grid[0])):
        island = self.find_island(r, c)
        if island:
          island = self.process_island(island)
          if island not in self.cache:
            self.islands += 1
            self.find_mirrors(island)
    return self.islands

  def find_island(self, r, c):
    if self.grid[r][c] == 0:
      return []

    if self.grid[r][c] == 1:
      island = [[r, c]]
      self.grid[r][c] = 0
      neighbors = [[r - 1, c], [r, c - 1], [r + 1, c], [r, c + 1]]
      for neighbor in neighbors:
        r1, c1 = neighbor
        if 0 <= r1 < len(self.grid) and 0 <= c1 < len(self.grid[0]):
          r = self.find_island(r1, c1)
          if r:
            island += r
      return island

  def process_island(self, island):
    """
    inputs: 
      islands: List of List [[]]
    
    iii. Find its x-axis mirror: (x,y) --> (-x,y)
    iv. Find its y-axis mirror: (x,y) --> (x,-y)
    v. Find its origin mirror: (x,y) --> (-x,-y)
    vi. Find its diagonal mirror: (x,y) --> (y,x)
    """
    # find min_x
    min_x = min(island, key=lambda s: s[0])[0]
    min_y = min(island, key=lambda s: s[1])[1]

    island = tuple(sorted([(x - min_x, y - min_y) for x, y in island]))

    print("island", island)
    print("current cache", self.cache)
    return island

  def find_mirrors(self, island):
    min_x = min(island, key=lambda s: s[0])[0]
    min_y = min(island, key=lambda s: s[1])[1]

    island = tuple(sorted([(x - min_x, y - min_y) for x, y in island]))
    self.cache.add(island)

    max_x = max(island, key=lambda s: s[0])[0]
    max_y = max(island, key=lambda s: s[1])[1]

    # flip over y axis
    mirror1 = tuple(sorted([(-x + max_x, y) for x, y in island]))
    self.cache.add(mirror1)

    # flip over x axis
    mirror2 = tuple(sorted([(x, -y + max_y) for x, y in island]))
    self.cache.add(mirror2)

    # flip over origin
    mirror3 = tuple(sorted([(-x + max_x, -y + max_y) for x, y in island]))
    self.cache.add(mirror3)

    mirror4 = tuple(sorted([(y - min_y, x - min_x) for x, y in island]))
    self.cache.add(mirror4)

    mirror5 = tuple(sorted([(-y + max_y, x) for x, y in island]))
    self.cache.add(mirror5)

    mirror6 = tuple(sorted([(y, -x + max_x) for x, y in island]))
    self.cache.add(mirror6)

    mirror7 = tuple(sorted([(-y + max_y, -x + max_x) for x, y in island]))
    self.cache.add(mirror7)


islands = [[1, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 1, 1]]
s = Solution()
r = s.numDistinctIslands2(islands)
print("result", r)