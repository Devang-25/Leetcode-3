# Amazon Virtual Interview

## Behavior Questions:

#### introduce yourself 

#### why [Amazon](http://www.amazon.com/b?_encoding=UTF8&tag=1p3a-guanlian-20&linkCode=ur2&linkId=89c11e2c5b86155c5422f19cca1e9880&camp=1789&creative=9325&node=5); do you use any amazon product? 

#### why choose amazon product not others? for example; 

if your teammate push-back his work, how could you do?; 

if your will miss the deadline, but you didn't finish your work, what will you do? ect.



1. Describe a time when you went outside normal procedures to get a project done.
2. You are going to miss tomorrow's deadline, how do you and your team handle it?
3. Give me a detailed example of the project you have led before to help me understand more of your previous job.
4. What practical steps have you taken to elicit maximum contributions from each member of your team?
5. What is the most innovative thing that you have created?
6. In a situation where your intuition tells you there is a potential business opportunity, how do you go about finding the data necessary to substantiate it? Where do you even start?  
7. Tell us about your strengths
8. Describe a time that you exhibited leadership in your organization.
9. Tell me about a time when a decision you made didn't produce the results you wanted.
10. Tell me about a time when you disappointed a team member
11. Tell me about a time when you had to deal with a difficult customer
12. Give 3 examples of projects where you invented, simplified, delivered results quickly, and were able to scale to a larger result  
13. Tell me about a time when you proceeded to deal with an issue without your bosses OK.
14. Please tell me about a time when you had a project in trouble and how you handled it.
15. Tell me about a decision that did not go your way. How did you deal with it.
16. What was a challenge you faced during a project you worked on and how did you overcome it.
17. Describe a time you failed at work, or describe the most difficult situation you faced at work
18. When in your last job did you take a risk and fail?
19. How do you express different opinions to your manager?
20. Give me an example of when you have failed at a task, what did you do?
21. Tell me about a time when you innovated to simplify a process.
22. Talk about a project that you took with ambiguity (lack of data) and how did you proceed with the project?
23. Talk about a situation where you remotely influenced stakeholders and were able to get your work done. Explain the approach taken.
24. Talk about a project, where you had to take a difficult decision - Explain the decision, impact, reason for such decision, and how did you handle it, and the result?
25. Name a time you disagreed with your boss - how did the issue get solved?
26. How did you train one of your team members (Jr or Sr) to make him/her better in his/her daily work?
27. A time when you took a calculated risk, pushed through with it and succeeded.
28. A time when you used customer feedback to improve an aspect of your organization. 
29. A time when, halfway through a project, you encountered an incident/setback/roadblock and act to overcome it. With what result?
30. Give me 5 examples of how you are working to better yourself
31. Tell me about the most innovative thing you have ever created.
32. Name a time when you had to deal with a tough situation. Or, when you disagreed with management and what did you do.  
33. Tell me your most successful project which you led, what did you achieve at the end?    

-------------------------

## Data Strcutre

#### DIfference between Thread and Process?

**What is a process?**

**Process is an executing instance of a program.** For example, when you double click on a notepad icon on your computer, a process is started that will run the notepad program.

A process is sometimes referred as **active entity** as it resides on the primary memory and leaves the memory if the system is rebooted. Several processes may related to same program. For example, you can run multiple instances of a notepad program. Each instance is referred as a process.

**What is a thread?**

T**hread is the smallest executable unit of a process.** For example, when you run a notepad program, operating system creates a process and starts the execution of main thread of that process.

**A process can have multiple threads.** Each thread will have their own task and own path of execution in a process. For example, in a notepad program, one thread will be taking user inputs and another thread will be printing a document.

**All threads of the same process share memory of that process.** As threads of the same process share the same memory, **communication between the threads is fast.**

![image-20190402213404089](/Users/sonya/Library/Application Support/typora-user-images/image-20190402213404089.png)





## Coding

#### Find number of unique palindrome in a substring

```python
class Solution(object):

  def countSubstrings(self, s):
    """
    :type s: str
    :rtype: int
    """
    # self.matrix = [[None] * len(s) for _ in range(len(s))]
    self.results = set()

    for i in range(len(s)):
      self.if_palindrome(i, i, s)
      self.if_palindrome(i, i + 1, s)

    return len(self.results)

  def if_palindrome(self, b, e, s):
    while b >= 0 and e < len(s):
      if s[b] == s[e]:
        self.results.add(s[b:e + 1])
        b -= 1
        e += 1
      else:
        break


string = "aa"
s = Solution()
r = s.countSubstrings(string)
print("string:{}, r:{}".format(string, r))

string = ""
s = Solution()
r = s.countSubstrings(string)
print("string:{}, r:{}".format(string, r))

string = "aaa"
s = Solution()
r = s.countSubstrings(string)
print("string:{}, r:{}".format(string, r))

string = "ab"
s = Solution()
r = s.countSubstrings(string)
print("string:{}, r:{}".format(string, r))

string = "aba"
s = Solution()
r = s.countSubstrings(string)
print("string:{}, r:{}".format(string, r))

```





