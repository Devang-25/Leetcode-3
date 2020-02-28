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
