"""
problem: 
Given two sorted arrays of integers, find the Kth smallest number.

Assumptions

The two given arrays are not null and at least one of them is not empty

K >= 1, K <= total lengths of the two sorted arrays

Examples

A = {1, 4, 6}, B = {2, 3}, the 3rd smallest number is 3.

A = {1, 2, 3, 4}, B = {}, the 2nd smallest number is 2.




解题思路：
- arr1 start at k/2th index; arra2 starts at k/2th index.
- if array1[k/2 + 1] < arra2[k/2]: include array1[k/2 + 1]; exclude arra2[k/2]; vice versa.
- until no updates.
- return the smallest between (array1[last_include_inde] , array2[last_include_index])

time complexity: 
- 我每次至少可以缩减(k/2)的搜索空间
- 所以我只需要O(logK) 的时间复杂度。

space comlexity: 
- O(1)

"""


class Solution(object):

  def kth(self, a, b, k):
    """
    input: int[] a, int[] b, int k
    return: int
    """
    if not k or (k > (len(a) + len(b))):
      return -1

    # make sure a is always shorter than b.
    while a and b and k:
      # edge case, when only one num is needed to delete.
      if k == 1:
        return min(a[0], b[0])

      if len(a) > len(b):
        a, b = b, a
      ai = (k - 1) // 2 if ((k - 1) // 2) < len(a) else (len(a) - 1)
      bi = k - ai - 2
      print("k", k, "ai", ai, "bi", bi)
      print("a", a, "b", b)

      # compare
      if a[ai] <= b[bi]:
        k -= (ai + 1)
        a = a[ai + 1:]
        if not k:
          return b[bi]
      else:
        k -= (bi + 1)
        b = b[bi + 1:]
        if not k:
          return a[ai]

    if (not a) and b and k:
      return b[k - 1]

    if (not b) and a and k:
      return a[k - 1]


# a = [1]
# b = []
# k = 1
# s = Solution()
# print(s.kth(a, b, k), "\n")

# a = [1, 2]
# b = []
# k = 2

# s = Solution()
# print(s.kth(a, b, k), "\n")

# a = [1, 2, 3]
# b = []
# k = 3

# print(s.kth(a, b, k), "\n")

# a = [1, 2]
# b = [1, 2]
# k = 4
# s = Solution()
# print(s.kth(a, b, k), "\n")

# a = [1, 2]
# b = [1, 2, 3]
# k = 6
# s = Solution()
# print(s.kth(a, b, k), "\n")

# a = [1, 4, 5, 5, 8, 12, 12, 12]
# b = [2, 2, 3, 7, 9, 9, 9]
# k = 14
# s = Solution()
# print(s.kth(a, b, k), "\n")

# a = [1, 2, 3, 4, 5]
# b = [6, 7, 8, 9, 10]
# k = 6
# s = Solution()
# print(s.kth(a, b, k), "\n")

a = [1, 3, 5, 7, 9]
b = [2, 4, 6, 8]
k = 6
s = Solution()
print(s.kth(a, b, k), "\n")
