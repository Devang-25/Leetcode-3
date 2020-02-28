## 2019/03 数据科学类 OT Hackerank

OT**一共三道题，第三题不算分**，计时共**三小时.** 

**第一题，写一个function，根据已有的（x,y），计算新x的y值，**题目不难，而且instruction 里，也把特殊情况说的很清楚，所以做起来是很顺利的
**第二题，处理数据，首先读取一个dataframe，题目有很多个小问，每个小问考察一个小点，****前两个主要是需要熟悉pandas/numpy的计算和操作，后几个问是linear regression 和 mse的相关计算**
第三题，我没有做lol...



<https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=494746&highlight=two%2Bsigma>



>

## 2019/01 Data Science Intern

我面的是QR，有三道题，不过最后一道是bonus，开始吓我一条，还琢磨怎么多一道。 
**第一道编程序，game of life。 秒过。很简单。(<https://leetcode.com/problems/game-of-life/>)**
**第二道是数据分析题。**

比较恶心的是，要知道怎么读取数据，如果这一关过不来就挂了。我在这上面花了挺长时间，所幸最后弄对了。 
数据分析倒不难，就是要准备一些数据分析的技巧，如果用python，pandas， sklearn肯定要熟的。 
最后通过了所有的case。

<https://www.1point3acres.com/bbs/thread-493467-1-1.html>



##  2019/03 Quantitative Researcher HackerRank

<https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=475845

![image-20190415201812009](/Users/sonya/Library/Application Support/typora-user-images/image-20190415201812009.png)

![image-20190415201830423](/Users/sonya/Library/Application Support/typora-user-images/image-20190415201830423.png)

![image-20190415201922147](/Users/sonya/Library/Application Support/typora-user-images/image-20190415201922147.png)



![image-20190415201959376](/Users/sonya/Library/Application Support/typora-user-images/image-20190415201959376.png)![image-20190415202011691](/Users/sonya/Library/Application Support/typora-user-images/image-20190415202011691.png)



![image-20190415202028295](/Users/sonya/Library/Application Support/typora-user-images/image-20190415202028295.png)





----------------------



![image-20190415202047623](/Users/sonya/Library/Application Support/typora-user-images/image-20190415202047623.png)



![image-20190415202105462](/Users/sonya/Library/Application Support/typora-user-images/image-20190415202105462.png)



![image-20190415202124634](/Users/sonya/Library/Application Support/typora-user-images/image-20190415202124634.png)



![image-20190415202145875](/Users/sonya/Library/Application Support/typora-user-images/image-20190415202145875.png)



<https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=475845>





## 2019/03 Software Engineer

**Phase one** :是叫你设计一个**Random Class**， 要求**specify一个interval**之后，它**return interval中的随机数字**。但额外的要求是，每个数字只能return一次，一旦出现过，就不会再return相同的数字。直到最后把这个inteval里所有的数字return完。然后再回到所有数字都可能被return的阶段。
然后叫自己写testing。

**Phase two**是要求支持随时可以改变interval range的feature，而且range改变之后，此前return过的数字依然不会再return，直到range里的所有数字都被return一遍。
然后是写更多的testing。

**楼主的做法:**

是用一个Arraylist candidateList装可以return的candidate，每次通过call Java的Random.nextInt 来得到 to-return element的index。return了这个element出去之后，把它和arrayList的最后一个element交换位置，再remove。这样removal就是O（1）。
支持update range的方法是maintain另外一个List，记录所有被remove掉了的element，每次update之后重建ArrayList，并把所有被记录了remove的element从重建的list里去除。有这第二个array的好处是，当range里所有element都进了removed list之后，可以直接调换两个array的reference，重新开始而不需要重新populate。

按照这样的做法，initialize需要O（N），UpdateRange O(N), getRandom O(1).  30分钟内要做完coding，自己写test和跑test时间还是比较紧张的。不确定是否是最优解，应该可以再优化，但在big O time上似乎已经没法做到更好了。结束之后问我假如用BST或者hashmap的话会有什么区别， 似乎是还有更好的解。但我分析之后认为不管用什么DS，Initialize和UpdateRange似乎没法做到比O（N）更好。如果地里有想到更好解法的大神，请务必让我知道。

第二个list仅是记录，不存在lookup操作，所以并不一定要用set。调换只是一个小优化，也不影响BigOTime，做不做都无所谓的。



**最后说下感受，**总的来说感觉2s电面的professionalism还是差了点，尤其是和谷歌比。大多数问题都是问了很多年的原题，可以看出他们的题库也就这么点而且没动力更新。面试官全程基本没什么反馈，我跟他说我的想法他就只会说ok那你写写看，很多时候干脆不说话，估计是在干别的，于是后来楼主也不说话了。写出来了以后，感觉他也无法判断对错，只能通过跑test的结果。有点好笑的是面试结束之后楼主没有关页面，看到他自己留在那个hackarank页面上各种写和跑test。我觉得一个有足够水平的面试官，熟悉问题、肉眼判断解法对错是基本的吧。



<https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=496638&highlight=two%2Bsigma>



## 2019/03 Software Engineer

老题: **1)friend circle 和 2)longest chain.**
对没见过这两题的朋友，**Friend circles**在**leetcode 547.**
**Longest chain 在 <https://www.cnblogs.com/EdwardLiu/p/6177843.html>**



