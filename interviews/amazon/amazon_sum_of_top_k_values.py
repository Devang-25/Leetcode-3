'''
给你一个iterator, iterator 动态输入数字:比如 【1，2，0，4，5，2】； 
你写个function 能够及时返回 top 3 value's sum

- use max heap to maintain the top 3 values
- whenever there is a new number: compare it with min heap, the smallest node in min_heap
  - if new num > top node in min_heap: pop and push; update sum
  - else: pass

'''
import heapq


class Solution:

  def __init__(self, nums, k):
    self.sum = 0
    self.min_heap = []
    # def top_k_val_sum(self, nums, k):
    """
    inputs: 
      nums: [int]

      k: int. indicate the top k values we want

    return:
      self.sum: int
    """
    self.nums = nums

    for i in range(k):
      heapq.heappush(self.min_heap, self.nums[i])
      self.sum += self.nums[i]
      # print("1 sum", self.sum)

    for i in range(k, len(nums)):
      self.update(self.nums[i])
      # print("2 sum", self.get_sum())

  def get_sum(self):
    return self.sum

  def add(self, new_num):
    self.nums.append(new_num)
    self.update(new_num)
    # print("3 sum", self.get_sum())

    # return self.sum

  def update(self, new_num):
    min_val = self.min_heap[0]
    if new_num > min_val:
      heapq.heappop(self.min_heap)
      heapq.heappush(self.min_heap, new_num)
      self.sum = self.sum - min_val + new_num


nums = [1, 2, 0, 4, 5, 2]
s = Solution(nums, k=3)  #return 11
print(s.get_sum())
s.add(6)
print(s.get_sum())  # return 15
"""
Time complexity for Heappop():
O(longN), n = level of heap

time complexity for heappush():
O(LogN), n = level of heap

time complexity of update sum: 
O(1)

So, overall time complexity: O(N*Log(N))
the time complexity to add a number if O(log(N))

"""
