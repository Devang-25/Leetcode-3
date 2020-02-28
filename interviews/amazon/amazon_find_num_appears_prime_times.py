"""
给一个Array, 里面有一个元素出现了奇数次，其他的都出现了偶数次，求出现奇数次的数字，不能用位操作。

"""

from collections import Counter


def find_prime(nums):
  counter = Counter(nums)

  for num, times in counter.items():
    if times == 2:
      return num
    if times % 2 == 0:
      continue
    for n in range(3, times, 2):
      if times % n == 0:
        continue
    return num
  return []


nums = [1, 1, 1, 1, 2, 2, 3, 3, 3, 3]
r = find_prime(nums)
print("r", r)
