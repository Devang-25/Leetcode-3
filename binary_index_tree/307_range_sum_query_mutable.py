"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.

Example:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:

The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.

----
N = # of node
Time complexity for building tree: N(logN)
time complexity to update and find sum: LogN

"""

class Node(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        def create_tree(nums, l, r):
            # base case
            if l > r:
                return None
            # leaf node
            if l == r:
                node = Node(l, r)
                node.total = nums[l]
                return node

            mid = (l + r) // 2

            # first, build this root node
            root = Node(l, r)

            # second, build the left and right nodes
            root.left = create_tree(nums, l, mid)
            root.right = create_tree(nums, mid+1, r)

            # third, update the total of root node
            root.total = root.left.total + root.right.total

            return root

        self.root = create_tree(nums, 0, len(nums)-1)


    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        # helper function
        def update_val(root, i, val):
            # base case
            if root.start == root.end:
                root.total = val
                return val

            # find the leaf node
            mid = (root.start + root.end) // 2

            if i <= mid:
                update_val(root.left, i, val)

            else:
                update_val(root.right, i, val)

            # update the root value
            root.total = root.left.total + root.right.total

            # return
            root.total

        return update_val(self.root, i, val)


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        #helper function
        def range_sum(root, i, j):
            # base case
            if root.start == i and root.end == j:
                return root.total

            # find the interval
            mid = (root.start + root.end) // 2

            if j <= mid:
                return range_sum(root.left, i, j)

            elif i >= (mid + 1):
                return range_sum(root.right, i, j)

            else:
                return range_sum(root.left, i, mid) + range_sum(root.right, mid+1, j)

        # return sum
        return range_sum(self.root, i, j)

class NumArray_2(object):
    def __init__(self, nums):
        self.update = nums.__setitem__
        self.sumRange = lambda i, j: sum(nums[i:j+1])


# Your NumArray object will be instantiated and called as such:
nums = [0, 1, 2, 3, 4, 5]
obj = NumArray(nums)
obj.update(i,val)
param_2 = obj.sumRange(i,j)
