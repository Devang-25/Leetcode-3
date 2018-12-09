"""
155. Min Stack
Easy
1341
140


Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""

# # Leetcode 155. Min Stack:
# # https://leetcode.com/problems/min-stack/


# # Solution 1 64ms, beat 59.62%:
# # Use 2 stacks.
# # The two stacks always maintain the same length.
# # 1st stack will simply record the values
# # 2nd stack will record the min value up to this point.
# class MinStack:

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.vals = []
#         self.mins = []

#     def push(self, x):
#         """
#         :type x: int
#         :rtype: void
#         """
#         self.vals.append(x)
#         cur_min = min(self.mins[-1], x) if self.mins else x
#         self.mins.append(cur_min)

#     def pop(self):
#         """
#         :rtype: void
#         """
#         self.vals.pop()
#         self.mins.pop()

#     def top(self):
#         """
#         :rtype: int
#         """
#         return self.vals[-1]

#     def getMin(self):
#         """
#         :rtype: int
#         """
#         return self.mins[-1]

########################################

# Solution 2. 56ms, beat 99.01%:
# Keep track of the current mean.
# The stack should store diff = cur_val - last_min.
# We need to update cur_min if
# 1) push. diff < 0. cur_min += diff
# 2) pop. diff < 0. cur_min -= diff
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.diffs = []
        self.cur_min = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.cur_min is None:
          self.cur_min = x
          self.diffs.append(0)
        else:
          diff = x - self.cur_min
          self.diffs.append(diff)
          if diff < 0:
            self.cur_min = x

    def pop(self):
        """
        :rtype: void
        """
        diff = self.diffs.pop()
        # Boundary condition.
        if not self.diffs:
          x = self.cur_min
          self.cur_min = None
          return x

        if diff < 0:
          x = self.cur_min
          self.cur_min -= diff
          return x

        x = self.cur_min + diff
        return x

    def top(self):
        """
        :rtype: int
        """
        diff = self.diffs[-1]
        if diff < 0:
          return self.cur_min

        return self.cur_min + diff

    def getMin(self):
        """
        :rtype: int
        """
        return self.cur_min





########################################

# class MinStack:

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.val = []
#         self.min = []



#     def push(self, x):
#         """
#         :type x: int
#         :rtype: void
#         """
#         self.val.append(x)
#         if not self.min or (x <= self.min[-1]):
#             self.min.append(x)


#     def pop(self):
#         """
#         :rtype: void
#         """
#         if not self.val:
#             raise Exception("error: list is empty")
#         ele = self.val.pop()
#         if ele == self.min[-1]:
#             self.min.pop()

#     def top(self):
#         """
#         :rtype: int
#         """
#         return self.val[-1]

#     def getMin(self):
#         """
#         :rtype: int
#         """
#         print(self.min)
#         if not self.min:
#             raise Exception("list is empty")
#         return self.min[-1]



# # Your MinStack object will be instantiated and called as such:
# # obj = MinStack()
# # obj.push(x)
# # obj.pop()
# # param_3 = obj.top()
# # param_4 = obj.getMin()
