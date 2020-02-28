"""
647. Palindromic Substrings
Medium

1248

65

Favorite

Share
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
 

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

"""


class Solution(object):

  def countSubstrings(self, s):
    """
    :type s: str
    :rtype: int
    """
    # self.matrix = [[None] * len(s) for _ in range(len(s))]
    self.results = []

    for i in range(len(s)):
      self.if_palindrome(i, i, s)
      self.if_palindrome(i, i + 1, s)

    return len(self.results)

  def if_palindrome(self, b, e, s):
    while b >= 0 and e < len(s):
      if s[b] == s[e]:
        self.results.append(s[b:e + 1])
        b -= 1
        e += 1
      else:
        break


string = "aa"
s = Solution()
r = s.countSubstrings(string)
print("string:{}, r:{}".format(string, r))

string = ""
s = Solution()
r = s.countSubstrings(string)
print("string:{}, r:{}".format(string, r))

string = "aaa"
s = Solution()
r = s.countSubstrings(string)
print("string:{}, r:{}".format(string, r))

string = "ab"
s = Solution()
r = s.countSubstrings(string)
print("string:{}, r:{}".format(string, r))

string = "aba"
s = Solution()
r = s.countSubstrings(string)
print("string:{}, r:{}".format(string, r))
