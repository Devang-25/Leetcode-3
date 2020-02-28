"""
240. Search a 2D Matrix II
Medium

1528

43

Favorite

Share
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

------------------

binary search: 
- start from the top right corner. 
- if cur value is smaller than target: go down one more row
- if the cur value is bigger than target: go left one more col

corner cases:
- []
- [[]]

time complexity: 
O(M + N)

potentially improvment: 
- make the starting point from the mid of all the rows (while still the last col). 
  - choose to go up or down using binary search
- then time complexity is O(log M) + N
"""


class Solution:

  def searchMatrix(self, matrix, target):
    """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
    if not matrix or not matrix[0]:
      return False

    r = 0
    c = len(matrix[0]) - 1
    # while 0 <= r < len(matrix) and 0 <= c < len(matrix[0]):
    while r < len(matrix) and c >= 0:
      if matrix[r][c] == target:
        return True
      elif matrix[r][c] > target:
        c -= 1
      elif matrix[r][c] < target:
        r += 1
    return False


s = Solution()

matrix = [[-5]]
target = -2
r = s.searchMatrix(matrix, target)
print('result', r, "\n")
assert r == False

matrix = [[1, 1]]
target = 2
r = s.searchMatrix(matrix, target)
print('result', r, "\n")
assert r == False

matrix = [[-1, 3]]
target = 3
r = s.searchMatrix(matrix, target)
print('result', r, "\n")
assert r == True