#### Reverse a list

```python
def reverse(nums):
  n = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}
  s = 0
  e = len(nums) - 1

  while s < e:
    if nums[s] in n and nums[e] in n:
      nums[s], nums[e] = nums[e], nums[s]
    s += 1
    e -= 1

  return nums


nums = ["1", "$", "2", "4", "7", "*", "#"]
r = reverse(nums)
print("r", r)

```



#### 给你一个iterator, iterator 动态输入 数字 比如 【1，2，0，4，5，2】； 你写个function 能够及时返回 top 3 value's sum

```python
'''
给你一个iterator, iterator 动态输入数字:比如 【1，2，0，4，5，2】； 
你写个function 能够及时返回 top 3 value's sum

- use max heap to maintain the top 3 values
- whenever there is a new number: compare it with min heap, the smallest node in min_heap
  - if new num > top node in min_heap: pop and push; update sum
  - else: pass

'''
import heapq


class Solution:

  def __init__(self, nums, k):
    self.sum = 0
    self.min_heap = []
    # def top_k_val_sum(self, nums, k):
    """
    inputs: 
      nums: [int]

      k: int. indicate the top k values we want

    return:
      self.sum: int
    """
    self.nums = nums

    for i in range(k):
      heapq.heappush(self.min_heap, self.nums[i])
      self.sum += self.nums[i]
      # print("1 sum", self.sum)

    for i in range(k, len(nums)):
      self.update(self.nums[i])
      # print("2 sum", self.get_sum())

  def get_sum(self):
    return self.sum

  def add(self, new_num):
    self.nums.append(new_num)
    self.update(new_num)
    # print("3 sum", self.get_sum())

    # return self.sum

  def update(self, new_num):
    min_val = self.min_heap[0]
    if new_num > min_val:
      heapq.heappop(self.min_heap)
      heapq.heappush(self.min_heap, new_num)
      self.sum = self.sum - min_val + new_num


nums = [1, 2, 0, 4, 5, 2]
s = Solution(nums, k=3)  #return 11
print(s.get_sum())
s.add(6)
print(s.get_sum())  # return 15
"""
Time complexity for Heappop():
O(longN), n = level of heap

time complexity for heappush():
O(LogN), n = level of heap

time complexity of update sum: 
O(1)

So, overall time complexity: O(N*Log(N))
the time complexity to add a number if O(log(N))

"""

```



#### top k freq item

```python
from collections import defaultdict
from typing import List

# O(N) solution

class Solution:

  def topKFrequent(self, nums, k):
    word_freq_cache = defaultdict(int)
    freq_word_cache = defaultdict(list)

    for num in nums:
      word_freq_cache[num] += 1

    for num, freq in word_freq_cache.items():
      freq_word_cache[freq].append(num)

    results = []
    for freq in range(len(nums), 0, -1):
      if freq in freq_word_cache:
        results += freq_word_cache[freq]

    return results[:k]


nums = [1, 1, 1, 2, 2, 3]
k = 2
s = Solution()
r = s.topKFrequent(nums, k)
# return [1, 2]
print(r)

nums = [1]
k = 1
s = Solution()
r = s.topKFrequent(nums, k)
# return [1]
print(r)

nums = []
k = 1
s = Solution()
r = s.topKFrequent(nums, k)
print(r)
# return []



###########################
# O(N*LogN) solution
class Solution:

  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    self.cache = defaultdict(int)

    for num in nums:
      self.cache[num] += 1

    # items(): (num, freq)
    sorted_tuples = sorted(self.cache.items(), key=lambda x: x[1], reverse=True)

    result = [item[0] for item in sorted_tuples[:k]]

    return result


# nums = [1, 1, 1, 2, 2, 3]
# k = 2
# s = Solution()
# r = s.topKFrequent(nums, k)
# print(r)

nums = [1]
k = 1
s = Solution()
r = s.topKFrequent(nums, k)
print(r)

nums = []
k = 1
s = Solution()
r = s.topKFrequent(nums, k)
print(r)

```



#### find non-repeating char

```python
import collections

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        cache = collections.Counter(s)
        for i, w in enumerate(s):
            if cache[w] == 1:
                return i
        return -1
```



#### Find duplicates numbers within a list

