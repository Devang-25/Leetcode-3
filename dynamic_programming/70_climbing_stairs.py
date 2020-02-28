"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Solution:
for ways of climbing to nth step:
    = num of ways of [n-1] + num of ways of [n-2]

for step 1: 1
for step 2: 2
for step 3: 1 + 2 = 3
for step 4: 2 + 3 = 5
...

"""


class Solution(object):

  def climbStairs(self, n):
    """
        :type n: int
        :rtype: int
        """
    a = b = 1
    for _ in range(n):
      a, b = b, a + b
    return a


print(Solution().climbStairs(3))

#####################################
"""
12 ms	11.6 MB	python
"""


class Solution(object):

  def climbStairs(self, n):
    """
        :type n: int
        :rtype: int
        """
    states = [0] * (n + 1)
    states[1] = 1

    if n > 1:
      states[2] = 2

    if n > 2:
      for i in range(3, n + 1):
        states[i] = states[i - 1] + states[i - 2]
    return states[n]
