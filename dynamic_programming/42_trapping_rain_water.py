"""
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""



class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int

        **Thought:

        Q: which bound matter?
        - only the lower of (left_bound, right_bound) matter to how much water trap at a piont
        - so, you have two pointers: i, j, keep track of left-bound and right bound respectively.
        - move i or j whichever one is the lower bound. (i++, j--)

        Q: How much water trap:
        - water = max(0, lower_bound - height)
        - if height is higher than lower_bound, no water trap

        Q: When do you update the amount of water trap:
        - you update the amoutn of water trap at height[i] when you pointer is that that place.
        - so, after you update the water trap at height[i], you move the pointer forward or backward depend on which point you move (i++, j--)

        Q: When do you stop update:
        - Since you only update the water at a place when you about the move that pointer forward or backward,
        - so you update until i surpass j. (water at height[i] is only updated when a pointer i or j surpass it, NOT when the pointer is at it.)

        Q: Time comlexity:
        - O(N) b/c you only go through the list once.

        """
        i = 0
        j = len(height) - 1
        left_bound = 0
        right_bound = 0
        total = 0
        while i < len(height) and j > 0 and i <= j:
            #print("i", i, "j", j)
            if height[i] <= height[j]:
                # the amount of the water can hold: lower_bound - height
                total += max(0, left_bound - height[i])
                # update the bound
                left_bound = max(left_bound, height[i])
                # move pointer
                i += 1
            elif height[i] > height[j]:
                total += max(0, right_bound - height[j])
                right_bound = max(right_bound, height[j])
                j -= 1
        return total


    def trap1(self, height):
        """
        :type height: List[int]
        :rtype: int
          time complexity: O(N) = (O(N) + O(N) + O(N))
        """
        left = [0] * len(height)
        right = [0] * len(height)
        total = 0
        for i in range(1, len(height)):
            left[i] = max(left[i-1], height[i-1])
        for j in range(len(height)-2, -1, -1):
            right[j] = max(right[j+1], height[j+1])
        for k in range(len(height)):
            lower_bound = min(left[k], right[k])
            water = max(0, lower_bound - height[k])
            total += water
        return total
