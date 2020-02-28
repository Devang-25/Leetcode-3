"""
question: given two numbers, num1 and num2, return the biggest number 
created from permutation the digit of num1 so the new number is bigger 
than num2. If no such number exist, return None.
"""

from collections import defaultdict
from collections import Counter


class Solution:

  def biggerNum(self, num1, num2):
    """
    input num1: int
    input num2: int
    return: num

    num1 = 23888
    numDict = { 8: 3, 3: 1, 2: 1 }

    sortedKeys = [8, 3, 2]
    88832
    """
    if num1 == num2 or len(str(num2)) > len(str(num1)):
      return

    num1_dict = Counter(str(num1))
    num1_keys = sorted(num1_dict.keys(), reverse=True)

    new_num = self.newNum(num1_dict, num1_keys)
    return new_num if new_num > num2 else None

  def newNum(self, num1_dict, num1_keys):
    new_num = ""

    i = 0
    while i < len(num1_keys):
      key = num1_keys[i]
      new_num += key * num1_dict[key]
      i += 1
    return int(new_num)


####### test case ####

s = Solution()

num1 = 1
num2 = 42
result = s.biggerNum(num1, num2)
print("num1:{}, num2:{}, result:{}".format(num1, num2, result))

num1 = 0
num2 = 0
result = s.biggerNum(num1, num2)
print("num1:{}, num2:{}, result:{}".format(num1, num2, result))

num1 = 2
num2 = 3
result = s.biggerNum(num1, num2)
print("num1:{}, num2:{}, result:{}".format(num1, num2, result))

num1 = 3
num2 = 2
# r = s.newNum(3)
result = s.biggerNum(num1, num2)
print("num1:{}, num2:{}, result:{}".format(num1, num2, result))

num1 = 13
num2 = 15
result = s.biggerNum(num1, num2)
print("num1:{}, num2:{}, result:{}".format(num1, num2, result))

num1 = 15
num2 = 17
result = s.biggerNum(num1, num2)
print("num1:{}, num2:{}, result:{}".format(num1, num2, result))

######### more iterative solution #######
"""
question: given two numbers, num1 and num2, return the biggest number 
created from permutation the digit of num1 so the new number is bigger 
than num2. If no such number exist, return None.
"""

from collections import defaultdict


class Solution:

  def biggerNum(self, num1, num2):
    """
    input num1: num
    input num2: num
    return: num

    num1 = 23888
    numDict = { 8: 3, 3: 1, 2: 1 }

    sortedKeys = [8, 3, 2]
    88832
    """
    if num1 == num2:
      return

    if len(str(num2)) > len(str(num1)):
      return

    num1_str = str(num1)
    num1_dict = defaultdict(int)
    num1_max_digit = float("-inf")  # float
    num1_min_digit = float("inf")

    i = 0
    while i < len(num1_str):
      # eg: {1: 2, 3: 4}
      n1 = int(num1_str[i])
      num1_dict[n1] += 1
      if n1 > num1_max_digit:
        num1_max_digit = n1
      if n1 < num1_min_digit:
        num1_min_digit = n1
      i += 1

    # print("num1 dict", num1_dict, num1_max_digit, num1_min_digit)

    num2_str = str(num2)
    # print("num2_str first digit", num2_str[0], "max1_num_digit", num1_max_digit)
    # assert int(num2_str[0]) > num1_max_digit
    if int(num2_str[0]) > num1_max_digit:
      return

    # return new_num that is the biggest among the permutation of num1 digits
    # new_num: int or float
    new_num = self.newNum(num1_dict, num1_max_digit, num1_min_digit)
    return new_num if new_num > num2 else None

  def newNum(self, num1_dict, num1_max_digit, num1_min_digit):
    """
    input num1_dict: {int: int}
    input num1_max_digit: int
    input num1_min_digit: int

    return: int
    """
    print("num1_dict, num1_max_digit, num1_min_digit", num1_dict,
          num1_max_digit, num1_min_digit)
    new_num = ""

    while num1_dict:
      while num1_dict[num1_max_digit] > 0:
        new_num += str(num1_max_digit)
        num1_dict[num1_max_digit] -= 1
        if num1_dict[num1_max_digit] == 0:
          del num1_dict[num1_max_digit]
          print("max_digit is 0", num1_dict)
          break
      if not num1_dict:
        print("break")
        break
      while num1_max_digit not in num1_dict:
        num1_max_digit -= 1

    return int(new_num)


####### test case ####

s = Solution()

# num1 = 1
# num2 = 42
# result = s.biggerNum(num1, num2)
# print("num1:{}, num2:{}, result:{}".format(num1, num2, result))

# num1 = 0
# num2 = 0
# result = s.biggerNum(num1, num2)
# print("num1:{}, num2:{}, result:{}".format(num1, num2, result))

# num1 = 2
# num2 = 3
# result = s.biggerNum(num1, num2)
# print("num1:{}, num2:{}, result:{}".format(num1, num2, result))

# num1 = 3
# num2 = 2
# # r = s.newNum(3)
# result = s.biggerNum(num1, num2)
# print("num1:{}, num2:{}, result:{}".format(num1, num2, result))

num1 = 13
num2 = 15
result = s.biggerNum(num1, num2)
print("num1:{}, num2:{}, result:{}".format(num1, num2, result))

num1 = 15
num2 = 17
result = s.biggerNum(num1, num2)
print("num1:{}, num2:{}, result:{}".format(num1, num2, result))