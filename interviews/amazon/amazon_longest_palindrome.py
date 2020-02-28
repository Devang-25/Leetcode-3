"""
# longest Palindrome

思路：
- dynamic programming
index 1 , 2, 3....
1
2
3
.
.
.

for each substring from (s, e):
  - whether it's a palondrome depends on:
    - s == e and
    - whether (s+1, e-1) is a palindrome

data structure:
- a 2x2 table to record whether substring (s, e) a palindrome
- self.longest_len
- self.longest_palindrome

time complexity:
O(N^2)
"""



def dprint(*args, **kwargs):
  print(*args)
  print(**kwargs)

class LongestPalindrome:
  def __init__(self):
    self.longest_len = 0
    self.longest_palindrome = ""


  def find_longest_palindrome(self, string):
    """
    input string: str
    output type: str, the longest palindrome substring
    """
    if not string:
      return self.longest_palindrome

    ### if palindrome

    def check_string(s, e):
      """
      input s: int, the start index
      input e: int, the end index

      output bool: True / False
      """
      # corner / base case
      if s == e or s > e:
        return True

      elif string[s] != string[e]:
        return False

      elif string[s] == string[e]:
        if cache[s+1][e-1] == None: # no cache yet
          return check_string(s+1, e-1)
        else: # if has True / Fasle
          return cache[s+1][e-1]


    # database
    cache = [([None] * len(string)) for _ in range(len(string))]
    print("cache", cache)

    for i in range(len(string)):
      for j in range(i+1):
        print("index", i, j)
        cache[i][j] = check_string(i, j)
        if cache[i][j] and (j-i+1) > self.longest_len:
          self.longest_len = j - i + 1
          self.longest_palindrome = string[i : j+1]

    return self.longest_palindrome

string = "a"
s = LongestPalindrome()
print(s.find_longest_palindrome("a"))
