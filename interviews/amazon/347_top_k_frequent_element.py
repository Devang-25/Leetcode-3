'''
347. Top K Frequent Elements
Medium

1333

88

Favorite

Share
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]

'''

##### Solution 1  Time Complexity: O(N*logN)########

from collections import defaultdict
from typing import List


class Solution:

  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    self.cache = defaultdict(int)

    for num in nums:
      self.cache[num] += 1

    # items(): (num, freq)
    # sort time complexity: O(N*logN)
    sorted_tuples = sorted(self.cache.items(), key=lambda x: x[1], reverse=True)

    result = [item[0] for item in sorted_tuples[:k]]

    return result


# nums = [1, 1, 1, 2, 2, 3]
# k = 2
# s = Solution()
# r = s.topKFrequent(nums, k)
# print(r)

# nums = [1]
# k = 1
# s = Solution()
# r = s.topKFrequent(nums, k)
# print(r)

# nums = []
# k = 1
# s = Solution()
# r = s.topKFrequent(nums, k)
# print(r)

################# Solution 2  Time Complexity: O(N)########


class Solution:

  def topKFrequent(self, nums, k):
    word_freq_cache = defaultdict(int)
    freq_word_cache = defaultdict(list)

    for num in nums:
      word_freq_cache[num] += 1

    for num, freq in word_freq_cache.items():
      freq_word_cache[freq].append(num)

    results = []
    for freq in range(len(nums), 0, -1):
      if freq in freq_word_cache:
        results += freq_word_cache[freq]

    return results[:k]


nums = [1, 1, 1, 2, 2, 3]
k = 2
s = Solution()
r = s.topKFrequent(nums, k)
# return [1, 2]
print(r)

nums = [1]
k = 1
s = Solution()
r = s.topKFrequent(nums, k)
# return [1]
print(r)

nums = []
k = 1
s = Solution()
r = s.topKFrequent(nums, k)
print(r)
# return []