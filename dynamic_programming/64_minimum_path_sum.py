"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.

"""

class Solution(object):
    def minPathSum1(grid):
    cols = len(grid[0])
    rows = len(grid)
    # build a result same shape as grid with all 0s
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    result[0][0] = grid[0][0]
    for col in range(1, cols):
        result[0][col] = result[0][col - 1] + grid[0][col]
    for row in range(1, rows):
        for col in range(cols):
            result[row][col] = min(result[row-1][col], result[row][col-1]) + grid[row][col]
    return result[rows-1][cols-1]

    def minPathSum2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        cols = len(grid[0])
        rows = len(grid)
        result = [0] * cols
        result[0] = grid[0][0]
        for col in range(1, cols):
            result[col] = result[col - 1] + grid[0][col]
        for row in range(1, rows):
            for col in range(cols):
                result[col] = min(result[col], result[col-1]) + grid[row][col]
        return result[cols-1]

grid1 = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
# output 7, path: 1-3-1-1-1
Solution().minPathSum1(grid1)
Solution().minPathSum2(grid1)
