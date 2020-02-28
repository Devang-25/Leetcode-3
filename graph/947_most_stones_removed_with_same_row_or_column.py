"""
947. Most Stones Removed with Same Row or Column
Medium

422

112

Favorite

Share
On a 2D plane, we place stones at some integer coordinate points.  Each coordinate point may have at most one stone.

Now, a move consists of removing a stone that shares a column or row with another stone on the grid.

What is the largest possible number of moves we can make?

 

Example 1:

Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Example 2:

Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
Example 3:

Input: stones = [[0,0]]
Output: 0


解题思路：
- 其实所有的在直接或间接(通过中间别的石头相连)的石头都算在一个set里。
- 而且每一个set只需要留下一个石头。其他的石头都可以去掉。
- 因此可以用union find 来做。

技巧：
- 因为每个石头的位置是(x, y) coordinate,因此为了不让x和y的值clashes, 因此我们需要转换一下y. 
- 转换用的方面： bitwise inverse (~y)

"""


class Solution(object):

  def removeStones(self, stones):
    """
    :type stones: List[List[int]]
    :rtype: int
    """
    self.stones_dict = {}

    for x, y in stones:
      print("\nstone: {},{}".format(x, y))
      if x not in self.stones_dict and (~y) not in self.stones_dict:
        self.stones_dict[x] = x
        self.stones_dict[~y] = x
      elif x not in self.stones_dict and (~y) in self.stones_dict:
        self.stones_dict[x] = self.find_parent(~y)
      elif x in self.stones_dict and (~y) not in self.stones_dict:
        self.stones_dict[~y] = self.find_parent(x)
      elif x in self.stones_dict and (~y) in self.stones_dict:
        self.union(x, ~y)

    parents = set([self.find_parent(x) for x in self.stones_dict.keys()])
    print("parents", parents)
    return len(stones) - len(parents)

  def find_parent(self, x):
    if self.stones_dict[x] == x:
      return x
    return self.find_parent(self.stones_dict[x])

  def union(self, x, y):
    xr = self.find_parent(x)
    yr = self.find_parent(y)
    if xr != yr:
      self.stones_dict[xr] = yr


s = Solution()

# stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
# r = s.removeStones(stones)
# print("result", r)
# assert r == 5

# stones = [[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]
# r = s.removeStones(stones)
# print("result", r)
# assert r == 3

stones = [[0, 1], [1, 0], [1, 1]]
r = s.removeStones(stones)
print("result", r)
# assert r == 3
