from collections import defaultdict


class Solution(object):

  def fourSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]

    Overall Time complexity: O(N^2) + O(N^2) == O(N^2)
    """
    nums.sort()
    self.nums = nums
    print("nums", self.nums)
    self.dict = defaultdict(list)
    self.results = []
    self.hash = set()
    self.twoSum()
    """
    Time complexity: O(N^2)
    """
    for total1 in self.dict:
      total2 = target - total1
      if total2 in self.dict:
        candidates = [
            set([i, j, l, m])
            for i, j in self.dict[total1]
            for l, m in self.dict[total2]
        ]
        for candidate in candidates:
          if len(candidate) == 4:
            i, j, l, m = candidate
            r = [self.nums[i], self.nums[j], self.nums[l], self.nums[m]]
            r.sort()
            if tuple(r) not in self.hash:
              self.hash.add(tuple(r))
              self.results.append(r)

    return self.results

  def twoSum(self):
    """
    Time complexity: O(N^2)
    """
    for i in range(len(self.nums)):
      for j in range(i + 1, len(self.nums)):
        total = self.nums[i] + self.nums[j]
        self.dict[total].append([i, j])



##########################################

from collections import defaultdict


class Solution(object):

  def fourSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]

    Overall Time complexity: O(N^2) + O(N^2) == O(N^2)
    """
    nums.sort()
    self.nums = nums
    self.dict = defaultdict(list)
    self.results = []
    self.hash = set()
    self.twoSum()
    """
    Time complexity: O(N^2)
    """

    totals = [key for key in self.dict]
    totals.sort()
    l = 0
    r = len(totals) - 1
    while l <= r:
      total = totals[l] + totals[r]
      if total == target:
        candidates = [
            set([i, j, k, m])
            for i, j in self.dict[totals[l]]
            for k, m in self.dict[totals[r]]
        ]
        for candidate in candidates:
          if len(candidate) == 4:
            i, j, k, m = candidate
            result = [self.nums[i], self.nums[j], self.nums[k], self.nums[m]]
            result.sort()
            if tuple(result) not in self.hash:
              self.hash.add(tuple(result))
              self.results.append(result)
        r -= 1
      elif total > target:
        r -= 1
      elif total < target:
        l += 1

    return self.results

  def twoSum(self):
    """
    Time complexity: O(N^2)
    """
    for i in range(len(self.nums)):
      for j in range(i + 1, len(self.nums)):
        total = self.nums[i] + self.nums[j]
        self.dict[total].append([i, j])


nums = [1, 0, -1, 0, -2, 2]
target = 0

nums = [-3, -2, -1, 0, 0, 1, 2, 3]
target = 0

nums = [1, -2, -5, -4, -3, 3, 3, 5]
target = -11

nums = [0, 0, 0, 0]
target = 0

s = Solution()
r = s.fourSum(nums, target)
print("result", r)