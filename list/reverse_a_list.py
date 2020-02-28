"""
question: reverse a string
"""


def reverseString(word):
  """
  input word: str
  output result: str
  """
  s = 0
  e = len(word) - 1
  result = [""] * len(word)

  while s < e:
    result[s], result[e] = word[e], word[s]
    s += 1
    e -= 1

  return "".join(result)


####### test cases #######
word = ""
result = reverseString(word)
print("result", result)

word = "abc"
result = reverseString(word)
print("result", result)

word = "abcd"
result = reverseString(word)
print("result", result)

word = "a"
result = reverseString(word)
print("result", result)

######## modify in place, input is a list ##########


def reverseString2(word):
  """
  input word: list
  output result: str
  """
  s = 0
  e = len(word) - 1

  while s < e:
    word[s], word[e] = word[e], word[s]
    s += 1
    e -= 1

  return "".join(word)


####### test cases #######
word = []
result = reverseString2(word)
print("result", result)

word = ["a", "b", "c"]
result = reverseString2(word)
print("result", result)

word = ["a", "b", "c", "d"]
result = reverseString2(word)
print("result", result)

word = ["a"]
result = reverseString2(word)
print("result", result)