```python
"""
Coding:找出重复的数字(not sorted) 问两种解并分析两个的优缺点

input: [1,5,3,3,2,4,2]  output:[3,2] 

https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=508611&highlight=%D1%C7%C2%E9vo

"""

from collections import defaultdict


def find_duplicates(nums):
  cache = defaultdict(int)
  results = []
  for num in nums:
    cache[num] += 1  #O(1)
    if cache[num] == 2:  #O(1)
      results.append(num)
  return results


# overall O(N)


def find_duplicates2(nums):
  """
  more memory efficient
  """
  cache = set()
  results = set()
  for num in nums:
    if num in cache:  #O(1)
      results.add(num)  #O(1)
    elif num not in cache:
      cache.add(num)
  return list(results)


# overall: O(N)
```



### BST

#### Binary Tree Right Side View

```python
from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

  def rightSideView(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if not root:
      return []

    self.results = []
    cur_level = deque([root])
    self.helper(cur_level)

    return self.results

  def helper(self, cur_level):
    if not cur_level:
      return

    next_level = deque()

    print("cur", cur_level)
    node = cur_level.popleft()
    self.results.append(node.val)
    if node.right:
      next_level.append(node.right)
    if node.left:
      next_level.append(node.left)

    while cur_level:
      node = cur_level.popleft()
      if node.right:
        next_level.append(node.right)
      if node.left:
        next_level.append(node.left)

    self.helper(next_level)

```



#### Flatten binary tree to linked list

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

  def flatten(self, root):
    """
    :type root: TreeNode
    :rtype: void Do not return anything, modify root in-place instead.
    """
    self.helper(root)

  def helper(self, node):
    if not node:
      return

    if node.left:
      self.helper(node.left)

    if node.left and node.right:
      right = node.right
      node.right = node.left
      node.left = None
      while node.right:
        node = node.right
      node.right = right

      self.helper(right)

    elif node.left:
      node.right = node.left
      node.left = None

    elif node.right:
      self.helper(node.right)

    return
```



#### validate bst

```python
class TreeNode:

  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


# need to use boundary
class Solution:

  def isValidBST(self, root):
    """
    inputs:
      root: Treenode
    
    outputs:
      result: bool

    """
    return self.helper(root, float("-inf"), float("inf"))

  def helper(self, node, left_bound, right_bound):
    """
    inputs:
      node: Treenode
      left_bound: int
      right_bound: int
    
    outputs:
      result: bool

    """
    if not node:
      return True

    if node.val <= left_bound or node.val >= right_bound:
      return False

    left_valid = self.helper(node.left, left_bound, node.val)
    right_valid = self.helper(node.right, node.val, right_bound)

    if not left_valid or not right_valid:
      return False

    return True


a = TreeNode(3)
b = TreeNode(1)
c = TreeNode(4)

a.left = b
a.right = c

s = Solution()
r = s.isValidBST(a)
print("1 result", r)

#################
# a = TreeNode(None)
# s = Solution()
# r = s.isValidBST(a)
# print("2 result", r)

##########

a = TreeNode(3)
b = TreeNode(1)

a.left = b

s = Solution()
r = s.isValidBST(a)
print("3 result", r)

```

#### path with max sum from root to leaf

```python
# Definition for a binary tree node.
class TreeNode:

  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


class Solution:

  def maxPathSum(self, root):
    self.max_sum = 0
    self.max_path = []
    self.helper(root, [], 0)

    return self.max_path

  def helper(self, node, path, total):
    if not node:
      if total > self.max_sum:
        self.max_sum = total
        self.max_path = path
      return

    print("node", node.val)
    if node.left:
      print("left", node.left.val)

    if node.right:
      print("right", node.right.val)
    self.helper(node.left, path + [node.val], total + node.val)
    self.helper(node.right, path + [node.val], total + node.val)


a = TreeNode(3)
b = TreeNode(1)
c = TreeNode(4)

a.left = b
a.right = c

s = Solution()
r = s.maxPathSum(a)
print("1 result", r)

##########

# a = TreeNode(3)
# b = TreeNode(1)

# a.left = b

# s = Solution()
# r = s.maxPathSum(a)
# print("3 result", r)

```



#### If any path from root to leaf math given sum

```python
# Definition for a binary tree node.
class TreeNode:

  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


class Solution:

  def hasPathSum(self, root, sum):
    self.sum = sum
    return self.helper(root, 0)

  def helper(self, node, total):
    if not node:
      if total == self.sum:
        return True
      return False

    if total > self.sum:
      return False

    left = self.helper(node.left, total + node.val)
    right = self.helper(node.right, total + node.val)
    return (left or right)


a = TreeNode(3)
b = TreeNode(1)
c = TreeNode(2)
a.left = b
a.right = c

s = Solution()
r = s.hasPathSum(a, 4)
print("r", r)

