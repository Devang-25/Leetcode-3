"""
time complexity: O(Log mxn)

space complexity: O(1)

"""


class Solution(object):

  def searchMatrix(self, matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    if not matrix:
      return -1

    l = 0
    r = len(matrix) * len(matrix[0]) - 1

    while l <= r:
      mid = (l + r) // 2
      row = mid // len(matrix[0])
      col = mid % len(matrix[0])
      print("mid: {}, row:{}, col:{}".format(mid, row, col))
      num = matrix[row][col]
      # print("row:{}, c:{}, num:{}".format(row, col, num))
      if num == target:
        return True
      elif num < target:
        # go to right
        l = mid + 1
      elif num > target:
        r = mid - 1
    return False


matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50],
]

target = 3

###############

matrix = []
taret = 0

#############

matrix = [[1, 1]]
target = 2

s = Solution()
print(s.searchMatrix(matrix, target))
