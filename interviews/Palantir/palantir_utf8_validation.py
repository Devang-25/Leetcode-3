"""
393. UTF-8 Validation
Medium

127

595

Favorite

Share
A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:

For 1-byte character, the first bit is a 0, followed by its unicode code.
For n-bytes character, the first n-bits are all one's, the n+1 bit is 0, followed by n-1 bytes with most significant 2 bits being 10.
This is how the UTF-8 encoding would work:

   Char. number range  |        UTF-8 octet sequence
      (hexadecimal)    |              (binary)
   --------------------+---------------------------------------------
   0000 0000-0000 007F | 0xxxxxxx
   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
Given an array of integers representing the data, return whether it is a valid utf-8 encoding.

Note:
The input is an array of integers. Only the least significant 8 bits of each integer is used to store the data. This means each integer represents only 1 byte of data.

Example 1:

data = [197, 130, 1], which represents the octet sequence: 11000101 10000010 00000001.

Return true.
It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.
Example 2:

data = [235, 140, 4], which represented the octet sequence: 11101011 10001100 00000100.

Return false.
The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
The next byte is a continuation byte which starts with 10 and that's correct.
But the second continuation byte does not start with 10, so it is invalid.


Conclusion
SO requirements:
1. A character in UTF8 can be from 1 to 4 bytes long
2. For 1-byte character, the first bit is a 0, followed by its unicode code.
3. For n-bytes character, the first n-bits are all one's, the n+1 bit is 0, followed by n-1 bytes with most significant 2 bits being 10.

"""

from typing import List


class Solution:

  def validUtf8(self, data: List[int]) -> bool:
    result = []
    for num in data:
      r = "{:08b}".format(num)
      result.append(r)
    print("result", result)
    return self.check_valid(result)

  def check_valid(self, result):
    """
    inputs:
        result: List[str]
    
    outputs:
        bool
    """
    l = len(result)

    i = 0

    while i < l:
      print("i:{}:{}".format(i, result[i]))
      if result[i][0] == "0":
        i += 1

      elif result[i][0] == "1" and result[i][1] == "0":
        return False

      elif result[i][0] == "1" and result[i][1] == "1":
        n_bytes = 2
        j = 2
        while j < 8 and result[i][j] == "1":
          n_bytes += 1
          print("j:{}, n_byte: {}".format(j, n_bytes))
          j += 1
        # from i+1 to i+n_bytes should start with 10
        # eg. 3bytes: #0: 1110..., 10xxx, 10xxx,
        if n_bytes > 4:
          return False
        for ii in range(i + 1, i + n_bytes):
          if ii >= l:
            return False
          print("ii:{}".format(ii))
          if result[ii][0] != "1" or result[ii][1] != "0":
            return False
        i += n_bytes

    return True


# data = [197, 130, 1]
# s = Solution()
# # print(s.validUtf8(data))
# s.validUtf8(data) == True

#######

# data = [235, 140, 4]
# s = Solution()
# r = s.validUtf8(data)
# assert r == False
# print(r)

# data = [255]
# s = Solution()
# r = s.validUtf8(data)
# assert r == False
# print(r)

#########

data = [250, 145, 145, 145, 145]
s = Solution()
r = s.validUtf8(data)
assert r == False
print(r)

data = [240, 162, 138, 147, 17]
s = Solution()
r = s.validUtf8(data)
assert r == True
print(r)
