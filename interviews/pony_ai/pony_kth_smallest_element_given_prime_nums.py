"""
1. 给你几个质数，他们作为分母的所有分数，然后找出第k小的分数，大概就是比如质数2，3，5。那么就有1/2, 1/3, 2/3, 1/5, 2/5, 3/5, 4/5, 那么第2小就是1/3。然后还有follow up就是如果k很大的时候，怎么解.
- Min Heap
- 先加第一档（1/5, 1/3,....)
-
- 1题 n sorted list 找kth

"""



import heapq
from fractions import Fraction

def kth_smallest(nums, k):
  # create a max heap with k element
  # b/c I want the kth largest
  """
  # results = [-float("inf")] * k
  # heapq.heapify(results)

  Why do I not heapify the reresults up front?
  - because heapq just modify the list in place
  - results remain a list
  - heapq just reorder it.
  - so rather just check the length of list results later in the loop.
  - it is faster this way.

  Another reason:
  - if k is biggest than the num of available numbers:
  - then function would return -inf if I use the above method.
  - the new way below would avoid this type of error in such corner cases.


  Note:
  - Python only has min heap, NOT max heap.
  - I want the kth smallest.  -> 所以我存每个数的负数。这样最大的就变成最小的。



  """


  if not nums:
    return None

  results = []

  for i in range(1, max(nums)):
    for j in reversed(nums):
      if i < j:
        print("i", i, "j", j)
        # num = - (i/j)
        num = - Fraction(i, j)
        # if num > smallest results[0]
        if len(results) < k:
          heapq.heappush(results, num)
      elif num >= results[0]:
          heapq.heappushpop(results, num)
          print("after", results)
        else:
          break
  print(results)
  # return -(heapq.heappop(results))
  return -results[0] # return the smallest ele in the list, which is the biggest in the list

# nums = [2, 3, 5]
k = 3

nums = []

a = kth_smallest(nums, k)
print(a)
