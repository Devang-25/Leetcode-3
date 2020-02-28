"""
closest two sum < target

https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=478916

"""


from collections import defaultdict

########## return only 1 pair of results ##########
def closest_sum(nums, target):

  nums.sort() # O(NlogN)

  l = 0
  r = len(nums) - 1
  closest_sum = "None"
  closest_pair = []

  while l < r:
    cur = nums[l] + nums[r]
    if cur == target:
      return(nums[l], nums[r])
    elif cur < target:
      if closest_sum == "None" or (target - cur < target - closest_sum):
        closest_sum = cur
        closest_pair = [nums[l], nums[r]]
      l += 1
    elif cur > target:
      r -= 1
  return closest_pair


nums = [2, 0, 6, -3, -6, 8, 10, 4]
target = 11

nums = [2, 1, 6, -3, -6, 8, 10, 4]
target = 11


print(closest_sum(nums, target))

########## return all pair of results ##########


from collections import defaultdict

def closest_sum_all_pairs(nums, target):

  nums.sort() # O(NlogN)
  # print("nums", nums)

  l = 0
  r = len(nums) - 1
  closest_sum = "None"
  closest_pairs = []

  """
  # if not any closest sum OR
  # if the current diff < previous diff:
    # target - cur < target - closest_sum
  # then update
  """
  while l < r:
    # print("l,r", nums[l], nums[r])
    cur = nums[l] + nums[r]
    if cur <= target:
      if closest_sum == "None" or (target - cur < target - closest_sum):
        closest_sum = cur
        closest_pairs = [[nums[l], nums[r]]]
      # if same, then append
      elif target - cur == target - closest_sum:
        closest_pairs.append([nums[l], nums[r]])
    if cur == target:
      l += 1
      r -= 1
    elif cur < target:
      l += 1
    elif cur > target:
      r -= 1
  return closest_pairs


# nums = [2, 0, 6, -3, -6, 8, 10, 4]
# target = 11

nums = [2, 1, 6, -3, -6, 8, 10, 4]
target = -6


print(closest_sum_all_pairs(nums, target))
