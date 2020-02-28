class Solution(object):

  def minDistance(self, word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    # row would be word1
    # col would be word2
    n = len(word1)
    m = len(word2)
    dp = [([0] * (m + 1)) for i in range(n + 1)]
    print("dp", dp, len(dp), len(dp[0]))

    # base cases:
    dp[n][m] = 0
    # dp[n - 1][m - 1] = 0 if word1[-1] == word2[-1] else 1
    # dp[n][m - 1] = 1
    # dp[n - 1][m] = 1

    # handle the last row:
    for j in range(m - 1, -1, -1):
      dp[n][j] = 1 + dp[n][j + 1]

    for i in range(n - 1, -1, -1):
      dp[i][m] = 1 + dp[i + 1][m]

    for i in range(n - 1, -1, -1):
      for j in range(m - 1, -1, -1):
        # print("enter")
        # print("i", i, word1[i:], "j", j, word2[j:])
        insert_option = 1 + dp[i][j + 1]
        del_option = 1 + dp[i + 1][j]
        replace_option = 1 + dp[i + 1][j + 1]
        dp[i][j] = min(insert_option, del_option, replace_option)
        if word1[i] == word2[j]:
          # print("prev", dp[i][j], dp[i + 1][j + 1])
          # print("same", "i", i, word1[i], "j", j, word2[j])
          dp[i][j] = min(dp[i][j], dp[i + 1][j + 1])
        # print("dp[{}][{}]:{}".format(i, j, dp[i][j]))

    # for row in dp:
    #   print(row)

    return dp[0][0]


##### test #####
word1 = "horse"
word2 = "ros"
result = Solution().minDistance(word1, word2)
print(result, "\n")
# return 3

word1 = "intention"
word2 = "execution"
result = Solution().minDistance(word1, word2)
print(result, "\n")
# return 3