class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        length = [1] * len(nums)
        for i in range(1, len(nums)):
            # for j from 0 to (i-1)
            for j in range(i):
                if nums[i] > nums[j]:
                    length[i] = max(length[i], length[j]+1)
        return max(length)

    def lengthOfLIS_2(self, nums):
    # minend[i] is the minimum ending of an increasing subsequence of length i+1
        minend = [float('inf')] * (len(nums) + 1)
        for num in nums:
            minend[bisect.bisect_left(minend, num)] = num
        return minend.index(float('inf'))

nums1 = [10,9,2,5,3,7,101,18] #[2,3,7,101],length=4
