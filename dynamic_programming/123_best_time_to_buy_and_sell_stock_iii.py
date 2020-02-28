class Solution(object):

  def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if not prices:
      return 0

    n = len(prices)
    dp1 = [0] * n
    dp2 = [0] * n

    min_price = prices[0]
    for i in range(1, n):
      dp1[i] = max(dp1[0], prices[i] - min_price)
      if prices[i] < min_price:
        min_price = prices[i]

    max_price = prices[-1]
    for j in range(n - 2, -1, -1):
      dp2[j] = max(max_price - prices[j], dp2[j + 1])
      if prices[j] > max_price:
        max_price = prices[j]

    dp = [0] * n
    for k in range(n):
      dp[k] = dp1[k] + dp2[k]

    return max(dp)


############ test case ########
prices = [3, 3, 5, 0, 0, 3, 1, 4]
result = Solution().maxProfit(prices)
print(result, "\n")
# return 6

prices = [1, 2, 3, 4, 5]
result = Solution().maxProfit(prices)
print(result, "\n")
# return 4