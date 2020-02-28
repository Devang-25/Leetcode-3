from collections import defaultdict


class Solution(object):

  def fourSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    self.results = []
    self.hash = set()

    self.nums = nums
    self.nums.sort()
    self.moreSum(0, 4, target, [])
    return self.results

  def twoSum(self, start, target, result):
    end = len(self.nums) - 1
    while start < end:
      if self.nums[start] + self.nums[end] == target:
        r = result + [self.nums[start], self.nums[end]]
        if tuple(r) not in self.hash:
          self.results.append(r)
          self.hash.add(tuple(r))
        print("new", r)
        end -= 1
      elif self.nums[start] + self.nums[end] > target:
        end -= 1
      else:
        start += 1

  def moreSum(self, start, n, target, result):
    end = len(self.nums) - 1
    if n == 2:
      self.twoSum(start, target, result)
    elif n > 2:
      for i in range(start, end):
        self.moreSum(i + 1, n - 1, target - self.nums[i],
                     result + [self.nums[i]])


nums = [1, 0, -1, 0, -2, 2]
target = 0

nums = [-3, -2, -1, 0, 0, 1, 2, 3]
target = 0

nums = [1, -2, -5, -4, -3, 3, 3, 5]
target = -11

s = Solution()
r = s.fourSum(nums, target)
print("result", r)