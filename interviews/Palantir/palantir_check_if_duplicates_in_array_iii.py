from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
      for i in range(len(nums)):
        for j in range(i+1, i+k+1):
          if j >= len(nums):
            break
          if abs(nums[i] - nums[j]) <= t:
            return True
      return False



Input: nums = [1,2,3,1], k = 3, t = 0
Output: true