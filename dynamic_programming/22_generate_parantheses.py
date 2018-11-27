class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return[]

        dp = {1: {"()"},
        2: {"()()", "(())"},
        }

        if n >= 3:
            for i in range(3, n+1):
#                 print(["(" + w + ")" for w in dp[i-1]])
                dp[i] = set(["(" + w + ")" for w in dp[i-1]])
                for j in range(1, i):
                    new = [l + r for l in dp[j] for r in dp[i-j]]
                    dp[i] = dp[i].union(new) # Note: union does not update in place
#                     print(dp)

        return list(dp[n])

==============

class Solution(object):
    def generateParenthesis_2(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        def dfs(n, string, left, right, result):
            # if all right bracket used up
            if right == n:
                result.append(string)

            # if left bracket still available
            if left < n:
                dfs(n, string + "(", left + 1, right, result)

            # if right bracket still available
            if right < left:
                dfs(n, string + ")", left, right + 1, result)

        dfs(n, "", 0, 0, result)
        return result

############Test Case####################
# print(Solution().generateParenthesis(0))
# print(Solution().generateParenthesis(1))
# print(Solution().generateParenthesis(2))
# print(Solution().generateParenthesis(3))
print(Solution().generateParenthesis(4))


"""
two base cases:
if n = 1, result = ['()']
if n = 2, result = ['(())', '()()']

if n = 3, result = [
"((()))", # pattern: result of dp[2] is around by an outer '()'
"(()())", # the same pattern as above
"(())()", # pattern: result of dp[2] + result of dp[1]
"()(())", # the same pattern as above with another permutation order: dp[1] + dp[2]
"()()()" # the same pattern as above
]

we can found the same recursive patterns for n > 3:
pattern 1: candidates = '(' + x + ')' , where x is element of dp[n-1]
pattern 2: candidates = [x + y] , where x is element of dp[i] and y is element of dp[n-i] (the range of i is [0 : n])
"""