```



#### max leaf to any node path of binary tree

```python
"""
Q: find a path from leaf to any of its parent node in the tree that it has the max sum

"""


class TreeNode:

  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


class Solution:

  def maxSumPath(self, root):
    """
    inputs:
      roots: a TreeNode object

    outputs:
      max_sum: int

    """
    self.max_sum = None
    self.helper(root)

    return self.max_sum

  def helper(self, node):
    if not node:
      return 0

    left_total = self.helper(node.left)
    right_total = self.helper(node.right)

    new_total = max(left_total, right_total) + node.val
    if not self.max_sum or new_total > self.max_sum:
      self.max_sum = new_total

    return new_total


# a = TreeNode(-1)
# b = TreeNode(1)
# c = TreeNode(4)
# a.left = b
# a.right = c

# s = Solution()
# r = s.maxSumPath(a)
# print("r", r)

###################

a = TreeNode(-1)
# b = TreeNode(1)
# c = TreeNode(4)
# a.left = b
# a.right = c

s = Solution()
r = s.maxSumPath(a)
print("r", r)
```



#### Binary Tree Maximum Path Sum

Given a **non-empty** binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain **at least one node** and does not need to go through the root.

**Example 1:**

```
Input: [1,2,3]

       1
      / \
     2   3

Output: 6
```

**Example 2:**

```
Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
```



```python
"""

124. Binary Tree Maximum Path Sum
Hard

1337

96

Favorite

Share
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42

"""


# Definition for a binary tree node.
class TreeNode:

  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


class Solution:

  def maxPathSum(self, root):
    """
      inputs:
        root: TreeNode

      outputs:
        max_sum: int

      """
    self.max_sum = None
    self.helper(root)

    return self.max_sum

  def helper(self, node):
    if not node:
      return float("-inf")

    left_max = self.helper(node.left)

    right_max = self.helper(node.right)

    # globaly max up until this points
    this_max = max(node.val, left_max, right_max, node.val + left_max,
                   node.val + right_max, node.val + left_max + right_max)

    if not self.max_sum or this_max > self.max_sum:
      self.max_sum = this_max

    # max WITH cur node
    max_with_node = max(node.val, node.val + left_max, node.val + right_max)

    return max_with_node


a = TreeNode(-1)

s = Solution()
r = s.maxPathSum(a)
assert r == -1
print("r", r)

##################

a = TreeNode(-1)
b = TreeNode(2)
c = TreeNode(3)
a.left = b
a.right = c

s = Solution()
r = s.maxPathSum(a)
assert r == 4
# 2 + -1 + 3 = 4
print("r", r)

##################

a = TreeNode(-1)
b = TreeNode(-2)
c = TreeNode(3)
a.left = b
a.right = c

s = Solution()
r = s.maxPathSum(a)
assert r == 3
# path = [3]
print("r", r)

##############

a = TreeNode(-1)
b = TreeNode(-2)
c = TreeNode(3)
d = TreeNode(4)
a.left = b
a.right = c
c.right = d

s = Solution()
r = s.maxPathSum(a)
assert r == 7
print("r", r)

```



#### Print bst from root to leaf

```python
"""
257. Binary Tree Paths
Easy

794

63

Favorite

Share
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

  def binaryTreePaths(self, root):
    """
    :type root: TreeNode
    :rtype: List[str]
    """

    if not root:
      return []

    self.paths = []
    self.results = []

    self.travel(root, [])

    # ["1->2->5","1->3"]
    for path in self.paths:
      path = "->".join(path)
      self.results.append(path)

    return self.results

  def travel(self, node, path):
    """
    inputs: 
      nodes: TreeNode object
      path: List[int]
    
    outputs:
      None
    """
    if not node.left and not node.right:
      self.paths.append(path + [str(node.val)])
      return

    if node.left:
      self.travel(node.left, path + [str(node.val)])
      # self.travel(node.left, path + "->" + str(node.val))

    if node.right:
      self.travel(node.right, path + [str(node.val)])
      # self.travel(node.right, path + "->" + str(node.val))

```



#### if same tree

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

  def isSameTree(self, p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    
    idea: check level by level
    recursively check each of their node and their children
    """
    if not p and not q:
        return True
    
    if (not p and q) or (p and not q):
        return False
        
    if p and q:
      if p.val != q.val:
        return False

      if p.val == q.val:
        left_same = self.isSameTree(p.left, q.left)
        right_same = self.isSameTree(p.right, q.right)
        return left_same and right_same

```



####  Merge Two linked List

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp_head = ListNode(0)
        pre = temp_head
        while l1 and l2:
            if l1.val < l2.val:
                pre.next = l1
                l1 = l1.next
            else:
                pre.next = l2
                l2 = l2.next
            pre = pre.next
        if l1:
            pre.next = l1
        else:
            pre.next = l2
        return temp_head.next

```





