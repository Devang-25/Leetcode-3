"""
维护一个中位数。先要支持add和get,remove.

思路：

- 用两个heap来储存：中位数存在左边, 如果数量是单数的话。
- 左边：比中位数小 + 中位数 (max heap）， 所以root是最大的
- 右边： 中位数 + 比中位数大， min heap, 所以root是最小的
- 中位数：
  - 如果左右两边长度相同：
    - (左 + 右）/ 2
  - 如果左右两边不同，则：
    - 左



当加一个数字时：

- 如果比median大：加到右边
- 如果比median小：加到左边
- 检查两边的heap长度是否相等：
  - 左边长：左边pop，加到右边
  - 右边长：右边pop, 加到左边
"""

############### Pony: with Add(), Get_Median(), Remove() fucntions ##########

import heapq
from collections import defaultdict

class Heap:
  def __init__(self, min_heap = True):
    self.heap = []
    self.remove_dict = defaultdict(int)
    self.remove_count = 0
    self.ele_dict = defaultdict(int)
    self.min_heap = min_heap


  def __len__(self):
    return len(self.heap) - self.remove_count

  def push(self, num):
    if self.min_heap:
      heapq.heappush(self.heap, num)
    else: # max heap
      heapq.heappush(self.heap, -num)
    self.ele_dict[num] += 1

  def pop(self):
    extra = heapq.heappop(self.heap) if self.min_heap else -heapq.heappop(self.heap)
    while extra in self.remove_dict:
      self.remove_dict[extra] -= 1
      self.remove_count -= 1
      extra = heapq.heappop(self.heap) if self.min_heap else -heapq.heappop(self.heap)
    return extra

  def top(self):
    if self.min_heap:
      return self.heap[0]
    else:
      return -self.heap[0]

  def remove_ele(self, num):
    if self.ele_dict[num] <= 0:
      print("{} not in the heap: {}".format(num, self.ele_dict[num]))
    else:
      self.ele_dict[num] -= 1
      self.remove_dict[num] += 1
      self.remove_count += 1


class MaintainMedian:
  """
  - 希望知道中位数

  - 功能支持： 1）add 2)get 3)remove

  input nums: list of int
  """
  def __init__(self):
    self.left = Heap(min_heap = False)
    self.right = Heap(min_heap = True)


  def get_median(self):
    left_actual_len = len(self.left)
    right_actual_len = len(self.right)

    if left_actual_len > right_actual_len:
      return self.left.top()
    elif left_actual_len == 0 and right_actual_len == 0:
      return 0
    elif left_actual_len == right_actual_len:
      return (self.left.top() + self.right.top()) / 2

  def add(self, num):
    medium = self.get_median()
    if num < medium:
      self.left.push(num)
    elif num >= medium:
      self.right.push(num)
    self._balance_heap()

  def remove_num(self, num):
    median = self.get_median()

    if num < median:
      self.left.remove_ele(num)
    else:
      self.right.remove_ele(num)

    self._balance_heap()

  def _balance_heap(self):
    while (len(self.left) - len(self.right)) > 1:
      extra = self.left.pop()
      self.right.push(extra)

    while (len(self.right) - len(self.left)) > 0:
      extra = self.right.pop()
      self.left.push(extra)


s = MaintainMedian()
s.add(1)
print("median", s.get_median())

s.add(2)
print("median", s.get_median())

s.remove_num(1)
print("remove 1.1")

s.remove_num(1) # should return "not in heap"
print("remove 1.2")
print("left", s.left.heap, "right", s.right.heap)
print("median", s.get_median())


s.add(1)
print("add 1")
print("median", s.get_median())


s.add(3)
print("median", s.get_median())
s.add(4)
print("median", s.get_median())
s.add(5)
print("median", s.get_median())




############## Leetcode 
import heapq

class maintainMedian():
  def __init__(self):
    self.left = [] #max heap, smallest is the biggest
    self.right = [] #min heap, smallest is smallest

  def get_median(self):
    if not self.left and not self.right:
      return "empty"
    if len(self.left) > len(self.right):
      return -self.left[0]
    elif len(self.left) == len(self.right):
      return (-self.left[0] + self.right[0])/2

  def add(self, num):
    print("add num", num)
    if not self.left and not self.right:
      # left is max heap, to implement, we have to make the number negative
      self.left.append(-num)
    else:
      if num > self.get_median():
        heapq.heappush(self.right, num)
        if len(self.right) > len(self.left): # to maintina the order, left should always > or = to len(right)
          print('right has more')
          assert(len(self.right) - len(self.left) == 1)
          extra = heapq.heappop(self.right)
          print("right extra", extra)
          heapq.heappush(self.left, -extra)
          print("left and right", self.left, self.right)
      elif num < self.get_median():
        heapq.heappush(self.left, num)
        if (len(self.left) - len(self.right)) >= 2:
          assert(len(self.right) - len(self.left) == -2)
          print("right has more")
          extra = heapq.heappop(self.left)
          heapq.heappush(self.left, extra)


s = maintainMedian()
s.add(1)
print(s.get_median())
s.add(2)
print(s.get_median())
s.add(3)
print(s.get_median())
s.add(4)
print(s.get_median())
s.add(5)
print(s.get_median())
