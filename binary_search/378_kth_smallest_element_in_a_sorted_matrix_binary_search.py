from typing import List
"""
Solution 1: binary search solution: 
1) calculate the target (mid) (average of smallast and largest elements in matrix, lo and high), 
2) and assume that number is the kth smallest element. 
  2.1) check if that is by by counting how many element in the matrix is smaller or equal to that number. How? 
    - by starting from the top row's last col, see if that number is smaller or euqal to target number.
    - if that number is larget than target, col -= 1. until number is smaller or equal. 
    - use the col index of that number to count toward how many number is smaller or equal to target. 
    - move to next row, do the same. until a row's first element is already bigger than target number. 
3) if the count is more than k, which means the target (mid) is smaller, search range would be low ~ mid
4) if the count is less thatn k, which means the target (mid) should be higher, the search range would be mid + 1 ~ hi.

the time complexity is O(log (max - min)) where max is the max number if matrix and min is the minimum number in matrix.
"""


class Solution:

  def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    self.matrix = matrix
    self.k = k

    lo = self.matrix[0][0]
    hi = self.matrix[-1][-1]

    while lo < hi:
      mid = (lo + hi) // 2
      count = self.count(mid)
      # print("lo:{}, hi:{}, mid:{}, count:{}".format(lo, hi, mid, count))
      if count >= k:  # we need less count and thus less target number
        hi = mid
      else:
        lo = mid + 1

    # print("last lo:{}, hi:{}".format(lo, hi))
    return lo

  def count(self, target: int) -> int:
    r = 0
    c = len(self.matrix[0]) - 1

    count = 0

    for r in range(len(self.matrix)):
      while self.matrix[r][c] > target and c >= 0:
        c -= 1
      if c >= 0:
        count += (c + 1)

    return count


matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
k = 8
# return 13

matrix = [[1, 2], [3, 3]]
k = 2
# return 2

s = Solution()
print(s.kthSmallest(matrix, k))
