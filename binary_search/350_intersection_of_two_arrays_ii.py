from typing import List
from collections import Counter


class Solution:

  def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    dict1 = Counter(nums1)  #O(N)
    dict2 = Counter(nums2)  #O(M)
    results = []

    if len(dict1) >= len(dict2):
      dict1, dict2 = dict2, dict1
    for ele in dict1:  #O(M or N) whichever is shorter
      if ele in dict2:
        times = min(dict1[ele], dict2[ele])
        new = [ele for i in range(times)]
        results += new

    return results


"""
time complexity: O(N) + O(M) + O(M or N) whichever is smaller
= O(M or N) whichever is smaller

"""

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
# [2, 2]

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
# [4, 9]

s = Solution()
print(s.intersection(nums1, nums2))