"""
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

"""
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        top = 0
        bottom = n - 1
        left = 0
        right = n - 1

        result = [[0 for i in range(n)] for j in range(n)]

        # result[i][j]: i=row, j = col
        num = 1
        while num <= (n*n):
            for j in range(left, right + 1):
                result[top][j] = num
                num += 1
            top += 1

            for i in range(top, bottom + 1):
                result[i][right] = num
                num +=1
            right -= 1

            if top <= bottom:
                for j in reversed(range(left, right + 1)):
                    result[bottom][j] = num
                    num += 1
                bottom -= 1

            if left <= right:
                for i in reversed(range(top, bottom + 1)):
                    result[i][left] = num
                    num += 1
                left += 1

        return result

Solution().generateMatrix(3)
