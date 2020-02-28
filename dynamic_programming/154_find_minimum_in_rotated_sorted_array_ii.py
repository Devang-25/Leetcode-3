"""
154. Find Minimum in Rotated Sorted Array II
Hard

451

142

Favorite

Share
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:

Input: [1,3,5]
Output: 1
Example 2:

Input: [2,2,2,0,1]
Output: 0

题目思路：
- find the minimum in rotated sorted array
- 难点：里面有重复的数字。因此你不知道去哪个半边继续查找。





"""


class Solution(object):

  def findMin(self, nums):
    """
        :type nums: List[int]
        :rtype: int
        """
    l = 0
    r = len(nums) - 1
    while l <= r:
      mid = (l + r) / 2
      if nums[mid] > nums[r]:
        l = mid + 1
      elif nums[l] > nums[mid]:
        r = mid
      else:
        r -= 1
    return nums[mid]
