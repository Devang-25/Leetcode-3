import heapq
from typing import List
from collections import defaultdict

# _debug = True

_debug = False


def dprint(*args, **kwargs):
  if _debug:
    print(*args, **kwargs)


class Node:

  def __init__(self, val, index):
    self.val = val
    self.i = index
    self.removed = False
    self.location = None


class MinHeap:

  def __init__(self):
    self.heap = []
    self.remove_count = 0

  def push(self, node):
    assert node.removed == False
    p = node.val
    i = node.i
    node.location = "right"
    heapq.heappush(self.heap, (p, i, node))
    dprint("min p{}, i{}, node{}".format(p, i, node))

  def pop(self):
    p, i, node = heapq.heappop(self.heap)
    # print("p{}, i{}, node{}".format(p, i, node))
    while node.removed:
      node.location = None
      self.remove_count -= 1
      dprint("CAUTIONS")

      item = heapq.heappop(self.heap)
      dprint("item", item)
      p, i, node = item
    return node

  def peek(self):
    p, i, node = self.heap[0]
    while node.removed:
      heapq.heappop(self.heap)
      self.remove_count -= 1
      p, i, node = self.heap[0]
    return node

  def __len__(self):
    # dprint("len of min heap", len(self.heap))
    # dprint("remove count", self.remove_count)
    assert len(self.heap) - self.remove_count >= 0
    return len(self.heap) - self.remove_count


class MaxHeap:

  def __init__(self):
    self.heap = []
    self.remove_count = 0

  def push(self, node):
    assert node.removed == False
    p = -node.val
    i = node.i
    node.location = "left"
    heapq.heappush(self.heap, (p, i, node))
    dprint("max p{}, i{}, node{}".format(p, i, node))
    if node.removed == True:
      self.remove_count += 1

  def pop(self):
    p, i, node = heapq.heappop(self.heap)
    while node.removed:
      node.location = None
      self.remove_count -= 1
      p, i, node = heapq.heappop(self.heap)
    return node

  def peek(self):
    p, i, node = self.heap[0]
    while node.removed:
      heapq.heappop(self.heap)
      self.remove_count -= 1
      p, i, node = self.heap[0]
    return node

  def __len__(self):
    # dprint("len of max heap", len(self.heap))
    # dprint("remove count", self.remove_count)
    assert len(self.heap) - self.remove_count >= 0
    return len(self.heap) - self.remove_count


class Solution:

  def __init__(self):
    self.left_heap = MaxHeap()
    self.right_heap = MinHeap()
    self.results = []
    self.dict = defaultdict()

  def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
    # push the first k ele into the heap
    # always make left has equal or one more element than right
    if not nums:
      return self.results

    for i in range(k):
      dprint("\n[{}]:{}".format(i, nums[i]))
      self._add(i, nums)
    median = self.find_median()
    self.results.append(median)
    dprint("results", self.results)

    for i in range(k, len(nums)):
      dprint("\n[{}]: {}".format(i, nums[i]))
      # remove
      self._remove(i - k, nums)
      # add
      self._add(i, nums)
      median = self.find_median()
      self.results.append(median)

    return self.results

  def find_median(self):
    dprint("start find median")
    if len(self.left_heap) > len(self.right_heap):
      dprint("from left")
      node = self.left_heap.peek()
      median = float(node.val)

    elif len(self.left_heap) == len(self.right_heap):
      dprint("from left and right")
      left = self.left_heap.peek()
      right = self.right_heap.peek()
      median = (left.val + right.val) / 2.0

    dprint("find median", median)
    return median

  def _add(self, index, nums):
    dprint("add[{}]: {}".format(index, nums[index]))
    num = nums[index]
    node = Node(num, index)
    self.dict[index] = node

    if not self.left_heap and not self.right_heap:
      self.left_heap.push(node)

    else:
      left = self.left_heap.peek()

      if num <= left.val:
        self.left_heap.push(node)
      else:
        self.right_heap.push(node)
    self._balance()

  def _remove(self, index, nums):
    dprint("remove [{}]: {}".format(index, nums[index]))
    node = self.dict[index]

    if node.location == "left":
      self.left_heap.remove_count += 1
    elif node.location == "right":
      self.right_heap.remove_count += 1

    node.removed = True
    self._balance()

  def _balance(self):
    dprint("BALANCE HEAP BEFORE")
    dprint("left len", len(self.left_heap))
    dprint("right len", len(self.right_heap))

    while len(self.left_heap) - len(self.right_heap) > 1:
      dprint("while left has more")
      node = self.left_heap.pop()
      self.right_heap.push(node)

    while len(self.right_heap) > len(self.left_heap):
      dprint("while right has more")
      node = self.right_heap.pop()
      self.left_heap.push(node)

    dprint("BALANCE HEAP AFTER")
    dprint("left len", len(self.left_heap))
    dprint("right len", len(self.right_heap))


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
s = Solution()
r = s.medianSlidingWindow(nums, k)
dprint("nums", nums)
dprint("FINAL RESULT", r)
assert r == [1, -1, -1, 3, 5, 6]

nums = [1, 1, 1, 1]
k = 2
s = Solution()
r = s.medianSlidingWindow(nums, k)
dprint("nums", nums)
dprint("FINAL RESULT", r)
assert r == [1.0, 1.0, 1.0]

nums = []
k = 0
s = Solution()
r = s.medianSlidingWindow(nums, k)
dprint("nums", nums)
dprint("FINAL RESULT", r)
assert r == []

nums = [0]
k = 1
s = Solution()
r = s.medianSlidingWindow(nums, k)
dprint("nums", nums)
dprint("FINAL RESULT", r)
assert r == [0.0]

nums = [2147483647, 1, 2, 3, 4, 5, 6, 7, 2147483647]
k = 2
s = Solution()
r = s.medianSlidingWindow(nums, k)
dprint("nums", nums)
dprint("FINAL RESULT", r)
# assert r == [0.0]
