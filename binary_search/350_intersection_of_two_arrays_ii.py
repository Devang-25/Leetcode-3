from typing import List
from collections import Counter
"""
Solution1: Hash Table
time complexity: O(N) + O(M) + O(M or N) whichever is smaller
= O(M or N) whichever is smaller

Solution2: Linear Scan (or Two Pointers) 
# only if the inputs are sorte or need to sort inputs
time complexity: O(N) + O(M) if inputs are sorted
time compelxity O(NlogN) + O(MlogM) + O(M) + O(N) if inputs are not sorted


Q: What if the given array is already sorted? How would you optimize your algorithm?
Solution 2 Linear scan is better. It is faster.

Q: What if nums1's size is small compared to nums2's size? Which algorithm is better?
If that is the case, than hash table Solution 2 is still better. Unless the inputs are not sorted, than solution 1 hash table would be better. 

Q: What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
- if cannot read all the elements of nums2 all at a time, (but can read nums1 all at a time), then we can process chunk at a time. 
- if both nums1 are nums2 cannot be process all at a time, then we should sort nums1 and nums2 individually (external sort), and then use linear scan (two pointers) to process them.

An improvement can be sort them using external sort, read (let's say) 2G of each into memory and then using the 2 pointer technique, then read 2G more from the array that has been exhausted. Repeat this until no more data to read from disk.



"""


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


############# if the input are sorted ##########

  def intersect_sorted(self, nums1: List[int], nums2: List[int]) -> List[int]:
    nums1.sort()
    nums2.sort()

    results = []

    i, j = 0, 0

    while i < len(nums1) and j < len(nums2):
      if nums1[i] == nums2[j]:
        results.append(nums1[i])
        i += 1
        j += 1
      elif nums1[i] > nums2[j]:
        j += 1
      elif nums1[i] < nums2[j]:
        i += 1

    return results

s = Solution()

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
# [2, 2]

print(s.intersect_sorted(nums1, nums2))

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
# [4, 9]
print(s.intersect_sorted(nums1, nums2))

# print(s.intersection(nums1, nums2))
