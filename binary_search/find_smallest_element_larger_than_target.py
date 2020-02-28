"""
problem: 
find the smallest number in the nums that is larger than target.

"""


def find_smallest_num_larger_than_target(nums, target):
  """
  inputs:
    nums: list[int]
    target: int

  output: int
  """
  if not nums:
    return -1

  l = 0
  r = len(nums) - 1

  while l < r:
    mid = (l + r) // 2
    print("l", l, "r", r, "mid", mid)
    if nums[mid] == target:
      l = mid + 1
    if nums[mid] < target:
      l = mid + 1
    elif nums[mid] > target:
      r = mid

  if nums[l] > target:
    print("index", l, "nums", nums[l])
    return nums[l]
  return -1


nums = [1]
target = 0

nums = [0, 1]
target = 0

nums = [0, 0, 1]
target = 0

nums = [0, 1, 1, 2, 3, 4, 5]
target = 4

print(find_smallest_num_larger_than_target(nums, target))