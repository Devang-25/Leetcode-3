
"""
213. House Robber II
Medium
627
18


You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

"""

def robbery(houses):
  """
  input houses: list[int]
  output total: int
  """
  if len(houses) <= 3:
    return max(houses or [0])

  def dplist(new_houses):
    new_houses = [0] + new_houses
    dp = new_houses[0:3]


    total = 0
    for i in range(3, len(new_houses)):
      dp.append(new_houses[i] + max(dp[i-2], dp[i-3]))
      if dp[i] > total:
        total = dp[i]
    return total

  return(max(dplist(houses[1:]), dplist(houses[:len(houses)-1])))

houses = [1,3,1,3,100]
print(robbery(houses))