### Other

#### frog jump



```python
"""
Time Complexity: O(N) , where n = length of stones

"""

from collections import defaultdict


class Solution:
  # def __init__(self):
  #   self.visited = defaultdict(list) # {position: [speed]}

  def canCross(self, stones):
    # self.visited = defaultdict(list)
    self.visited = set()  # set(tuple(pos, speed))
    self.destination = stones[-1]
    self.stones = set(stones)

    return self.find_next_steps([0], [1])

  def find_next_steps(self, cur_positions, cur_speeds):
    if cur_positions and cur_speeds:
      next_positions = []
      next_speeds = []
      assert len(cur_positions) == len(cur_speeds)
      for i in range(len(cur_positions)):
        cur_pos = cur_positions[i]
        cur_speed = cur_speeds[i]
        if cur_pos == 0 and cur_speed == 1:
          speeds = [1]
        else:
          speeds = [cur_speed - 1, cur_speed, cur_speed + 1]
        # note: speed cannot be 0 or negative

        for s in speeds:
          if s > 0:
            next_pos = cur_pos + s
            if next_pos in self.stones:
              if (next_pos, s) not in self.visited:
                next_positions.append(next_pos)
                next_speeds.append(s)
                self.visited.add((next_pos, s))

      if self.arrived(next_positions):
        return True
      if not next_positions and not next_speeds:
        return False
      else:
        return self.find_next_steps(next_positions, next_speeds)

  def arrived(self, next_positions):
    if self.destination in next_positions:
      return True
    return False


stones = [0, 1, 3, 5, 6, 8, 12, 17]
s = Solution()
r = s.canCross(stones)
print("stones:{}, r:{}".format(stones, r))

stones = [0, 1, 2, 3, 4, 8, 9, 11]
s = Solution()
r = s.canCross(stones)
print("stones:{}, r:{}".format(stones, r))

stones = [0, 2]
s = Solution()
r = s.canCross(stones)
print("stones:{}, r:{}".format(stones, r))

stones = [0, 1]
s = Solution()
r = s.canCross(stones)
print("stones:{}, r:{}".format(stones, r))

```



#### Find all words that started with certain patter

给你一堆string，找所有start with pattern的string，pattern是一个string input，先问可以用什么数据结构，答trie tree，写了一个trie node class
https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=506047&highlight=%D1%C7%C2%E9Vo

```python
import re

re.findall(pattern, text)
re.findall(r"patter\w*", text, flags=re.IGNORECASE)

######### Example ######

import re
text = ["apple", "app", "apod", "boring"]
text = "apple, app, apod, boring"
r = re.findall(r"ap\w*", text, flags=re.IGNORECASE)
print(r)
```



#### Find  word that one more character than s

```python
"""
如果给你一个string s，s misses exactly one character，不知道missing character的位置，只知道一定少了一个character，问给的所有string里有没有符合的要求的string

# find all words with one more letters in length than s

# make s in to counter:
  # for each word: 

"""

def find_word(s, words):
  for w in words:
    if len(s) != len(w) - 1:
      continue
    i = 0
    j = 0
    while i < len(s) - 1 and j < len(w) - 1:
      if s[i] == w[j]:
        i += 1
        j += 1
      elif s[i] != w[j]:
        j += 1
        if s[i:] == w[j:]:
          return True
  return False

s = "apple"
words = ["app", "applee", "bapple"]
r = find_word(s, words)
print(r)
```



#### Find all combination of two strings while maintain order

```python
"""
https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=504192&highlight=%D1%C7%C2%E9%2Bvo

给两个string, 要求保证每个string内部相对顺序不变的情况下，输出所有可能的组合.
比如 s1 = “AB”  s2 = “CD” 输出ABCD ACBD ACDB CABD CADB CDAB

fn(s1, s2) = [s1[0] + tail for tail in fn(s1[1:], s2)] +
             [s2[0] + tail for tail in fn(s1, s2[1:])] +
"""


def all_combinations(s1, s2):

  # print('s1:{}, s2:{}'.format(s1, s2))
  """
  inputs:
    t1: List[str]
    t2: List[str]
  outputs:
    r: List[str]

  """
  # print("\n")
  # print("t1:{}, t2:{}".format(t1, t2))

  if not s1:
    return [s2]

  if not s2:
    return [s1]

  l = all_combinations(s1[1:], s2)
  left = [s1[0] + s for s in l]
  # print("l:{}, t1:{}, left:{}".format(l, t1[0], left))

  r = all_combinations(s1, s2[1:])
  right = [s2[0] + s for s in r]
  # print("r:{}, t2:{}, right:{}".format(r, t2[0], right))

  return left + right


######## test case 1 ######
s1 = "AB"
s2 = ""
# AB

r = all_combinations(s1, s2)
print("r", r)

######## test case 2 ######
s1 = "A"
s2 = "C"
# AC, CA

r = all_combinations(s1, s2)
print("r", r)

######## test case 3 ######

s1 = "AB"
s2 = "CD"

r = all_combinations(s1, s2)
print("r", r)
# ABCD ACBD ACDB CABD CADB CDAB
```



