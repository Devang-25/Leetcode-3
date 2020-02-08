from typing import List
"""
Input: dividend = 20, divisor = 3
Output: 6


i) bit, total = divisor << bit, compare, remainder
0) 0,   3 = 3 << 0,             small,   20
1) 1,   6 = 3 << 1,             small,   14
2) 2,   12 = 3 << 2,            smaller, 8 ---- STOP HERE: add count (1 << 2 = 4) toward result 
3) 3,   24 = 3 << 3,            bigger, -4


Thought:
# First starting from bit i = 0, see if dividend >= (divisor << bit 0). If not, i += 1. 
# Do this until dividend is not longer bigger or equal to (divisor << bit_i).
# Then update dividend by subtracting divisor from it: dividend -= divisor. 
# The repeat from step 1 again until the new dividend is smaller than 

Time Complexity: O(log(dividend/divisor))
calculation of time complexity
3*(2^i)=20
log_2(20/3)
log_2(dividend/divisor)

"""

class Solution:
  def divide(self, dividend: int, divisor: int) -> int:
    sign = (dividend > 0) is (divisor > 0)
    dividend = abs(dividend)
    divisor = abs(divisor)

    # print("sign", sign, "dividend", dividend, "divisor", divisor)

    result = 0
    
    while dividend >= divisor:
      i = self.find_stop_count(dividend, divisor)
      result += (1 << i)
      dividend -= (divisor << i)
    # return result if sign else -result
    return min(result if sign else -result, 2147483647)

  def find_stop_count(self, dividend:int, divisor:int) -> int:
    i = 0
    while dividend >= divisor << (i+1):
      i += 1
    
    return i


dividend = 20
divisor = 3

dividend = 0
divisor = 3

dividend = -20
divisor = 3

dividend = -2147483648
divisor = -1

s = Solution()
result = s.divide(dividend, divisor)
print("result:", result)
