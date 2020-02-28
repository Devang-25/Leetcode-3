""""


81. Search in Rotated Sorted Array II
Medium

672

314

Favorite

Share
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false


思路总结：
- 目标：是在一个sorted, rotated array里找target number

解法：
- 那么array里可能出现两种情况：1）一半是从小到大（按顺序）2）另外一半：不是按顺，数字的顺序是大小大



"""


class Solution:

  def search(self, nums, target):
    """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
    l = 0
    r = len(nums) - 1
    print("e", r)
    while l <= r:
      mid = (l + r) // 2
      if target == nums[mid]:
        return True
      # if left is the ascending half
      elif nums[l] < nums[mid]:
        if nums[l] <= target < nums[mid]:
          r = mid - 1
        else:
          l = mid + 1
      # right right is the ascending half:
      elif nums[l] > nums[mid]:
        if nums[mid] < target <= nums[r]:
          l = mid + 1
        # elif nums[l] == target:
        #   return True
        else:
          r = mid - 1
      else:
        l += 1
    return False