####  Swap to balance scores for two teams

```python
"""
https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=506802&highlight=%D1%C7%C2%E9Vo

给两个team数组，数组元素是team player 的分数。问如何swap两队的队员使得两队分数最balance（队员分数和相差最小）。

"""


class Solution:

  def balance(self, team1, team2):
    """
    inputs:
      team1: list[int]
      team2: list[int]
    
    outputs:
      team1: list[int]
      team2: list[int]
    """
    
    # sort tema1 and team2 together:
    self.nums = team1 + team2
    self.nums.sort()

    self.diff = sum(self.nums)

    # do binary search 


    return self.team1, self.team2

  def gap(self, i, j):
    team1 = sum(self.team1) - self.team1[i] + self.team2[j]
    team2 = sum(self.team2) - self.team2[j] + self.team1[i]
    return abs(team1 - team2)

  def swap(self, i, j):
    self.team1[i], self.team2[j] = self.team2[j], self.team1[i]


team1 = [2, 3]
team2 = [4, 6]
total = 5 + 10 = 15 
15/ 2 = 7
15 - 7 = 8
"""
goal:
team1: [2, 6]
team2: [3, 4]


t1: [2, 3]
t2: [4, 6]
diff = 10 - 5 = 5

swap: i = 0, j = 1
t1 = [6, 3]
t2 [4, 2]
diff = 9 - 6 = 3


# return:
# team1[2, 6]
# team2[3, 4]


```



#### Find a num in a list the appear prime times

```python
"""
给一个Array, 里面有一个元素出现了奇数次，其他的都出现了偶数次，求出现奇数次的数字，不能用位操作。

"""

from collections import Counter


def find_prime(nums):
  counter = Counter(nums)

  for num, times in counter.items():
    if times == 2:
      return num
    if times % 2 == 0:
      continue
    for n in range(3, times, 2):
      if times % n == 0:
        continue
    return num
  return []


nums = [1, 1, 1, 1, 2, 2, 3, 3, 3, 3]
r = find_prime(nums)
print("r", r)
```



#### Find Two sums

<https://leetcode.com/problems/two-sum/>

Given an array of integers, return **indices** of the two numbers such that they add up to a specific target.

You may assume that each input would have **exactly** one solution, and you may not use the *same* element twice.

**Example:**

```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```

```python
class Solution(object):

  def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    d = {}  # {value: index}

    for i, n in enumerate(nums):
      m = target - n
      if m in d:
        return [d[m], i]
      else:
        d[n] = i
        
```



#### Find Two Sum Data Structure

170. Two Sum III - Data structure design

<https://leetcode.com/problems/two-sum-iii-data-structure-design/>

Design and implement a TwoSum class. It should support the following operations: `add` and `find`.

`add` - Add the number to an internal data structure.
`find` - Find if there exists any pair of numbers which sum is equal to the value.

**Example 1:**

```
add(1); add(3); add(5);
find(4) -> true
find(7) -> false
```

**Example 2:**

```
add(3); add(1); add(2);
find(3) -> true
find(6) -> false
```

```python
class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: None
        """
        if number in self.d:
            self.d[number] += 1
        else:
            self.d[number] = 1

    def find(self, value):
        # print("find", value)
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for n in self.d:
            if value - n in self.d and (n != value - n or self.d[value - n] > 1):
                    return True
        return False
```



####  Two Sum Input Array Sorted

```python
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.numbers = numbers
        for i, n in enumerate(numbers):
            m = target - n
            if m == n and numbers[i+1] == n:
                return (i+1, i + 2)
            elif m == n and number[i-1] == n:
                return (i, i+1)
            elif m < n:
                find = self.binary_search(m, 0, i-1)
            elif m > n:
                # print("m > n")
                find = self.binary_search(m, i+1, len(numbers)-1)
            if find:
                return sorted([i+1, find+1])
        return []
            
    def binary_search(self, m, s, e):
        if s > e:
            return False
        
        mid = (s + e) // 2
        # print("s{}, e{}, mid{}, val{}".format(s, e, mid, self.numbers[mid]))
        
        if self.numbers[mid] == m:
            return mid
    
        elif self.numbers[mid] > m:
            return self.binary_search(m, s, mid-1)
        
        elif self.numbers[mid] < m:
            return self.binary_search(m, mid+1, e)
        
        
```

