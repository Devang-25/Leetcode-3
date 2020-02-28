"""
problem:

Given a target integer T, a non-negative integer K and an integer array A sorted in ascending order, find the K closest numbers to T in A.

Assumptions

A is not null
K is guranteed to be >= 0 and K is guranteed to be <= A.length
Return

A size K integer array containing the K closest numbers(not indices) in A, sorted in ascending order by the difference between the number and T. 
Examples

A = {1, 2, 3}, T = 2, K = 3, return {2, 1, 3} or {2, 3, 1}
A = {1, 4, 6, 8}, T = 3, K = 3, return {4, 1, 6}


解题思路：
- Closet k elements"
    - What is k is larger than N? Then time complexity become O(N), then would binary search loose its point?
        - 1) find the target, then split the array into half at the target. 
        - 2)left side (from left to right) has the diff from largest to smallest
        - 3) right side (from lelf to right) has diff from smallest to largest. 
        - 4) then just solve it like kith smallest in two sorted array. 

[0, 1, 2, 3, 4, 5, 6]
taget = 3
k = 3
[3, 2, 1]
        [0, 1, 2, 3]

time complexity: 
- first find the target: O(log N)
- then find kth smallest element: O(log K)
= O(logN)
This would be the case even when k is really big, as big as N.

Space complexity:
- O(N) for store the difference
- O(K) for result.
= O(N + K)


line 61: Need improvement in reverse, which take O(N) time
line 5: Need improvement on sorted time, which take O(KlogK) time


"""


class Solution(object):

  def kClosest(self, array, target, k):
    """
    input: int[] array, int target, int k
    return: int[]
    """
    mid = self.find_target(array, target)
    # find difference
    l = array[:mid]
    l.reverse()
    r = array[mid:]

    results = self.find_k_smallest(l, r, k, target)
    results = sorted(results, key=lambda x: abs(x - target))
    return results

  def find_target(self, nums, target):
    """
    find the index of the number that is closest to target
    """

    l = 0
    r = len(nums) - 1

    while l < (r - 1):
      mid = (l + r) // 2
      if nums[mid] == target:
        return mid
      elif nums[mid] < target:
        l = mid
      elif nums[mid] > target:
        r = mid

    return l if abs(nums[l] - target) <= abs(nums[r] - target) else r

  def find_k_smallest(self, a, b, k, target):
    """
    goals: find the k smallest elements and return those elements.

    inputs:
    a: sorted list[int]
    b: sorted list[int]
    k: int

    output:
    result: list[int]
    """
    results = []

    while a and b and k:
      print("\n results", results)
      if k == 1:
        num = a[0] if abs(a[0] - target) <= abs(b[0] - target) else b[0]
        results.append(num)
        print("result when k is 1", results)
        k -= 1

      ai = (k - 1) // 2 if ((k - 1) // 2 < len(a)) else (len(a) - 1)
      bi = k - ai - 2
      print("k", k)
      print("ai", ai, "bi", bi)
      print("a:", a)
      print("b", b)

      a_diff = abs(a[ai] - target)
      b_diff = abs(b[bi] - target)
      if a_diff <= b_diff:
        results += a[:ai + 1]
        a = a[ai + 1:]
        k -= (ai + 1)
        print("update a:", a)
        print("ai + 1:", ai + 1)
      else:
        # nums = [num - target for num in b[:bi + 1]]
        results += b[:bi + 1]
        b = b[bi + 1:]
        k -= (bi + 1)
        print("update b:", b)
        print("bi + 1:", bi + 1)

      print("updated k", k)

    if (not a) and b and k:
      nums = [b[i] for i in range(k)]
      results += nums

    if (not b) and a and k:
      nums = [a[i] for i in range(k)]
      results += nums

    return results


# a = [1, 3, 5, 7, 9]
# target = 4
# s = Solution()
# print(s.find_target(a, target), "\n")

# a = [0, 1, 2]
# b = [1, 2, 3]
# k = 4
# target = 0
# s = Solution()
# print(s.find_k_smallest(a, b, k, target))

# a = [1, 3, 5, 7, 9]
# target = 4
# k = 2
# s = Solution()
# print(s.kClosest(a, target, k), "\n")

# a = [1, 3, 3, 6, 9, 9, 12, 15]
# target = 10
# k = 5
# s = Solution()
# print(s.kClosest(a, target, k), "\n")

a = [1, 5]
target = 10
k = 2
s = Solution()
print(s.kClosest(a, target, k), "\n")
