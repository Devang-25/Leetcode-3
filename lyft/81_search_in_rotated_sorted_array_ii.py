"""
81. Search in Rotated Sorted Array II
Medium
463
228
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

"""


"""
Since there is repetition of digit happens here,
so there might be cases where there is not sufficient information to choose which half to search.

Thus we divide into three scenario:
1. left half if ascending
2. rotating happen if the left half
(the alternative nums[r] >= nums[mid] ### MUST be equal to as well
### nums[r] > nums[mid] will not work
b/c
right side might be all same numbers, which is not ascending,
eg: [1, 3, 1, 1, 1])
3. information loss in cases [1, 3, 1, 1, 1]:
so increment left += 1 and search again.

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
        #print("e", r)
        while l <= r:
          mid = (l + r) // 2
          if target == nums[mid]:
            return True
          # if left is the aseceinding half
          elif nums[l] < nums[mid]:
            if nums[l] <= target < nums[mid]:
              r = mid - 1
            else:
              l = mid + 1
          # if the rotating happen on the left half:
          elif nums[l] > nums[mid]:
          # elif nums[r] >= nums[mid]:
            if nums[mid] < target <= nums[r]:
              l = mid + 1
            else:
              r = mid - 1
          # example for this case: [1, 3, 1, 1, 1]
          # else there is information loss:
          # l = mid -> not sure which half to check
          # increement l += 1 until there is new information
          else:
            l += 1
        return False


# nums = [3, 1, 1]
# target = 3

nums = [1,3,1,1,1]
target = 3
s = Solution().search(nums, target)
print(s)
