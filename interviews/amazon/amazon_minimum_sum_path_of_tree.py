"""
### Q1: Mininum Sum of BST

BST那道题，root到leaves是到最后一个leave的完整路径还是root到BST中的任意一个leave，返回root到所有leave中的minimum sum.

注意1：对的就是这样子的。但是**有坑**，题目中**给的类型和代码里的返回值不一样**。我最后都没有找出问题。|| cycle list跟ListNode没关系，题目自定义了一个CNode，用这个就行了

类似题目：Minimum Sum Path http://csegeek.com/csegeek/view/tutorials/algorithms/trees/tree_part5.php

https://leetcode.com/problems/path-sum-ii/

Given a binary tree:

     1
   /   \
 -5     11
 / \   /  \
1   2 4    -2

return the path with minimum sum
"""

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


class MinimumSumPath:
  # def __init__(self):
  #   self.min_path = []
  #   self.min_sum = float("-inf")

  def find_min_sum(self, node):
    """
    input node: a treenode
    return total: the mininum sum of the this subtree
    return path: the path with minimum sum of this subtree
    """
    if not node:
      return []

    left_min_route = self.find_min_sum(node.left)

    left_sum = sum(left_min_route)

    right_min_route = self.find_min_sum(node.right)

    right_sum = sum(right_min_route)

    return left_min_route + [node.val] if left_sum < right_sum else right_min_route + [node.val]


a = Node(3)
b = Node(-12)
c = Node(14)

a.left = b
a.right = c

print(MinimumSumPath().find_min_sum(a))
