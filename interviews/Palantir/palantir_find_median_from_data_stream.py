"""
since python only has min heap, so I want to implement a max heap for the left heap

"""

import heapq
from collections import defaultdict

class MaxHeap(object):
    def __init__(self):
        """
        initialize a heap
        """
        self.heap = []

    def push(self, num):
        # if 1 is inside, add 2, 2 -> -2--> < 1
        heapq.heappush(self.heap, -num)

    def pop(self):
        "Purpose: return teh max number in the heap"
        num = heapq.heappop(self.heap)
        return -num

    def peak(self):
        # peak at the largest item in the heap
        return -self.heap[0] if self.heap else None

    def __len__(self):
        return len(self.heap)


class MinHeap(object):
    def __init__(self):
        self.heap = []

    def push(self, num):
        heapq.heappush(self.heap, num)

    def pop(self):
        return heapq.heappop(self.heap)

    def peak(self):
        # peak the smallest item in the heap
        return self.heap[0]

    def __len__(self):
        return len(self.heap)


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        # left heap is always equal or 1 more than the right heap
        """
        self.left_heap = MaxHeap()
        self.right_heap = MinHeap()
        self.mean = 0
        self.nums_count = 0

        self.mode = None
        self.mode_dict = defaultdict(int)


    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        # print("add num {}".format(num))
        if not self.left_heap and not self.right_heap:
            self.left_heap.push(num)

        else:
            left = self.left_heap.peak()
            # right = self.right_heap.peak()
            if num <= left:
                self.left_heap.push(num)
            else:
                self.right_heap.push(num)
            self._balance()
        # print("added num {}".format(num))
        self.mean = float(self.mean * self.nums_count + num) / (self.nums_count + 1.0)
        self.nums_count += 1

        self.mode_dict[num] += 1
        if self.mode_dict[num] > self.mode_dict[self.mode]:
            self.mode = num

    def _balance(self):
        """
        rtype: void
        """
        while len(self.left_heap) - len(self.right_heap) > 1:
            print("left_more before: left{}, right{}".format(len(self.left_heap), len(self.right_heap)))
            item = self.left_heap.pop()
            self.right_heap.push(item)
            print("after: left{}, right{}".format(len(self.left_heap), len(self.right_heap)))
        while len(self.right_heap) - len(self.left_heap) > 0:
            print("right_more before: left[{}], right[{}]".format(len(self.left_heap), len(self.right_heap)))
            print("right_more before: left{}, right{}".format(len(self.left_heap), len(self.right_heap)))
            item = self.right_heap.pop()
            self.left_heap.push(item)
            # print("after: left{}, right{}".format(len(self.left_heap), len(self.right_heap)))

    def findMedian(self):
        """
        :rtype: float
        """
        # print("find median")
        if len(self.left_heap) - len(self.right_heap) == 1:
            # left side is max heap
            # print("1 median", float(self.left_heap.peak()))
            return float(self.left_heap.peak())
        elif len(self.left_heap) == len(self.right_heap):
            # print("self.left_heap.peak {} , self.right_heap.peak{}, total {}".format(self.left_heap.peak(), self.right_heap.peak(), self.left_heap.peak() + self.right_heap.peak()))
            # print("2 median", float(self.left_heap.peak() + self.right_heap.peak()) / 2.0)
            return float(self.left_heap.peak() + self.right_heap.peak()) / 2.0


    def findMean(self):
        """
        rtype: float
        """
        return self.mean

    def findMode(self):
        """
        rtyep: int
        """
        return self.mode

    # def findMode()


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
param_2 = obj.findMedian()
print("median of (1,2) is {}".format(param_2))
mean1 = obj.findMean()
print("mean of (1, 2) is {}".format(mean1))
obj.addNum(3)
param_3 = obj.findMedian()
print("median of (1,2,3) is {}".format(param_3))
obj.addNum(2)
param_4 = obj.findMode()
print("mode of (1,2,3, 2) is {}".format(param_4))