<https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=494286&highlight=two%2Bsigma>





## 2019/03 Software Engineer OA

还是原来的配方，还是熟悉的味道，Friend Circles + longest chain

<https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=504459&highlight=two%2Bsigma>



## 2016/12 超全

(太长了，直接看链接)

<https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=216941&highlight=two%2Bsigma>

大概就是：
- Behavioral
- 电面6题加答案
- onsite 三套，每套三轮，附答案





## 2018/12 Quantitative Research Intern

1，以下俩linear regression模型Y~X, X~Y，那么他们的R2、系数Beta、以及noise（epsilon）是什么关系？ 
2，如果你是个taxi driver，如何规划一天让自己受益最大？ 如果你可以选择做Uber和普通Cap driver，应该如何利用数据做出选择？

<https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=467937&highlight=two%2Bsigma>



## 2019/01 

**题目如下：**

一个void generator (int ms, int bufferSize), 每隔 m (ms) 会generate 一个token 到queue 里面。 另外一个int getter(int desiredAmount) 去queue 里面fetch 它最大可以拿的数目，就是如果queue 里面的size大于它想要的，那么就返回那个desiredAmount,不然就直接返回当前queue 所有的数目。



我用了个不熟的synchronousQueue来做，其实应该直接用锁就好了，对queue的size 来增加减少，那时候也没想出来。。。



**楼主写的（不一定对）：**
import queue
import threading
import time

class tockenGenerator:
    def __init__(self):
        self.q = queue.PriorityQueue()
        self.count = 0
. check 1point3acres for more.
    def generator(self, time, buffer_size):
        self.buffer_size = buffer_size
        self.time = time
        self.enque_token(). 1point3acres

​    def enque_token(self):
​        print('ENQUEING...', self.count)
​        threading.Timer(self.time, self.enque_token).start()
​        self.count+=1
​        if self.count < self.buffer_size + 1:
​            self.q.put((self.count, "Task"))

​    def getter(self, amount):
​        res = []
​        for _ in range(amount):
​            if self.q.empty():
​                return res
​            res.append(self.q.get())
​            self.count-=1
​        return res



**不是的话 算法题不外乎就是**

1. **Random Mod 5 Iterator**
   可参考：[https://github.com/sreeprasad/To ... omMod5Iterator.java](https://github.com/sreeprasad/TodayILearntTo/blob/master/RandomMod5Iterator.java)
2. **weight random class**
3. **implement a random number generator in a range without repeats**(我拿到这题 等我确定我有没有onsite 我会把详细的code放上来)



## 2019 Summer Intern

还是两道原题，第三道题没写，一共三小时。

**Q1 implement a linear interpolate.** 有几种特殊情况列的很清楚。 我是先排序，按x排， x一样按y排，然后用binary search去找区间。 

**Q2 数据处理，好像是5个小问**。**找median，standard divination，least square。**主要用了pandas和sklearn里的linear regression



<https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=507865&highlight=two%2Bsigma>

