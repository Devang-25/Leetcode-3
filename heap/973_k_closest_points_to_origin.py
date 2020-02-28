
############# Linkcode 612 ###############

"""

612. K个最近的点
中文English
给定一些 points 和一个 origin，从 points 中找到 k 个离 origin 最近的点。按照距离由小到大返回。如果两个点有相同距离，则按照x值来排序；若x值也相同，就再按照y值排序。

Example
例1:

输入: points = [[4,6],[4,7],[4,4],[2,5],[1,1]], origin = [0, 0], k = 3
输出: [[1,1],[2,5],[4,4]]
例2:

输入: points = [[0,0],[0,9]], origin = [3, 1], k = 1
输出: [[0,0]]

"""

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
import heapq

class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
        # write your code here
        k_max_heap = []
        x0, y0 = origin.x, origin.y

        for point in points:
            x, y = point.x, point.y
            distance = -((x-x0) * (x-x0) + (y-y0)*(y-y0))
            if len(k_max_heap) < k:
                heapq.heappush(k_max_heap, (distance, -x, -y))
            else:
                heapq.heappushpop(k_max_heap, (distance, -x, -y))

        results = []
        while k_max_heap:
            distance, x, y = heapq.heappop(k_max_heap)
            results.append((-x, -y))

        return results[::-1]



################# Leetcode 973 #############


"""

We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)



Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].

"""

from collections import defaultdict

class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]

        need to use max heap
        """
        results = []
        distance_cache = defaultdict(list)
        for point in points:
            x, y = point
            distance = (x*x + y*y)
            # print("distance", distance)
            distance_cache[distance].append(point)

            if len(results) < K:
                heapq.heappush(results, -distance)

            else:
                heapq.heappushpop(results, -distance)
            # print(results)

        answer = []
        while results:
            distance = - heapq.heappop(results)
            # print("distance", distance)
            # print(distance_cache[distance])
            answer.append(distance_cache[distance].pop())
        return answer[:K]
