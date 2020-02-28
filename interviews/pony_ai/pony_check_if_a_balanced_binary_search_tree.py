"""
题目： 给一个先序遍历(pre-order: root, left, right)的输出，问这个树是不是binary search tree的

思路：
- 先序遍历的第一个值是root的输出，
- 接下来第一个大于root数的位置是右儿子，
- 那么就可以切成左子树和右子树
- 一个序列合法的情况是：左子树合法，右子树合法，且右子树每一个数都大于root

时间复杂度O(NlogN)，当时和面试官就主定理讨论了一下这个，但是没有仔细算，应该是T(n) = n + 2T(n/2)这样？

解法：
- user recursion:
    - pass in a root/node:
    - check if left child a balanced binary search tree
    - check if right child a balanced binary search tree
    - if both left and right return True
    - return True
- so for root, I find left child section and right (first number bigger than root) , pass left and right into recursion

- for the idea of balanced:
    - i need to keep track of the tree level
    - so maybe i should pass argument level into the recurvsion
    - each time it pass the level back


def recursion([left/right children], level=i):
    parent = children[0]
    if children[1] < parent:
        left_child = children[1]
    for i, num in enumerate(children[1:], 1):
        if num >= root:
            right_child = children[i]
            break
    if left_child:
        left = children[1: i]
        check_left, left_level = recursion(left, i+1)
    if right_child:
        right = children[i:]
        check_right, right_level = recursion(right, i+1)

    return True/False, level
"""


class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        def check_node(index):
            """
            index tyep: int. It is the current index of preorder list item I am trying to process
            return type: int
                - if return -1: means this preorder list is NOT a binary search tree
                - else return index, which is the maximum number of item this tree can fit according to the item I have travesed so far

            Overal method:
            - 每次返回的是下一个需要处理的item的index

            如果我走动一个是“#”， 说明，从它开始往下没有下一层了，已经在leaf了, 那就返回下一个处理的item的index。
            如果我走到的一个数字的话，说明下还没有走到leaf, 下面还有东西(下一层的东西可以是数字或者"#")：
                - 我把下一个需要处理的item的index放进check_node的recursion function中去检查（先放左边的树)
                - 左边和右边都放满了后，如果返回来的index是等于preorder list的长度的话，那就是一个binary tree.否则则不是binary tree.

            """
            if index >= len(preorder):
                # print("index", index)
                return -1

            if preorder[index] == "#":
                return index + 1 # 如果#， 就是没有东西，返回上层

            if cur_val != "#":
                # check left
                index = check_node(index + 1)
                # print("left finish", index-1, preorder[index-1])
                if index != -1:
                    index = check_node(index)
                    # print("right finish", index-1, preorder[index-1])

            return index

        preorder = preorder.split(",")
        # print(preorder)
        # index = check_node(0)
        # return index == len(preorder)
        return check_node(0) == len(preorder)


############ Check if a bineary SEARCH  Tree ########

class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        def check_node(index):
            """
            index tyep: int. It is the current index of preorder list item I am trying to process
            return type: int
                - if return -1: means this preorder list is NOT a binary search tree
                - else return index, which is the maximum number of item this tree can fit according to the item I have travesed so far

            Overal method:
            - 每次返回的是下一个需要处理的item的index

            如果我走动一个是“#”， 说明，从它开始往下没有下一层了，已经在leaf了, 那就返回下一个处理的item的index。
            如果我走到的一个数字的话，说明下还没有走到leaf, 下面还有东西(下一层的东西可以是数字或者"#")：
                - 我把下一个需要处理的item的index放进check_node的recursion function中去检查（先放左边的树)
                - 左边和右边都放满了后，如果返回来的index是等于preorder list的长度的话，那就是一个binary tree.否则则不是binary tree.

            """
            if index >= len(preorder):
                # print("index", index)
                return -1

            if preorder[index] == "#":
                return index + 1 # 如果#， 就是没有东西，返回上层

            if cur_val != "#":
                # check left
                index = check_node(index + 1)
                # print("left finish", index-1, preorder[index-1])
                if index != -1:
                    index = check_node(index)
                    # print("right finish", index-1, preorder[index-1])

            return index

        preorder = preorder.split(",")
        # print(preorder)
        # index = check_node(0)
        # return index == len(preorder)
        return check_node(0) == len(preorder)





############### Test Case ###############

nodes_list1 = "9,3,4,#,#,1,#,#,2,#,6,#,#" #return True
nodes_list2 = "1,#" # return False
nodes_list3 = "9,#,#,1" # return False

s = CheckBalancedBinarySearchTree()
s.check_binary_search_tree(nodes_list)



###################    leetcode 255 verify preorder sequence of binary search tree ################

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


########################

class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        def check_validity(index, left_bound, right_bound, depth):
            """
            return next_index: int
            next_index is the next index of the item to to process
            """
            if index >= len(preorder):
                return index, depth

            if left_bound < preorder[index] < right_bound:
                next_index, left_depth = check_validity(index+1, left_bound, preorder[index], depth+1)
                next_index, right_depth = check_validity(next_index, preorder[index], right_bound, depth+1)
                if abs(left_depth - right_depth) > 1:
                  return next_index, -1
                return next_index, max(left_depth, right_depth)
            return index, depth

        index, depth = check_validity(0, -float("inf"), float("inf"), 0)
        print("index", index, "depth", depth)
        return (index == len(preorder)) and (depth != -1)


list1 = [5,2,6,1,3] # False
list2 = [5,2,1,3,6] # True
list3 = [5,2,1,3,4,6] # False

s = Solution()
# print(s.verifyPreorder(list1))
# print(s.verifyPreorder(list2))
print(s.verifyPreorder(list3))
