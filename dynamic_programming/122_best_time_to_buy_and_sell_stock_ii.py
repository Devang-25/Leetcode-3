"""
approach: assume you buy in a previous day and sell on the next day for every day

time complexity: O(N)
space complexity: O(N)


"""


class Solution(object):

  def maxProfit(self, prices):
    """
        :type prices: List[int]
        :rtype: int
        """
    return sum(
        [max(prices[i] - prices[i - 1], 0) for i in range(1, len(prices))])


###########################
"""
time complexity: O(N^2)
space complexity: O(N)
N = len(prices)

method: dynamic programming
subproblem: what is the max profit you can gain if you sell or don't hold any stock at i-th prices? 

dp[i] = what is the max profit you can gain if you sell or don't hold any stock at i-th prices? 
dp[i] = max(prices[i] - prices[j], 0) + dp[j-1] for j in range(0, i+1)
"""


class Solution(object):

  def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    dp = [0] * len(prices)

    for i in range(1, len(prices)):
      dp[i] = max(
          max(prices[i] - prices[j], 0) + dp[j - 1] for j in range(0, i + 1))

    return dp[-1]


######### test ###########
prices = [7, 1, 5, 3, 6, 4]

result = Solution().maxProfit(prices)
print(result, "\n")
# return 7

##############
prices = [1, 2, 3, 4, 5]

result = Solution().maxProfit(prices)
print(result, "\n")
# return 4

#############
##############
prices = [7, 6, 4, 3, 1]

result = Solution().maxProfit(prices)
print(result, "\n")
# return 0