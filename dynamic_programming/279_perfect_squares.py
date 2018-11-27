"""
279. Perfect Squares
Medium
972
79


Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

"""

class Solution(object):
    _dp = [0]
    def numSquares(self, n):
        dp = self._dp
        if len(dp) <= n:
            squares = [i*i for i in range(1, int(n**0.5 + 1)) if i*i <= n]
            for i in range(len(dp), n+1):
                choices = [s for s in squares if s <= i]
                dp.append(1 + min(dp[i-s] for s in choices))
        return(dp[n])
