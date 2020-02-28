"""
### Missing Number:

leetcode268 Missing Number

Easy

Given an array containing *n* distinct numbers taken from `0, 1, 2, ..., n`, find the one that is missing from the array.

**Example 1:**

```
Input: [3,0,1]
Output: 2
```

**Example 2:**

````
Input: [9,6,4,2,3,5,7,0,1]
Output: 8
```

**Solution:**

From elementary school math, we have a popular math trick which is the sum of 1+2+...+n = n*(n+1)/2, it can be used here. Since we are finding the missing number, just get the sum of all the n number first using the formula, and the minus it to the sum of all the numbers in the array, we get the missing number.

"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        real_total = n*(n+1)/2
        return real_total - sum(nums)
