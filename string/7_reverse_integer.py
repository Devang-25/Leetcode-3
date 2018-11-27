"""
7. Reverse Integer
Easy
1710
2411


Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21

"""

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = list(reversed((str(x))))
        if x < 0:
            y = [y[-1]] + y[:-1]
        # print(y)
        z = "".join(y)
        # print(z, type(z))
        if ((-2)**31 <= int(z) <= (2 ** 31 - 1)):
            z = "".join(y)
            return(int(z))
        else:
            return(0)

Solution().reverse(123)
