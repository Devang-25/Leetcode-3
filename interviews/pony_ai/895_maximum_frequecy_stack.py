"""

895. Maximum Frequency Stack
Hard

264

5

Favorite

Share
Implement FreqStack, a class which simulateÒs the operation of a stack-like data structure.

FreqStack has two functions:

push(int x), which pushes an integer x onto the stack.
pop(), which removes and returns the most frequent element in the stack.
If there is a tie for most frequent element, the element closest to the top of the stack is removed and returned.


Example 1:

Input:
["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
Output: [null,null,null,null,null,null,null,5,7,5,4]
Explanation:
After making six .push operations, the stack is [5,7,5,7,4,5] from bottom to top.  Then:

pop() -> returns 5, as 5 is the most frequent.
The stack becomes [5,7,5,7,4].

pop() -> returns 7, as 5 and 7 is the most frequent, but 7 is closest to the top.
The stack becomes [5,7,5,4].

pop() -> returns 5.
The stack becomes [5,7,4].

pop() -> returns 4.
The stack becomes [5,7].

Time Complexity:
Push: O(1)
pop: O(1)

"""

from collections import defaultdict

class FreqStack(object):

    def __init__(self):
        self.frequency = collections.Counter() # map key to frequency
        self.freq_to_key = defaultdict(list)
        self.max_count = 0

    def push(self, x):
        """
        - push the ele into the frequency counter
        - update the three data structure
        """
        self.frequency[x] += 1
        self.max_count = max(self.max_count, self.frequency[x])
        self.freq_to_key[self.frequency[x]].append(x)

    def pop(self):
        x =  self.freq_to_key[self.max_count].pop()
        if not self.freq_to_key[self.max_count]:
            self.max_count -= 1
        self.frequency[x] -= 1
        return x




# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
