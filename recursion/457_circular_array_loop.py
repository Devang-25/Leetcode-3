"""
要求：
Time complexity: O(N)
Sapce Complexity: O(1)

解法：

- 存一个cache
"""
class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def recursion(i, count, direction):
            if nums[i] is not int:
                if nums[i] == direction:
                    if count > 1:
                        return True
                    else:
                        return False
                elif nums[i] != direction:
                    return False
            if nums[i] is int:
                cur_direction = "+" if nums[i] > 0 else "-"
                nums[i] = cur_direction
                if cur_direction == direction:
                    recursion(i+nums[i], count+1, direction)
                elif cur_direction != direction:
                    recursion(i+nums[i], count=1, cur_direction)

        return recursion(0, 0, "+")



[2, -1, 1, 2, 2]

"""
iter0:
recursion(0, 0, +)

iter1:
#0: 2
direction = +
[+, -1, 1, 2, 2]
next_place = 0+2=2
recursion(2, 1, +)

iter 2:
#2: 1
direction = +
cur_direction = +
[+, -1, +, 2, 2]
next_place = i + 1 = 2+1 = 3
recursion(3, 2, +)

iter 3:
#3: 2
direction = +
cur_direction = +
next_place = i + nums[i] = 3 + 2 = 5
add:
5 % len(list) -- 5 % 5 = 0
next_place = 0
recursion(0, 3, +)

iter 4:
#0: +
since num[0] is not int:
since num[0] is "+" == direction("+")
since count 3 > 1:
so return True



===========

[-1, 2]

iter 0:
recursion(i=0, count=0, direction = "+")

iter 1:
#0: -1
direction "+" != cur_direction "-":
so count = 1
next_place = (0-1) % len(list) = -1 % 2 = -1
next_place = len(list) - 1= 2 -1 = 1
["-", 2]
recursion(1, 1, "-")

iter 2:
#1: 2
direction = "-"
cur_direction = "+"
since cur_Diction != direction:
count = 1
next_place = (1 + 2) % len(list) = 3 % 2 = 1
["-", "+"]
recursion(1, 1, "+")

iter 3:
#1: 2
nums[1] is NOT int:
direction == cur_direction
count is NOT > 1:
return False
"""
