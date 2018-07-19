class Solution(object):
    def rob(self, nums):
    """
    :type nums: list[int]
    :rtype: int
    """

    pretotal = total = 0

    for num in nums:
      total, pretotal = max(pretotal + num, total)), total
    return total

test1 = [] # 0
test2 = [1, 2, 3] # return 4
test3 = [1, 3, 2, 1] # return 4
print(solution().rob(test1))
print(solution().rob(test2))
print(solution().rob(test3))