#### implement a stack using queue

```python
from collections import deque
# Pop from queue: deque.popleft()
# append to the queue: deque.append()
# Initialize: queue = deque()
"""
stack:
- first in, last out
"""


class Stack:

  def __init__(self):
    self.stackleft = deque()
    self.stackright = deque()

  def append(self, item):
    if not self.stackleft:
      self.stackleft.append(item)
      while self.stackright:
        i = self.stackright.popleft()
        self.stackleft.append(i)

    elif not self.stackright:
      self.stackright.append(item)
      while self.stackleft:
        i = self.stackleft.popleft()
        self.stackright.append(i)

  def pop(self):
    if self.stackleft:
      return self.stackleft.popleft()
    elif self.stackright:
      return self.stackright.popleft()

  def _show(self):
    print("left", self.stackleft)
    print("right", self.stackright)


s = Stack()
s.append(0)

s.append(1)

s._show()

s.pop()
s._show()

s.append(2)
print("\n")
s._show()
"""0: add 0
left: 0
right: 


1: add 1
right: 1
left pop: 0

right: 1, 0
left:

2: pop
right.pop() -> pop out 1

right: 0
left:

3: add 2
left: 2
while right:
  right.pop() -> 0
  left.add(0) ->

left: 2, 0
right:

4: pop
left.pop() -> pop 2"""

```



#### integer to english word

```python
def __init__(self):
    self.lessThan20 = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
    self.tens = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
    self.thousands = ["","Thousand","Million","Billion"]

def numberToWords(self, num):
    if num == 0:
        return "Zero"
    res = ""
    for i in range(len(self.thousands)):
        if num % 1000 != 0:
            res = self.helper(num%1000) + self.thousands[i] + " " + res
        num /= 1000
    return res.strip()

def helper(self, num):
    if num == 0:
        return ""
    elif num < 20:
        return self.lessThan20[num] + " "
    elif num < 100:
        return self.tens[num/10] + " " + self.helper(num%10)
    else:
        return self.lessThan20[num/100] + " Hundred " + self.helper(num%100)
```



#### 巧克力工厂



#### 给一个数，判断能不能写成6，9，20的和。

先暴力递归，问你复杂度。

第一次优化：记忆化，问你复杂度。这里我用的是C++的vector，然后他问我，你用了vector内存是不是有点浪费啊？如果还是用记忆化，但是省点内存，咋整捏？答案 -- HashMap (Unordered map)

第二次优化，dp，问你复杂度。

---------



## 基础代码知识：

### OOP

#### VO一道题，Word search，考了**OOP基础多态**。

https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=499581



#### Inheritance和composition什么区别？

感觉就是记感念，对我来说，过段时间概念会忘，所以面试前一天拿出来看。

https://www.1point3acres.com/bbs/thread-306707-1-1.html



### data structure & algorithm

#### Array和linked list有什么区别？

#### HashMap和TreeMap有什么区别？

#### quick sort和heap sort有什么区别？







## Behavior Questions

### Great Answers:

1. act diplomatic
2. stand up for what you believe is good  for the company and customers
3. advocate



### Avoids:

1. never disagree with  anyone
2. challenge things even after a final decision has been made
3. refuse to change direction of a project  becuase of ego



### Dive Deep:

1. Operate at all levels
2. stay connected to details
3. audit frequently
4. be skeptical when metrics and anedote differ
5. No task is beneath you



### Evaluate work:

Great Answers:

1. stay connected to details & emphasize systmes thinking
2. talk metrics, relevant ones
3. asks the right questions
4. tackle hard problems, immediately



Avoid:

1. talk vaguely
2. lack of energy



## Frugality

1. accompolish more with less
2. constrains breed resourcefulness, self-sufficiency and invention. 
3. There are no extra points for growing headcount, budget size or fixed expenses.









------

# 2019/1/12 bq + code

- Tell me about yourself.
- How did you manage to learn all the new technologies
- When will you choose technology/tool x over technology/tool y
- Tell me about a time when you took on something significant outside your area of responsibility.
- What did you do when your teammate said he needs help



LRU 变形。
Top K Elements。





--------

## 2018/10 bq + code

bq： 有没有遇到过需要赶deadline 的project 怎么处理的 ：答： 有，期末project， reprioritize tasks 然后produce working product
bq： 现在的学习目标或者工作目标： 答： 多学点技术，准备工作 掌握基础知识， 之后打算自己想搞开发，研究新商业模式
bq： 说一个你具体的project： 之前有工作半年， 所以扔了一个网址给面试官看， 然后带他走了遍当时用的technology，面试官说thanks for sharing， 然后就没深究 



Leetcode： 找岛屿数量





------



