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
