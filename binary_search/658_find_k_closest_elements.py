"""
there are two approaches: 1) two pointers, 2)max_heap

"""

######### two pointers #####


class Solution(object):

  def findClosestElements(self, arr, k, x):
    """
    :type arr: List[int]
    :type k: int
    :type x: int
    :rtype: List[int]
    """
    self.arr = arr
    self.x = x
    results = []

    # first find the cloest number using binary search
    i = self.search(0, len(arr) - 1)
    results.append(arr[i])

    # use two pointer, see which way we should go
    l = i - 1
    r = i + 1
    # l_num = arr[i - 1]
    # r_num = arr[i + 1]

    while len(results) < k:
      if l < 0:
        results.append(arr[r])
        r += 1
      elif r >= len(arr):
        results.append(arr[l])
        l -= 1
      else:
        l_diff = abs(arr[l] - x)
        r_diff = abs(arr[r] - x)
        if l_diff <= r_diff:
          results.append(arr[l])
          l -= 1
        else:
          results.append(arr[r])
          r += 1

    results.sort()
    return results

  def search(self, s, e):
    print("s:{}, e:{}".format(s, e))
    arr = self.arr
    x = self.x

    mid = (s + e) // 2
    print("mid", mid)
    if arr[mid] == x or s == e or s > e or (mid - 1 < 0 and
                                            mid + 1 == len(arr)):
      print("mid1", mid, arr[mid])
      return mid
    diff = abs(arr[mid] - x)
    l_diff = abs(arr[mid - 1] - x) if (mid - 1) > 0 else float("inf")
    r_diff = abs(arr[mid + 1] - x) if (mid + 1) < len(arr) else float("inf")
    if diff < l_diff and diff < r_diff:
      print("mid2", mid, arr[mid])
      return mid
    space = 2
    while l_diff == r_diff:
      l_diff = abs(arr[mid - space] - x) if (mid - space) > 0 else float("inf")
      r_diff = abs(arr[mid + space] -
                   x) if (mid + space) < len(arr) else float("inf")
      space += 1
    return self.search(s, mid - 1) if l_diff < r_diff else self.search(
        mid + 1, e)


########## heap solution #######

import heapq


class MaxHeap(object):

  def __init__(self):
    self.results = []  # min heap --> max heap

  def pop(self):
    priority, diff = heapq.heappop(self.results)
    return -priority, diff

  def push(self, value):
    priority, diff = value
    heapq.heappush(self.results, (-priority, diff))

  def peak(self):
    priority, diff = self.results[0]
    return -priority, diff


class Solution(object):

  def findClosestElements(self, arr, k, x):
    """
    :type arr: List[int]
    :type k: int
    :type x: int
    :rtype: List[int]
    """
    max_heap = MaxHeap()  # max heap

    for i in range(k):
      diff = arr[i] - x  # recover: k + diff
      priority = abs(diff)
      max_heap.push((priority, diff))

    for j in range(k, len(arr)):
      priority0, diff0 = max_heap.peak()
      # print("p0:{}, diff0:{}".format(priority0, diff0))
      diff1 = arr[j] - x  # recover: k + diff
      priority1 = abs(diff1)
      # print("p1:{}, diff1:{}".format(priority1, diff1))
      if (priority1 < priority0) or (priority1 == priority0 and
                                     diff1 + x < diff0 + x):
        max_heap.pop()
        max_heap.push((priority1, diff1))

    print("max_heap", max_heap.results)
    r = [diff + x for p, diff in max_heap.results]
    r.sort()
    return r