"""
Given a string of lowercase alphabets, count all possible substrings (not necessarily distinct) that has exactly k distinct characters.
Examples:

Input: abc, k = 2
Output: 2
Possible substrings are {"ab", "bc"}

Input: aba, k = 2
Output: 3
Possible substrings are {"ab", "ba", "aba"}

Input: aa, k = 1
Output: 3
Possible substrings are {"a", "a", "aa"}

思路：
- 需要记住目前的substring有哪些字母： set
- 目前的substring 长度. Len(set) O(1)
- 需要记住目前已有的results set()

move forward:
- 两个指针： i, j
- 如果发现已有重复的：1)set.remove(string[i]) 2)move i+=1 until string[i] not in current substring
- 发现len(set) == k: add string[i:j+1] into results if substring not in results_set
- len(set) < k: j +=1:
  - 如果发现已有重复的：1)set.remove(string[i]) 2)move i+=1 until string[i] not in current substring

"""

def substring_with_length_k(string, k):
  """
  input string: string
  input k: int

  output results: list of string [string]
  or output int: len(results)
  """
  if not string or not k:
    return []

  substring = set()
  results = set()

  for index in range(k-1):
    substring.add(string[index])
    print(substring)

  i = 0
  j = k-1

  while j < len(string):
    print("i{}, j{}".format(i, j))
    if string[j] not in substring:
      substring.add(string[j])
      if len(substring) == k:
        word = string[i:j+1]
        print("word", word)
        if word not in results:
          results.add(word)
          print("add", results)
        substring.remove(string[i])
        i += 1
      j += 1
    else: # if string[j] is already in substring
      substring.remove(string[i])
      i += 1
  return list(results)
  # return len(results)

####### test case 1###########
# string = "apeapele"
# # ape, pea, eap, pel
# k = 3
# print(substring_with_length_k(string, k))

######## more test cases ########

# print(substring_with_length_k("", 2))
# print(substring_with_length_k("abc", 2))
# print(substring_with_length_k("aba", 2))
print(substring_with_length_k("aa", 1))
