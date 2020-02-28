"""
time complexity: O(logN)

space complexity: O(1)

"""


def find_closest_ele(nums, target):
  """
  inputs: list[int]
  output: int

  output number that is closest to target
  """
  if not nums:
    return -1

  l = 0
  r = len(nums) - 1
  """
  note: remember to consider corner case here!
  when there are only two index: such as [0, 1], 
  if we have while loop l < r, 
  then we would be never out of the loop
  """
  while l < (r - 1):
    # print("l", l, end=" ")
    # print("r", r)
    mid = (l + r) // 2
    if nums[mid] == target:
      return target
    elif nums[mid] < target:
      l = mid
    elif nums[mid] > target:
      r = mid

  # if did not find target, but find a range
  # see which num left or right is closer to target
  if abs(nums[l] - target) <= abs(nums[r] - target):
    return nums[l]
  return nums[r]


nums = [0]
target = 1

nums = [0, 3]
target = 1

nums = [1, 2, 4, 5, 6, 6, 8, 9]
target = 3

nums = [2, 5, 6, 7, 8, 8, 9]
target = 4

print(find_closest_ele(nums, target))