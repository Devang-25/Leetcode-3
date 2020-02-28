class Solution(object):

  def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if not prices:
      return 0

    max_profit = 0
    min_price = prices[0]

    dp = [0] * len(prices)

    for i in range(1, len(prices)):
      if prices[i] > min_price:
        dp[i] = prices[i] - min_price
        if dp[i] > max_profit:
          max_profit = dp[i]
      elif prices[i] < min_price:
        min_price = prices[i]
    return max_profit


########### solution with Space O(1) and time complexity O(N)#####
class Solution(object):

  def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if not prices:
      return 0

    max_profit = 0
    min_price = prices[0]

    # dp = [0] * len(prices)

    for i in range(1, len(prices)):
      if prices[i] - min_price > max_profit:
        max_profit = prices[i] - min_price
      elif prices[i] < min_price:
        min_price = prices[i]
    return max_profit


prices = [7, 1, 5, 3, 6, 4]
result = Solution().maxProfit(prices)
print(result, "\n")
# result = 6

prices = [7, 6, 4, 3, 1]
result = Solution().maxProfit(prices)
print(result, "\n")
# result = 0
