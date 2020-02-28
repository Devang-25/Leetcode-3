from collections import defaultdict
from typing import List
""""
Problem:

209. Minimum Size Subarray Sum
Medium

1129

72

Favorite

Share
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.


解题思路1 (dynamic programming)：
- 需要找到最小的连续数组的和大于给定的目标
- 这是一个dynamic programming problem: 需要知道为了下一步，我该步需要记录什么。

- 1)从左往右，每次碰到一个数字，先把该数字的加到目前的总和上 (for loop)
- 2）如果目前的总和大于目标，看看如果把最左边的数字去掉是否还能大于目标 （while loop)
- 3）每次删减掉左边的一个数字时，查看目前的元素数量是否小于历史的最小元素数量：如果是，更新历史最小的元素数量

corner cases:
1)
- []: empty list

2) sum of list < target
- [1, 1,] target = 3
- in this case, return 0

Time complexity:

Solution 1: O(N).
- b/c we iterate through the list onnce. 

解题思路2 （binary search):
- 先看看有没有长度是nums的aray符合这个。(min_len = len(nums))
- 再看看有没有长度是目前一半的array的和超过目标。（i=0， j = len(nums), mid = (i + j)/2, min_len = mid)
  - 如果有： 继续重复一上一步。(重复：i = 0, j = mid - 1, mid = (i + j) / 2, min_len = mid)
  - 如果没有：(i = mid + 1)
"""


class Solution:

  def minSubArrayLen(self, s: int, nums: List[int]) -> int:
    # def minSubArrayLen(self, s, nums):
    if not nums:
      return 0

    total = 0
    l = 0
    r = -1
    min_eles = float("inf")

    for i in range(len(nums)):
      total += nums[i]
      r += 1
      # print("l:{}, r:{}, total:{}".format(l, r, total))
      """
      check for boundary conditions: 
      1) l < r: then we still have still to reduce one more element
      2) total - nums[l] >= s
      """
      while l < r and total - nums[l] >= s:
        total -= nums[l]
        l += 1
        # print("update--   l:{}, r:{}, total:{}".format(l, r, total))
      if (r - l + 1) < min_eles and total >= s:
        min_eles = (r - l + 1)
        # print("min eles", min_eles)
    """
    check for boundary condition (such as []):
    1) edge case 1: []
      - if we have empty list [], then we never enter the for loop. 
      - Thus, the min_eles would be inf. 
      - In the case, we need to return 0. 

    2) edge case 2: target = 3, nums = [1, 1,], return 0
      - though r != -1, but we did NOT update min_eles.
      - min_eles is inf, b/c total never exceed target.
      - in this, we return 0.

    thus, we return 0 if did not find an anwers. 
    failure to find answer is indiate by min_eles == inf.
    
    """
    return min_eles if min_eles != float("inf") else 0

  # def minSubArrayLen(self, s: int, nums: List[int]) -> int:
  #   # def minSubArrayLen(self, s, nums):
  #   if not nums:
  #     return None

  #   cur_sum = 0
  #   cur_nums = defaultdict(int)
  #   min_val = float("inf")
  #   for num in nums:
  #     cur_sum += num
  #     cur_nums[num] += 1
  #     if num < min_val:
  #       min_val = num

  #     while (cur_sum - min_val) > s:
  #       # print("cur_sum:{}, cur_num:{}, cur_min:{}".format(
  #       # cur_sum, num, min_val))
  #       # update dict
  #       cur_sum -= min_val
  #       cur_nums[min_val] -= 1
  #       if cur_nums[min_val] <= 0:
  #         del cur_nums[min_val]
  #       keys = [key for key in cur_nums.keys()]
  #       min_val = min(keys) if keys else float("inf")

  #   print("dict", cur_nums)
  #   r = sum([v for v in cur_nums.values()])
  #   return r or None


s = Solution()

t = 7
nums = [2, 3, 1, 2, 4, 3]
r = s.minSubArrayLen(t, nums)
print(nums, "s:{}, result:{}".format(t, r), "\n")

t = 7
nums = []
r = s.minSubArrayLen(t, nums)
print(nums, "s:{}, result:{}".format(t, r), "\n")

t = 0
nums = [2, 3, 1, 2, 4, 3]
r = s.minSubArrayLen(t, nums)
print(nums, "s:{}, result:{}".format(t, r), "\n")

t = 0
nums = []
r = s.minSubArrayLen(t, nums)
print(nums, "s:{}, result:{}".format(t, r), "\n")

t = 213
nums = [12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12]
r = s.minSubArrayLen(t, nums)
print(nums, "s:{}, result:{}".format(t, r), "\n")
