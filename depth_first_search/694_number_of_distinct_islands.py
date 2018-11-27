"""
694. Number of Distinct Islands
Medium
250
16


Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Example 1:
11000
11000
00011
00011
Given the above grid map, return 1.
Example 2:
11011
10000
00001
11011
Given the above grid map, return 3.

Notice that:
11
1
and
 1
11
are considered different island shapes, because we do not consider reflection / rotation.

"""

class Solution:
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        def find_island(i, j, island, x, y):
            """
            input i: int, index of current cell
            input j: int, index of current cell
            input island: list
            """
            if 0 <= i < rows and 0 <= j < cols and grid[i][j]:
                # island.append('%d,%d' % (x-i, y-j))
                island.append((x-i, y-j))
                grid[i][j] = 0
                find_island(i+1, j, island, x, y)  # right
                find_island(i, j+1, island, x, y)  # down
                find_island(i-1, j, island, x, y)  # left
                find_island(i, j-1, island, x, y)  # up
                return island

        def if_new_island(island):
            island = tuple(island)
            # island = ','.join(island)
            if island not in islands:
                islands.add(island)

        cell_to_islands = {}
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:  # is island
                    island = find_island(i, j, [], i, j)
                    # if_new_island(island)

                    cells = len(island)
                    if cells in cell_to_islands:
                        cell_to_islands[cells].append(island)
                    else:
                        cell_to_islands[cells] = [island]

        unique_count = 0
        for cell, islands in cell_to_islands.items():
            if len(islands) == 1:
                unique_count += 1
            else:
                unique_count += len(set(tuple(island) for island in islands))
        return unique_count
