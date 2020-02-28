"""
input [int] in ascending order

ouput [x1, x2, x3, ... ] where x_i % x_i-1 == 0,后面一个数可以除尽前面一个数。

思路：
- 不一定有同一个factor因数就能除得尽。
- 大的那个数要有小的那个数的所有因数。

- 用一个dict来记录每一包括第i个数字的最长答案
- 就一个数 i，除以（0， i）的数j：
  如果可以除尽，
  且dict[j] 的最长路径+1超过dict[i]，
  那么dict[i] = dict[j] + [nums[i]]

worst case time complexity:
O(N^2)
"""
def dprint(*args, **kwargs):
  print(*args)
  print(**kwargs)


from collections import defaultdict

def longest_common_multiple(nums):
  """
  input nums: [int] in ascedning order
  output type: results is  [int]
  """
  # routes_dict{index: [int]}
  routes_dict = defaultdict(list)

  for i in range(0, len(nums)):
    dprint("i{}, num{}".format(i, nums[i]))
    routes_dict[i] = [nums[i]]
    for j in range(0, i):
      if nums[i] % nums[j] == 0:
        if len(routes_dict[i]) < len(routes_dict[j]) + 1:
          routes_dict[i] = routes_dict[j] + [nums[i]]

  longest_routes = max([route for index, route in routes_dict.items()],
  key = lambda x: len(x))

  return longest_routes

nums = [2, 3, 4, 6, 8, 12]
print(longest_common_multiple(nums))
