"""
解题思路：
- 打算用stack来存左边的parentheses. 
- 如果出现了右边的characters, 必须和stack最上面的parentheses配的上，并pop出来;
- 如果出现右边的characters, 但是配不上，那就fail.

Time complexity: O(N)
Space complexity: O(N)

"""


class Solution(object):

  def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    for c in s:
      if c == "(" or c == "{" or c == "[":
        stack.append(c)
      elif c == ")" or c == "}" or c == "]":
        if not stack:
          return False
        elif c == ")" and stack[-1] == "(":
          stack.pop()
        elif c == "}" and stack[-1] == "{":
          stack.pop()
        elif c == "]" and stack[-1] == "[":
          stack.pop()
        else:
          return False
    return True if not stack else False


s = ""
s = "([])"
s = "()[]{}"
s = "([)]"
s = "("
s = ")"

sol = Solution()
print(sol.isValid(s))
