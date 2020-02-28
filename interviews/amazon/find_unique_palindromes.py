class Solution(object):

  def countSubstrings(self, s):
    """
    :type s: str
    :rtype: int
    """
    # self.matrix = [[None] * len(s) for _ in range(len(s))]
    self.results = set()

    for i in range(len(s)):
      self.if_palindrome(i, i, s)
      self.if_palindrome(i, i + 1, s)

    return len(self.results)

  def if_palindrome(self, b, e, s):
    while b >= 0 and e < len(s):
      if s[b] == s[e]:
        self.results.add(s[b:e + 1])
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
