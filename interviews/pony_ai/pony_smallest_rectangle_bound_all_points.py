"""
设计一个处理二维点坐标的数据结构，支持push x, y， pop （策略FIFO）， get（一个能够把所有二维点包括进去的平行坐标轴的矩形）
     思路： 用set和惰性删除做，前两个操作总体复杂度O(NlogN)，最后一个操作O(1)
                用四个单调队列做，前两个操作总体复杂度O(N)，最后一个操作O(1)

解法：
- 1 个main stack
- 两个max stack (top and right)
- 两个min stacks (bottom and left)
- Suppose O(1) solution

Min Stack:
http://alrightchiu.github.io/SecondRound/stack-neng-gou-zai-o1qu-de-zui-xiao-zhi-de-minstack.html

- Min stack can support:
    - Push O(1)
    - Pop O(1)
    - GetMin O(1)



"""

class SmallestRectangle:
    def __init__(self):
        self.main_stack = []
        self.l_min = []
        self.r_max = []
        self.t_max = []
        self.b_min = []

    def __status__(self):
        print("current status")
        print("main", self.main_stack)
        print("left_min", self.l_min)
        print("right_max", self.r_max)
        print("top_max", self.t_max)
        print("bottom_min", self.b_min)

    def push(self, point):
        """
        input point: a list or tuple, representing the (x,y) coordinate of a point

        function of push:
        push the point into the main stack and update relevant data bases

        return None
        """
        x, y = point
        self.main_stack.append(point)
        # compare x with  top and bottom:
        if not self.t_max or y > self.t_max[-1][1]:
            self.t_max.append(point)
        else:
            self.t_max.append(self.t_max[-1])

        if not self.b_min or y < self.b_min[-1][1]:
            self.b_min.append(point)
        else:
            self.b_min.append(self.b_min[-1])

        if not self.l_min or x < self.l_min[-1][0]:
            self.l_min.append(point)
        else:
            self.l_min.append(self.l_min[-1])

        if not self.r_max or x > self.r_max[-1][0]:
            self.r_max.append(point)
        else:
            self.r_max.append(self.r_max[-1])

        print("push point:{}".format(point))

    def pop(self):
        """
        - pop the top item of the main_stack
        - update relevant databases
        """

        point = self.main_stack.pop()

        for l in (self.l_min, self.r_max, self.t_max, self.b_min):
            l.pop()
        print("pop point:{}".format(point))


    def get(self):
        """
        return the coordinates of a smallest rectangle that contain all the pionts
        """
        if not self.main_stack:
          print("no coordinates")
          return

        # get max y-axis
        top = self.t_max[-1][1]
        bottom = self.b_min[-1][1]
        # get min x on x-axis
        left = self.l_min[-1][0]
        right = self.r_max[-1][0]
        print("rectangle: top_left{}, top_right{}, bottom_left{}, bottom_right{} ".format([left, top], [right, top], [left, bottom], [right, bottom]))

############### Test Case ###########

sr = SmallestRectangle()
sr.push((3,0))
sr.push((-1, 4))
sr.push((3,1))
# sr.pop()
# sr.__status__()
sr.get()
