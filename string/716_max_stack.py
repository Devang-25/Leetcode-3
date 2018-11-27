"""
Design a max stack that supports push, pop, top, peekMax and popMax.

push(x) -- Push element x onto stack.
pop() -- Remove the element on top of the stack and return it.
top() -- Get the element on the top.
peekMax() -- Retrieve the maximum element in the stack.
popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.
Example 1:
MaxStack stack = new MaxStack();
stack.push(5);
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5
"""

class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.line = []
        # self.maxi = -1


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.line.append(x)
        # if x >= self.line[self.maxi]:
        #     self.maxi = len(self.line) - 1


    def pop(self):
        """
        :rtype: int
        """
        return(self.line.pop())


    def top(self):
        """
        :rtype: int
        """
        #print("top", self.line)
        if self.line:
            return(self.line[-1])
        else:
            return(None)


    def peekMax(self):
        """
        :rtype: int
        """
        # print('peakMax', self.line)
        return(max(self.line))


    def popMax(self):
        """
        :rtype: int
        """
        if not self.line:
            return(None)
        #print(self.line)
        target = max(self.line)
        i = len(self.line)
        for item in reversed(self.line):
            i -= 1
            if item == target:
                #print('before', self.line)
                del self.line[i]
                #print('after', self.line)
                break
        return(target)



# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
