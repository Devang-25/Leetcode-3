"""
https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/maximum-chocolate-3/

Bharat is chocoholic. He found a chocolate factory of N floors ,but the factory has N*N rooms where in each room specific number of chocolate is present. Now, Bharat starts collecting chocolate from ground floor. He can only collect chocolate from one room in a floor. Bharat can only move to upper room or upper-right room or upper-left room .

He want to collect maximum number of chocolate possible. Help him in finding maximum number of chocolate.

Input:

First line contains a value of N. Next N lines contains N space separated integer.

Output:

Output a single integer denoting the maximum number of chocolate Bharat can collect.

Constraints

1 <= N <= 1000

1 <= Number chocolate in 1 room <= 10^5


###################
SOLUTION:

Algorithm: 
Dynamic Programming

Time Complexity: O(N*N) N = n given

So I only visit each room once. 
At each room, I only record the max amount of chocolate I can collect if I have to include this room.


"""


class Solution:

  def get_max_chocolate(self, n, chocolates_matrix):
    self.n = n
    self.chocolates_matrix = chocolates_matrix
    self.max_chocolates = 0
    self.best_route = []

    # # for get_chocolate():
    # for i in range(n):
    #   cur_chocolates = self.chocolates_matrix[0][i]
    #   self.get_chocolate((0, i), cur_chocolates, [(0, i)])

    # return self.max_chocolates, self.best_route

    self.get_chocolate_max_up_to_a_room(0, chocolates_matrix[0])
    return self.max_chocolates

  # def get_chocolate(self, cur_pos, cur_chocolates, route):
  #   level, col = cur_pos
  #   print("cur_pos:{}/{}, cur_chocolates:{}, route:{}".format(
  #       cur_pos, self.chocolates_matrix[level][col], cur_chocolates, route))

  #   if level == self.n - 1:
  #     if cur_chocolates > self.max_chocolates:
  #       self.max_chocolates = cur_chocolates
  #       self.best_route = route
  #     return

  #   next_positions = [[level + 1, col - 1], [level + 1, col],
  #                     [level + 1, col + 1]]

  #   for pos in next_positions:
  #     l, c = pos
  #     if 0 <= l < self.n and 0 <= c < self.n:
  #       new_chocolates = cur_chocolates + self.chocolates_matrix[l][c]
  #       self.get_chocolate((l, c), new_chocolates, route + [(l, c)])

  def get_chocolate_max_up_to_a_room(self, prev_level, prev_level_chocolates):
    cur_level = prev_level + 1

    if cur_level == self.n:
      self.max_chocolates = max(prev_level_chocolates)
      return

    cur_level_chocolates = [0] * self.n
    for c in range(self.n):
      total_chocolates = [
          prev_level_chocolates[prev_c]
          for prev_c in (c - 1, c, c + 1)
          if 0 <= prev_c < self.n
      ]
      cur_level_chocolates[c] = max(
          total_chocolates) + self.chocolates_matrix[cur_level][c]

    self.get_chocolate_max_up_to_a_room(cur_level, cur_level_chocolates)


n = 5
chocolates_matrix = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5],
                     [1, 2, 3, 4, 5], [100, 2, 3, 4, 5]]

s = Solution()
# c, r = s.get_max_chocolate(n, chocolates_matrix)
# print("factory:{}, total:{}, best_route{}".format(chocolates_matrix, c, r))
c = s.get_max_chocolate(n, chocolates_matrix)
c == 114
print("factory:{}, total:{}".format(chocolates_matrix, c))
