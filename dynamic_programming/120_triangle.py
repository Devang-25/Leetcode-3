"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

"""


class Solution(object):
    def minimumTotal_1(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        result = []
        for line in range(1, len(triangle)):
            result.append([0] * line)
        result.append(triangle[-1])

        for i in reversed(range(len(triangle))):
            for j in range(i):
                result[i - 1][j] = min(result[i][j], result[i][j+1]) + triangle[i - 1][j]

        return result[0][0]

    def minimumTotal_2(self, triangle):
        # modify the triangle in place
        if not triangle:
            return

        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] = min(triangle[i+1][j], triangle[i+1][j+1]) + triangle[i][j]
        return triangle[0][0]

    def minimumTotal_3(self, triangle):
        # O(n) space
        if not triangle:
            return
        result = triangle[-1]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                result[j] = min(result[j], result[j+1]) + triangle[i][j]
        return result[0]

triangle_1 = [[2],[3,4],[6,5,7],[4,1,8,3]]
