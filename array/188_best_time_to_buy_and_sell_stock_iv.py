class Solution(object):

  def maxProfit(self, k, prices):
    """
    :type k: int
    :type prices: List[int]
    :rtype: int
    """
    n = len(prices)
    t = [([0] * n) for _ in range(n)]

    for s in range(n):
      min_price = prices[s]
      max_profit = 0
      for c in range(s, n):
        min_price = min(min_price, prices[c])
        max_profit = max(max_profit, prices[c] - min_price)
        t[s][c] = max_profit
    print(t)

    a = [([0] * n) for _ in range(k)]

    a[0] = t[0]
    for kk in range(1, k):
      for i in range(n):
        a[kk][i] = a[kk - 1][i]
        for j in range(i):
          cur = max(a[kk - 1][j] + t[j + 1][i])
          a[kk][i] = max(a[kk][i], cur)

    return max(a[k - 1])


k = 1
prices = [3, 1, 2, 7, 5]
s = Solution()
s.maxProfit(k, prices)
