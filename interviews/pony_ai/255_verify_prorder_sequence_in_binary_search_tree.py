"""
解题思路：
- use index to keep track of where I am in the List

- for every ele, it's position
"""

class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        def recursion(i, left, right):
            # i += 1
            # 用现在的数字跟boundary 比较：
            # 如果在boundary之间：那就对切成两段的boundary:
            # 形成两个新的boundary: - inf - 5; 5 ~ inf
            #

            # i += 2
            # i+=1: 在左半边的boundary
            # 因此： #1 可以去左下方
            # 再形成两个boundary: -inf ~ 2; 2 - 5

            # i+= 3: 1
            # 1在左半边的boundary里面: -inf ~ 2
            # 所有又形成两个boundary: -inf ~ 1; 1 ~ 2

            # i += 4; 3
            # 3 不在左半边的boundary里面
            # 3 也不在又半边的boundary里面： 1 ~ 2
            # 所以3不能放在#3 （#4-1)的下面：它需要返回上次
            # 需要return 什么？
            #去到上一层的 2-5： okay

            # 重点：return the index_i that is waiting to be process

            if i >= len(preorder):
                return i

            cur = preorder[i]
            if cur > left and cur < right:
                # if cur node is in between the boundary
                # put the next ele into recursion to see
                # if next ele can be fit into the lower left side of cur
                next_i = recursion(i+1, left, cur)
                next_i = recursion(next_i, cur, right)
                return next_i
            else:
                return i

        last_i = recursion(0, -float("inf"), float("inf"))
        return (last_i == len(preorder))
