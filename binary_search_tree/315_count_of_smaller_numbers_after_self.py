'''
Problem:

You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
'''

'''
Thought:

The smaller numbers on the right of a number are exactly those that jump from its right to its left during a stable sort. So I do mergesort with added tracking of those right-to-left jumps.

# Since, going in the reversed range order of len(enums)
# so, if left number is bigger => left side is bigger
# => numbers in the right side are smaller than this left nm
# => smaller[position index of that number] = len(right)
# => enum[i] = that left num, left.pop()
# since you need to return the enum as a sorted list
# for the upper scope

# else:
# if the right num > left num:
# this means this right number is:
# 1) is bigger than left num
# 2) at the right side of this left num
# (since we only interest in nums that at the right side
# of a number & SMALLER,
# so, NO NEED to update smaller[] list
# just right.pop()

# Except for the last num,
# every num has been once on the left side,
# so every num, except for the last num,
# already has a chance to update SMALLER nums at its RIGHT side

'''

class Solution(object):
    def countSmaller_1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # build the counting
        counts = [0] * len(nums)

        # if 1 number => return
        # if more than 1 nubmer => split
        def mergesort(pairs):
            if len(pairs) < 2:
                return pairs

            mid = len(pairs) // 2
            left = mergesort(pairs[:mid])
            right = mergesort(pairs[mid:])

            # sort
            # if right is smaller => append right, j++
            # if left is smaller => append left, update count, i++
            # if left = right, (only care about smaller) => append left, update count, i ++
            # if no i, only j, append right

            i = j = 0
            results = []
            while i < len(left) or j < len(right):
                # print("i:{}, j:{}".format(i, j))
                if i >= len(left) or (j < len(right) and right[j][1] < left[i][1]):
                    results.append(right[j])
                    j += 1
                else:
                    results.append(left[i])
                    counts[left[i][0]] += j
                    i += 1
            return results

        mergesort(list(enumerate(nums)))
        return counts

    def countSmaller_2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def mergeSort(enum):
            half = len(enum) / 2
            if half:
                left, right = mergeSort(enum[: half]), mergeSort(enum[half :])
                for i in range(len(enum))[::-1]:
                        if not right or left and left[-1][1] > right[-1][1]:
                            smaller[left[-1][0]] += len(right)
                            enum[i] = left.pop()
                        else:
                            enum[i] = right.pop()
            return enum

        smaller = [0] * len(nums)
        mergeSort(list(enumerate(nums)))
        return smaller

nums1 = [5, 2, 6, 1]
sol = Solution()
sol.countSmaller_1(nums1)
sol.countSmaller_2(nums1)
