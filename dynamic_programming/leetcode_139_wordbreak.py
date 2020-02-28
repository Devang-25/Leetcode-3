"""

https://leetcode.com/problems/word-break/

Leetcode 139 解题思路：
Word break: 

s: s0, s1, s2..., sn-1

subproblem: 从这里开始的字母可否在wordict里面搭配到

dp[0]: 取决于s[0:i] + dp[i:]
dp[1]: 取决于从s[1:i] + dp[i:]
dp[2]: 取决于从s[2:i] + dp[i:]
....
dp[n-1]:s[n-1]是否能在worddict里面搭配到。



l e e t c o d e
01 23 45 6 7

dp[7] = s[7] = e = No

dp[6]: s[6:i] for i in range(6+1, n):
	   s[6:7] = d.= NO
	   s[6:8] = de=No
	   N0 + no = N0

dp[5] = s[5:i]+ dp[i] for i in range(5+1, n):
             s[5:6] = o = No
	     s[5:7] = od = No
             S[5:8] = ode= No

dp[4] = s[4:i] + dp[i:] for i in range(4+1, n):
s[4:5] = c = no
s[4:6] = 
...
s[4:8] = code = Yes
No + no + no + yes = Yes for dp[4]

dp[3] = s[3:i] + dp[i] for i in range(3+1, n)
s[3:4] = t = no = dp[4:] = yes ==> No
....
s[3:8] = no
No

dp[2] = s[2:i] + dp[i] for i in range(2+1, n)
s[2:3] = no
....
No

dp[0] = s[0:i] for dp[i] for i in range(0+1, n) s[0] = no
...
s[0:4] = leet = Yes + dp[4:] = yes ==> YES

========


Time complexity: 
# of subproblem: len(s) = n

For each subproblem: 
N-i, where I is i-th letter I am up to in string

So, total time complexity is O(n^2)
"""

class Solution(object):
  def wordBreak(self, s, wordDict):



    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    n = len(s)
    dp = [0] * (n + 1)

    # # base case: dp[last] = 1
    dp[-1] = 1

    for start in range(n - 1, -1, -1):
      for i in range(start + 1, n + 1):
        if s[start:i] in wordDict and dp[i] == 1:
          dp[start] = 1
          break
    print("dp")
    for i in range(len(dp)):
      print(i, dp[i])
    return dp[0]


################### tests ###############
s = "leetcode"
wordDict = {"leet", "code"}

solution = Solution().wordBreak(s, wordDict)
print(solution)

################
print("\n")

s = "applepenapple"
wordDict = {"apple", "pen"}

solution = Solution().wordBreak(s, wordDict)
print(solution)
