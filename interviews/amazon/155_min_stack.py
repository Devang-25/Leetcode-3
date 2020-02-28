#### Solution 1###########
#Runtime: 60 ms, faster than 76.79% of Python3 online submissions for Min Stack.


class MinStack:

  def __init__(self):
    """
    stack: first in, last out.
    """
    self.vals = []
    self.mins = []

  def push(self, val):
    self.vals.append(val)
    if (not self.mins) or (val < self.mins[-1]):
      self.mins.append(val)
    else:
      self.mins.append(self.mins[-1])

  def pop(self):
    self.mins.pop()
    return self.vals.pop()

  def top(self):
    return self.vals[-1]

  def getMin(self):
    return self.mins[-1]


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