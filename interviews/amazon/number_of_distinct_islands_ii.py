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
            print("\nfound")
            print("island", island)
            print("before cache")
            for s in self.cache:
              print(s)
            self.islands += 1
            self.find_mirrors(island)
            print("after cache", self.cache)
    return self.islands

  def find_island(self, r, c):
    if self.grid[r][c] == 0:
      return

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
    min_x = min(island, key=lambda x: x[0])[0]
    min_y = min(island, key=lambda x: x[1])[1]

    print("minx:{}, miny:{}".format(min_x, min_y))
    print(island)
    island = tuple(sorted([tuple([x - min_x, y - min_y]) for x, y in island]))
    print("after", island)

    return island

  def find_mirrors(self, island):
    self.cache.add(island)

    x_max = max([x for x, y in island])
    y_max = max([y for x, y in island])

    # x-axis mirror
    mirror1 = tuple((-x + x_max, y) for x, y in island)
    self.cache.add(mirror1)

    # y-axis mirror
    mirror2 = tuple((x, -y + y_max) for x, y in island)
    self.cache.add(mirror2)

    # flip over origin
    mirror3 = tuple((-x + x_max, -y + y_max) for x, y in island)
    self.cache.add(mirror3)

    # diagnoal mirror
    mirror4 = tuple((y, x) for x, y in island)
    self.cache.add(mirror4)

    mirror5 = tuple((-y + y_max, x) for y, x in mirror4)

    mirror6 = tuple((, -x + x_max) for y, x in mirror4)

    mirror7 = tuple((-y + y_max, -x + x_max) for y, x in mirror4)

    # mirror5 = tuple((-y + y_max, x) for y, x in mirror4)


    print("island", island)
    print("1", mirror1)
    print("2", mirror2)
    print("3", mirror3)
    print("4", mirror4)


grid = [[1, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 1, 1]]
s = Solution()
r = s.numDistinctIslands2(grid)
print("num of island:", r)
