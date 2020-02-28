"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.

Success
Details 
Runtime: 668 ms, faster than 93.48% of Python online submissions for Coin Change.
Memory Usage: 12 MB, less than 60.00% of Python online submissions for Coin Change.

Time complexity:
O(N*len(coin))

Space Complexity:
O(N)

where N = amount.

"""


class Solution(object):

  def coinChange(self, coins, amount):
    """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
    states = [float("inf")] * (amount + 1)

    states[0] = 0

    for i in range(1, amount + 1):
      choices = [states[i - coin] for coin in coins if coin <= i]
      if choices:
        states[i] = 1 + min(choices)

    return states[amount] if states[amount] != float("inf") else -1
