# 1) Kth smallest number in prime numbers

\1. 给你几个质数，他们作为分母的所有分数，然后找出第k小的分数，大概就是比如质数2，3，5。那么就有1/2, 1/3, 2/3, 1/5, 2/5, 3/5, 4/5, 那么第2小就是1/3。然后还有follow up就是如果k很大的时候，怎么解.

\- Min Heap

\- 先加第一档（1/5, 1/3,....)

\- 在每一档里，如果已经找到一个数不能往heap里加了的话，那就不再继续在这一档里面找了。 

```python
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
  """
  if not nums:
    return None
  
  results = []

  for i in range(1, max(nums)):
    for j in reversed(nums):
      if i < j:
        print("i", i, "j", j)
        num = - Fraction(i, j)
        # if num > smallest results[0]
        if len(results) < k:
          heapq.heappush(results, num)
        elif num > results[0]:
          heapq.heappushpop(results, num)
          print("after", results)
        else:
          break
  print(results)  
  # return -(heapq.heappop(results))
  return -results[0]

# nums = [2, 3, 5]
k = 3

nums = []

a = kth_smallest(nums, k)
print(a)

```



#  2) Maintain Median 维护中位数

维护一个中位数。先要支持add和get. 

思路：

- 用两个heap来储存：中位数存在左边, 如果数量是单数的话。
- 左边：比中位数小 + 中位数 (max heap）， 所以root是最大的
- 右边： 中位数 + 比中位数大， min heap, 所以root是最小的
- 中位数：
  - 如果左右两边长度相同：
    - 左 + 右）/ 2
  - 如果左右两边不同，则：
    - （左 + 右）/ 2



当加一个数字时：

 - 如果比median大：加到右边
 - 如果比median小：加到左边
 - 检查两边的heap长度是否相等：
    - 左边长：左边pop，加到右边
    - 右边长：右边pop, 加到左边





```python
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
```



# 3) Maximum score of Circle

给一堆(x, y)的二维坐标，每一个坐标对应一个整形的score。以原点为圆心的，会有很多圆存在。需要找出一个圆，使得这个圆内的（包括圆上）所有score的和最大。

\- 有些score可能是负数，因此并不是圆圈越大越好

\- 打算用dynamic programming

\- ith's core = (i-1)th score + new scores

问题：有办法很快的算一个点given (x, y)坐标的位置吗？

\- 正常算法：radius = (x^2 + y^2)^(1/2) ==> O(1)

问题：如何找到在界定内的点？

\- 1）dict (radius): score1, score2,...

\- 2) heap(sorted radius) - min-heap: so pop would returnt the smallest radius - O(nlogn)

\- or list(sorted radius) - O(Nlog(N))



```Python
from collections import defaultdict
import heapq

def largest_score(coordinates, scores):
  if not coordinates or not scores:
    return "empty"

  cache = defaultdict(list)
  radius = set()

  for i, coord in enumerate(coordinates):
    r = (coord[0]**2 + coord[1]**2) ** (1/2)
    cache[r].append(scores[i])
    radius.add(r)
  radius = sorted(list(radius))
  
  max_area = 0
  max_r = 0
  area = 0
  
  for r in radius:
    new_area = sum(cache[r])
    area += new_area
    if area > max_area:
      max_area = area
      max_r = r
  
  return (max_area, max_r)

#########################Test cases ###########

# coordinates = [(0, 0), (1, 1), (1, 1.5), (2, 2)]
# scores = (5, -2, 6, -7)

coordinates = []
scores = ()

coordinates = [(0, 0), (1, 1), (-2, 2), (2, 2)]
scores = (5, -2, 7, 6)

result = largest_score(coordinates, scores)
print("max_area: {}, optimal_radius: {}".format(result[0], result[1]))
```

