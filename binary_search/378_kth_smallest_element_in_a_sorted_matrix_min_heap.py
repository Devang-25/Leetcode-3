from typing import List
"""
Min Heap: 
- first put all the elments in the first row into your heap. 
- Then pop out the minimum number and push in the next smallest element in the same col as the mininum element you just pop out.
- Repeat above step for k times. 

need to:
1) Min_heap: python has min heap. 
2) for each tuple push into the heap, (value, row, col)
"""

import heapq


class Solution:

  def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

    min_heap = []

    # push the first row into the heap
    cols = len(matrix[0])
    rows = len(matrix)

    for c in range(cols):
      element = (matrix[0][c], 0, c)  # (val, row, col)
      heapq.heappush(min_heap, element)
    print("min_heap", min_heap)

    # pop smallest ele and push subsequent smallest element in the same col for k times.
    for i in range(k - 1):
      print("i:{}".format(i))
      min_val, row, col = heapq.heappop(min_heap)
      print("pop: {}, row{}, col{}".format(min_val, row, col))
      if row < (rows - 1):
        # print("elemenet:({}, {}, {})".format(matrix[]))
        new_element = (matrix[row + 1][col], row + 1, col)
        print("new: {}, row:{}, col:{}".format(matrix[row + 1][col], row + 1,
                                               col))
        heapq.heappush(min_heap, new_element)
        print("cur:", min_heap)

    kth_val = min_heap[0][0]

    return kth_val


matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
k = 8
# return 13

# matrix = [[1, 2], [3, 3]]
# k = 2
# # return 2

s = Solution()
print(s.kthSmallest(matrix, k))
