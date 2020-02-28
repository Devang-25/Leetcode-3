class Solution(object):

  def uniquePaths(self, m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    # m is number of rows
    # n is number of cols
    dp = [([0] * n) for i in range(m)]
    # print("initial dp", dp)

    # basecase:
    # last row:
    dp[-1] = [1] * n
    # last col:
    for row in range(m):
      dp[row][-1] = 1

    for row in range(m - 2, -1, -1):
      for col in range(n - 2, -1, -1):
        dp[row][col] = dp[row + 1][col] + dp[row][col + 1]

    return dp[0][0]


######## tests

m = 3
n = 2
result = Solution().uniquePaths(m, n)
print(m, n, result, "\n")

#####

m = 7
n = 3
result = Solution().uniquePaths(m, n)
print(m, n, result, "\n")

#####
