"""
https://www.1point3acres.com/bbs/thread-488000-1-1.html


求array的range sum，生成sum数组，每次求range sum只要O(1)

inputs: [1, 2, 3, 4]
1, 2 = 3
1, 3= 4
1, 4 = 5
2, 3 = 6
3, 4 = 7

range_sum = [3, 7]

get_range_sum
return [3, 7]
# in O(1) time complexity


a = [1, 2, 3, 4, 5]

i    0  1  2  3  4

           |        |

range_sum(a, 2, 5) == sum([2, 3, 4]) = 9
range_sum(a, 2, 3) == sum([2]) = 2


range_sum(a, 0, 3)
= range_sum(a, 0, 2) + a[2]
= range_sum(a, 0, 1) + a[1] + a[2]
= range_sum(a, 0, 0) + a[0] + a[1] + a[2]
= a[0] + a[1] + a[2]

Pre-compute range_sum(a, 0, j) = sum(a[:j])

range_sum(a, i, j) = sum(a[:j]) - sum(a[:i])



range_sum(a, i, j) = sum(a[:j])    # exclusive: not includeing a[j] <--- WRONG
                   = sum(a[:j+1])  # inclusive: including a[j]   <----- correct



get_range_sum(a, start, end) == sum(a[start:end])
"""

class RangeSum:
  def __init__(self, arr):
    self.arr_ = arr
    self.cache_ = [0] * (len(arr) + 1)  # i-th value will be sum(arr[:i])

    # arr[:j+1] = arr[:j] + arr[j]
    # cache[i] = sum(arr[:i+1])
    # cache[0] = arr[0]
    # cache[1] = arr[0] + arr[1]
    #
    # Initially, cache = [0, 0, 0, ...]
    # cache[-1] = 0
    for i, num in enumerate(arr):
      self.cache_[i + 1] = self.cache_[i] + num

  def get_range_sum(self, start, end):
    """
    Inputs:
      start: Int. Starting index.
      end: Int.

    Returns:
      Int. sum(arr[start:end])
    """
    if start > end:
      return 0

    if start >= len(self.arr_) or start < 0:
      return 0

    if end >= len(self.arr_) or end < 0:
      return 0

    # range_sum[a, i, j] = arr_[i:j+1]
    #                    = arr_[:j+1] - arr_[:i]
    #                    = cache[j+1] - cache[i]
    return self.cache_[end + 1] - self.cache_[start]



# Test cases.
# a = []  --> no matter what start or end, always return 0
# a = [1] ->
# a = [1, 2, 3] ->
# a = [1, 2, 3]. Check for different start and end
#   start == end     --> a[start]
#   start > end      --> 0
#   start > len(a)   --> 0
#   end > len(a)     --> 0
#   start < 0        --> 0
#   end < 0          --> 0

a = []
rs = RangeSum(a)
assert rs.get_range_sum(1, 3) == 0
assert rs.get_range_sum(0, 0) == 0


a = [1]
rs = RangeSum(a)
assert rs.get_range_sum(1, 3) == 0
assert rs.get_range_sum(0, 0) == 1




a = [1, 2, 3]
rs = RangeSum(a)
assert rs.get_range_sum(1, 3) == 0
assert rs.get_range_sum(1, 2) == sum(a[1:2+1])
