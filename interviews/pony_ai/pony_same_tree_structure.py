  """
1. 判断两颗二叉树是不是同构的。同构的定义是，每个随意左右儿子交换，他们最终能变成一样的树结构，则这两个树就是同构的
    follow-up1：多叉树
    follow-up2：无根树-baidu 1point3acres
    被打爆了....这题太难了，最后就是口胡了一下，没写代码
    思路大致是：归一化+hash，

解法：
设计一种hash使得同构的树的hash值相同，那么这个hash函数（假设已经存在，并且是由左右儿子的hash值计算得到的）一定要符合交换律（因为左右儿子随机交换不会影响hash值）
同构归一化，比如，hash值大的放到右边，hash值小的放到左边，然后就可以避免交换律....

Implementation Detail:
- 我需要一层一层的检查树，因此我需要travel by level
- to travel by level: 我需要一个stack/list to store next_level to travel nodes


solution:
https://www.geeksforgeeks.org/tree-isomorphism-problem/
"""


############### Final Solution ###########

Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if not root1 and not root2:
            return True

        if root1 is None or root2 is None:
            return False

        if root1.val != root2.val:
            return False

        return (
          self.flipEquiv(root1.left, root2.left) and
          self.flipEquiv(root1.right, root2.right)
        ) or \
        (
          self.flipEquiv(root1.left, root2.right) and
          self.flipEquiv(root1.right, root2.left)
        )

############### my own solution version 1 ##########


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class TreeStructure:
    def process_cur_level(self, cur_level):
        """
        for node in the current level:
            - append its value into cur_val
            - append its children (left and right) into next_level
        return cur_val: the value at current level for this tree
        return next_val: the nodes (children of nodes at cur_level) I want to travel at next level

        # for children nodes of each node: always store the bigger value first.
        """
        cur_val = []
        next_level = []
        while cur_level:
            node = cur_level.pop()
            if not node:
                cur_val.append("None")
                print("None")
            else:
                cur_val.append(node.val)
                print("cur_node", node.val)
                if node.left and node.right:
                    l = node.left.val
                    r = node.right.val
                    if l >= r:
                        print("l: l >= r")
                        next_level += [node.left, node.right]
                    else:
                        next_level += [node.right, node.left]
                elif node.left:
                    next_level += [node.left, None]
                elif node.right:
                    next_level += [node.right, None]
        for node in next_level:
            if node is None:
                print("None")
            else:
                print(node.val)
        return (cur_val, next_level)

    def if_same(self, root1, root2):
        """
        purpose: see if two tree have the same structure
        input tree1: a Node structure
        input tree2: a Node structure
        return bool
        """
        l_cur = [root1]
        r_cur = [root2]
        while l_cur or r_cur:
            l_val, l_next = self.process_cur_level(l_cur)
            r_val, r_next = self.process_cur_level(r_cur)
            if l_val == r_val:
                l_cur = l_next
                r_cur = r_next
            else:
                return False
        return True



############## Test Case ################

# # test case 1
# a = Node(1)
# b = Node(2)
# c = Node(3)
#
# d = Node(4)
# e = Node(5)
#
# f = Node(6)
# g = Node(7)
#
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.left = f
# c.right = g
#
# a2 = Node(1)
# b2 = Node(3)
# c2 = Node(2)
#
# d2 = Node(7)
# e2 = Node(6)
#
# f2 = Node(5)
# g2 = Node(4)
#
# a2.left = b2
# a2.right = c2
# b2.left = d2
# b2.right = e2
# c2.left = f2
# c2.right = g2

########################


# # test case 2
#
# a = Node(1)
# b = Node(2)
# # c = Node(3)
#
# d = Node(4)
# e = Node(5)
#
# # f = Node(6)
# # g = Node(7)
#
# a.left = b
# # a.right = c
# b.left = d
# b.right = e
# # c.left = f
# # c.right = g
#
# a2 = Node(1)
# # b2 = Node(3)
# c2 = Node(2)
#
# # d2 = Node(7)
# # e2 = Node(6)
#
# f2 = Node(5)
# g2 = Node(4)
#
# # a2.left = b2
# a2.right = c2
# # b2.left = d2
# # b2.right = e2
# c2.left = f2
# c2.right = g2


########################


# # test case 3

# a = Node(1)
# b = Node(2)
# c = Node(3)

# d = Node(4)
# e = Node(5)

# # f = Node(6)
# # g = Node(7)

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# # c.left = f
# # c.right = g

# a2 = Node(1)
# b2 = Node(3)
# c2 = Node(2)

# # d2 = Node(7)
# # e2 = Node(6)

# f2 = Node(5)
# g2 = Node(4)

# a2.left = b2
# a2.right = c2
# b2.left = f2
# b2.right = g2

# # return False

#####################

# # test case 4
#
# a = Node(1)
# b = Node(2)
# c = Node(3)
#
# d = Node(4)
# e = Node(5)
#
#
# a.left = b
# a.right = c
#
# b.left = d
#
# c.right = e
#
# a2 = Node(1)
# b2 = Node(3)
# c2 = Node(2)
#
# f2 = Node(5)
# g2 = Node(4)
#
# a2.left = b2
# a2.right = c2
#
# b2.left = f2
# c2.right = g2

## return True

##################################

# test case 5

a = Node(1)
b = Node(2)
c = Node(3)

d = Node(4)
e = Node(5)


a.left = b
a.right = c

b.left = d

c.right = e

a2 = Node(1)
b2 = Node(3)
c2 = Node(2)

f2 = Node(5)
g2 = Node(4)

a2.left = b2
a2.right = c2

b2.left = g2
c2.right = f2

# return False


ts = TreeStructure()
print(ts.if_same(a, a2))
print("Finished")
