"""
53. Maximum Subarray
DescriptionHintsSubmissionsDiscussSolution
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        type nums: List[int]
        rtype: int
        """
        max_sum = temp_sum = nums[0]
        for num in nums:
            # print(num, "\n", "prev sum", temp_sum)
            temp_sum = max(temp_sum + num, num)
            max_sum = max(max_sum, temp_sum)
            # print("new sum", temp_sum)
            # if temp_sum > max_sum:
                # max_sum = temp_sum
        return max_sum

test1 = [-2,1,-3,4,-1,2,1,-5,4] # 6

print(Solution().maxSubArray(test1))
