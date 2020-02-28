"""
time complexity:
since we runs twice binary search: so is 2 * O(logN), so it is still O(LogN)

space complexity: O(1)

Note:
if we use while l < r:
  when only has two nums with index [0, 1], 
  then we will never get out of the loop.
  b/c mid = (0 + 1) // 2 = 0
  left = 0

"""


class Solution(object):

  def searchRange(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    if not nums:
      return [-1, -1]

    l = 0
    r = len(nums) - 1

    # find first psotion of element
    while l < (r - 1):
      mid = (l + r) // 2
      if nums[mid] == target:
        r = mid
      elif nums[mid] < target:
        l = mid + 1
      elif nums[mid] > target:
        r = mid - 1

    if nums[l] == target:
      first = l
      print("first left", first)
    elif nums[r] == target:
      first = r
      print("first right", first)
    else:
      return [-1, -1]

    # find the last position of element
    l = 0
    r = len(nums) - 1

    while l < (r - 1):
      print("l", l, end=" ")
      print("r", r, end=" ")
      mid = (l + r) // 2
      print("mid", mid)
      if nums[mid] == target:
        l = mid
      elif nums[mid] < target:
        l = mid + 1
      elif nums[mid] > target:
        r = mid - 1

    if nums[r] == target:
      return [first, r]
    elif nums[l] == target:
      return [first, l]
    else:
      return [first, first]


nums = [1]
target = 1

nums = [1, 1]
target = 1

# nums = [1, 2, 3, 3, 4]
# target = 3

s = Solution()
print(s.searchRange(nums, target))