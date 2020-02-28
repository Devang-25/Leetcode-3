"""
解题思路：
- we search in the smaller array.
- we use binary search to see where the partition should be.

Example 1: 
x = [ 1, 3, 8, 9, 15]
Y = [7, 11, 18, 19, 21, 25]

Start = 0
End = 5
Partition x = (0 + 5) / 2 = 2
Partition y = (x + y + 1) / 2 - partition x
		= (5 + 6 + 1) / 2 - 2 
		= 6 - 2 = 4

#########################

How to handle edge cases: 
- if short array are all on left or all on right, 
- then we use {-inf} or {+inf}.
- When all elements are on the right side, the left side is just {-inf}
- when all elements are on the left side, the right side is just {+inf}

edge case 1: 
x=  [23, 26, 31, 35]
Y= [3, 5, 7, 9, 11, 16]

Start = 0
End = 4

Left: {-inf}             | 23, 26, 31, 36
Right: 1, 3, 6, 7, 9 | 11



"""

import os

debug = True

# debug = False


def dprint(*args, **kwargs):
  if debug == True:
    print(*args, **kwargs)


class Solution(object):

  def findMedianSortedArrays(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    # alwasy make sure nums1 is the shorter than nums2
    if len(nums1) > len(nums2):
      nums1, nums2 = nums2, nums1

    dprint("#############################")
    dprint("nums1:", nums1)
    dprint("nums2:", nums2)

    start = 0
    end = len(nums1)

    # i = 0
    while start <= end:
      partition_x = (start + end) // 2
      partition_y = (len(nums1) + len(nums2) + 1) // 2 - partition_x

      dprint("\n")
      dprint("start:{}, end:{}".format(start, end))
      dprint("partition x", partition_x)
      dprint("partition y", partition_y)
      """
      check all the cases:
      x_left | x_right
      y_left | y_right
      
      corner case: 
      if x_left is empty: partition_x = 0 , x_left = {-inf}
      if x_right is empty: partition_x = len(nums1), x_right = {+inf}
      """
      x_left = float("-inf") if partition_x == 0 else nums1[partition_x - 1]
      x_right = float("inf") if partition_x == len(
          nums1) else nums1[partition_x]
      y_left = float("-inf") if partition_y == 0 else nums2[partition_y - 1]
      y_right = float("inf") if partition_y == len(
          nums2) else nums2[partition_y]

      dprint(x_left, "|", x_right)
      dprint(y_left, "|", y_right)

      if x_left <= y_right and y_left <= x_right:
        dprint("find")
        break
      elif x_left > y_right:
        # 左边的数大于右边的数，需要把partion_x往左挪
        # need to move the partion x to left
        dprint("move left")
        end = partition_x - 1
      elif x_right < y_left:
        # 上右的数小于下做的数，需要把partition_x往右挪
        dprint("move right")
        start = partition_x + 1

      # i += 1
    if (len(nums1) + len(nums2)) % 2 == 1:
      return max(x_left, y_left)
    else:
      return (max(x_left, y_left) + min(x_right, y_right)) / 2


os.system("clear")

# x = [23, 26, 31, 35]
# y = [3, 5, 7, 9, 11, 16]
# s = Solution()
# print(s.findMedianSortedArrays(x, y))

# nums1 = [0, 1, 2, 3, 4, 5, 6, 9, 10]
# nums2 = [7, 8]
# s = Solution()
# print(s.findMedianSortedArrays(nums1, nums2))

# nums1 = [2, 3, 4, 5, 6, 7, 8, 9, 10]
# nums2 = [0, 1]
# s = Solution()
# print(s.findMedianSortedArrays(nums1, nums2))

nums1 = [1, 3]
nums2 = [2]
# return 2
s = Solution()
print(s.findMedianSortedArrays(nums1, nums2))

nums1 = [1, 2]
nums2 = [3, 4]
# reutrn 2.5
s = Solution()
print(s.findMedianSortedArrays(nums1, nums2))

nums1 = [3, 4]
nums2 = [1, 2]
# reutrn 2.5
s = Solution()
print(s.findMedianSortedArrays(nums1, nums2))

nums1 = []
nums2 = [1]

s = Solution()
print(s.findMedianSortedArrays(nums1, nums2))