第一轮印度小哥， 上来先自我介绍了一下， 给我一分钟自我介绍， 然后上题， 题目是**LRU变种**， bq问了一个

https://leetcode.com/problems/lru-cache/



第二轮是白人小哥， 也是上来自我介绍了一下， aws security的； 基本上都是简单的**数据结构问题**；

问的**input file unique line countting**的问题， follow up问了如果**文件很大**怎么办；



Input file unique line counting:

https://stackoverflow.com/questions/6712437/find-duplicate-lines-in-a-file-and-count-how-many-time-each-line-was-duplicated

```python
sort <file> | uniq --count
```





 最后**implement一个Trie Tree**

implement Trie:

https://leetcode.com/problems/implement-trie-prefix-tree/



第三面两轮烙印， 问了很久的**bq**问题； 主要和简历有关； 最后问**了two sum的变种**，就是包含**重复的情况**。 楼主coding没有答好， 感觉是要凉凉了；



https://leetcode.com/problems/two-sum/

https://leetcode.com/problems/3sum/

https://leetcode.com/problems/4sum/submissions/



------



第二部分是考察数据结构相关知识，先问了我BST，然后问我Hashtable，最后问了Tree的几种traverse，然后写了下基本的代码



第三部分是coding，先做了一道类似DFS的题，是在一个image（2d array）上选择一个点，然后遇到0就把0变成1，遇到1就停止。复杂度是多少？



简单写一写，设计一个social 软件的api系统，要怎么写。

大概的思路和需要的东西。

类似如果是一个像facebook或者其他社交app里面，**用户很多，该怎么办**？



-----

## 2019/3/15

Bq:

bq问了项目中和**队友合作遇到大困难**？

**自己研究问题特别deep的经历**，因为转专业项目经历很少所以还说了不少以前的经历。



code:

一个相连岛屿的coding



--------

## 2019/3

code题：

初始化一个扫雷的棋盘， 输入是棋盘大小，以及想要放置的地雷数量，输出是一个棋盘数组，每个值是该cell周边所有的地雷数，或者是地雷
用循环初始化所有节点搞定，现在突然想到最优解应该是loop地雷数，把地雷random地放置到棋盘上就完成了；当场问我，没想到这个优化解



System design考了怎么去设计交通路灯，放了几个class，流程应该能走通

2. 白人小哥，主要谈了一个系统设计，如何设计[kindle](http://amzn.to/2PcJxHB)的subscript
3. 一个很精力充沛的白人小哥：code题，**一个word list，一个character list，找出word数组的一个subset能够最多地使用character**
   我先PFS所有subset，然后计算所有subset使用的character数量，告诉我有更优解，当场没想出来，现在也在仔细想
4. 给一个string，再给一个指令集，生成xml ，比如【1，5，B】，要求在第一个字符前加<B>,第五个字符后加</B>
   用时间线做掉

https://www.1point3acres.com/bbs/thread-498873-1-1.html



------

## 2019/3

BQ好多都忘了问一些什么问题了，大部分是根据我讲的project，然后问一些项目实现上的具体问题。
1. tight ddl
2. risk
3. 另外还学了些什么新知识
4. 自己做决定



----

## 2019/3

Code:

BST寻找next smallest

https://leetcode.com/problems/kth-smallest-element-in-a-bst/



```python
"""
30. Kth Smallest Element in a BST
Medium

988

39

Favorite

Share
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# inorder traveral: left root right


class Solution:

  def __init__(self):
    self.result = []

  def kthSmallest(self, root: TreeNode, k: int) -> int:
    self.inorder(root)
    return self.result[k - 1]

  def inorder(self, root):
    if not root:
      return

    self.inorder(root.left)

    self.result.append(root.val)

    self.inorder(root.right)


'''
The solution above use the inorder traversal of the tree to solve this quesiton. 

The time complexity:
for this above solution is O(N), N = num of nodes in the tree.

The space complexity:
is also O(N), where N = num of node in the tree.

'''

#########  Solution 2 ######


class Solution:

  def kthSmallest(self, root: TreeNode, k: int) -> int:
    self.k = k
    self.result = None
    self.inorder(root)
    return self.result

  def inorder(self, node):
    if not node:
      return

    self.inorder(node.left)

    self.k -= 1
    if self.k == 0:
      self.result = node.val

    self.inorder(node.right)


'''
The solution above use the inorder traversal of the tree to solve this quesiton. 

The time complexity:
for this above solution is O(N), N = num of nodes in the tree.

The space complexity:
is also O(1)

'''

```



https://leetcode.com/problems/dungeon-game/



BQ:

1.帮助别人的例子，除了帮助组内的人，有没有帮助别组的经验；
 2.没有什么信息的情况下做的quick decision。