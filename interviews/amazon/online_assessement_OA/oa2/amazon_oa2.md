# Amazon OA2

## Work Simulation



这个simulation就是把你放在一个新入职的员工的角度来过一天全职的生活，期间会遇到各种问题，然后对于需要回答的问题会给你有多个解决选项，你需要对每个选项评分，每个选项可以评1~5分，most effective是5，然后1是least effective。时间是两个小时，不是90分钟，是非常充裕的。全程选择题，不需要文字描述。



就是把team正在推进的项目描述一下，期间会有多个项目和你有关系，后面会遇到。

**2 进入工作界面。在这里可以看到接收到邮件，接收到的instant message。**

3 进入工作状态。**会有同事给你发邮件，发信息。需要你对他们提出的问题做一些判断，也就是给解决问题的选项评分。**



4 一共有21道题。中间会穿插video。

有让你**看log分析bug原因的**，

有让你**看分析报告给出问题结论的**，

当然更多的还是那种让你**判断怎么推进项目走向的**。

---------------------


## Work Simulation原则：



Work simulation(原则有先后顺序) 目前两大做题中最重要原则： 

1.requirement排在第一，deadline第二。 

2.有manager出现的选项无脑选manager，manager就是一个组的地头蛇。 



Amazon9条主要原则 

原则1：**客户是上帝**，requirement优先，任何影响上帝的事情都不能干。如某个requirement影响了上帝的体验， 你就是死键盘上也不能砍了，宁愿miss deadline 

原则2：为**长远考虑**，**即客户几年之后可能会出现的需求也要考虑到**， 不会为了交付短期的deadline， 而牺牲长期的价值。（比如 global api 和 local api） 

原则3：**最高标准**，“最高”对应上面的“长远”。 

原则4：一般情况，能**请示manager**就请示manager，manager一般不会出错 

原则5：**速度很重要**，决策和行动都可以改变，因此不需要进行过于广泛的推敲 ，但提倡在深思熟虑下进行冒险。 

原则6：不需要一定要坚持“非我发明”，**需求帮助也是可以的**，四处寻找创意，并且接受长期被误导的可能 

原则7：**敢于承担责任，任劳任怨**，比如领导说谁会java，你会你就跳出来说我会 

原则8：**对问题刨根问底**，探究细节 

原则9：服从大局（**团队比个人重要**）

https://github.com/VincentUCLA/LCPython/blob/master/amazon_onsite.md

------------

**打分不是关键，排序才是关键。** 大部分情况下其实并没有deadline 和 requirement谁更好，更多还是在 这个组合中你对ddl 和 requirement整体的权衡。



### 例1：deadline/自己开发/其他组开发

deadline是两周，现在解决方案有两种：
一种是自己开发，
一种是重其他组的服务；
自己开发，会比较慢，但是requirement能全部满足，会超过deadline；
用其他组的服务，requirement有些不能满足，但是可以在deadline前做完。
这时候会给你几个选项，让你去评分。

**我的答案：**首先满足requirement, 跟manager 讨论。 

原则2：为**长远考虑**，**即客户几年之后可能会出现的需求也要考虑到**， 不会为了交付短期的deadline， 而牺牲长期的价值。（比如 global api 和 local api） 

原则4：一般情况，能**请示**manager****就请示manager，manager一般不会出错 



### 例2：遇到Bug/问什么问题

有个同事遇到一个bug想让你帮他，和他一起加班。会给你几个选项，选项是你如果要做判断所需要问那个同事的问题，比如:
- 这个bug会不会影响客户？ 
- 这个bug有没有客户投诉过？
- 解决这个bug要多长时间？
- 这个bug会不会影响到其他组的工作进度？ 
你需要这几个问题评分，哪个最优。

我的答案：
- 这个bug会不会影响客户？ 5
- 这个bug有没有客户投诉过？5
- 解决这个bug要多长时间？4
- 这个bug会不会影响到其他组的工作进度？ 3

原则1：**客户是上帝**，requirement优先，任何影响上帝的事情都不能干。如某个requirement影响了上帝的体验， 你就是死键盘上也不能砍了，宁愿miss deadline 
原则5：**速度很重要**，决策和行动都可以改变，因此不需要进行过于广泛的推敲 ，但提倡在深思熟虑下进行冒险。



### 例3: 开会时间约不上

你要和不同组一块开会 每个组的代表碰巧出差到各个不同国家 给你几个解决方案. 有同学说过一句很经典的总结: work simulation并不是找最优解 而是让你根据某个原则去给选项排序. 对的，选项有: 

a 让几个组重新安排自己部门的代表 

b 问几个组能不能重新安排自己部门的代表

c 直接用远程视频对话

<!--楼主，我当时评5分的是c 直接用远程对话 我看到这个选项的时候 心想卧槽 这不是科技时代最好的解决办法吗 当我自信满满点了提交以后 进入下一个题 脑子飞快运转起来 为什么会有两个选项 都是让几个组重新安排代表 这两个选项有区别吗 答案是有的: 区别在于语气 work simualtion 考察的是collaborate 能力 当然也包括沟通的语气 楼主立马冷汗直冒 差点虚脱-->

答案：c, b a
c > b > a
b比a的语气好。
原则5：**速度很重要**，决策和行动都可以改变，因此不需要进行过于广泛的推敲 ，但提倡在深思熟虑下进行冒险。



### 例4：error rate chart 、service 1 有问题

error rate chart： service 1 有问题， 但还要看其他report确认

source: http://www.themianjing.com/2015/12/amazon-oa2-1218-due/

=======================================================================================



以下来自： https://github.com/YuanyuanZh/Algorithm/blob/master/src/Amzon/%E9%9D%A2%E7%BB%8F%E9%9B%86%E5%90%88.md



### 例5: shopping代码的test case
题目：test case。关于shopping的代码。

1. 第一问是某个method为什么不行:

  答案选的performance issue。 O(n^2)
  这个不太确定（其他几个选项更不合理）。

  

2. 第二问是how to improve shoppingcart class。
  我选的是**add user.id to shoppingcart class**. 

  

3. 第三问就是5个test case了。
  地里前辈说过很多了，应该是**1，3，5**跑不过。
  第一个是get_defualt_payment会返回null。
  第三个是user并没有初始化email，所以getemail会出错。
  第5个是setprice的method 返回的是integer，而testcase set的是double 。





同一个问题？

关于如何优化 JUnit 代码那部分两个问题

<!--有人说 **要选最长** 楼主顿时晕厥 楼主恰恰选的是俩最短.-->

-------


https://github.com/VincentUCLA/LCPython/blob/master/amazon_onsite.md



### 情境6： 图书馆推荐系统

给图书馆写图书推荐系统，关于book api 两个人，在表达不同的观点 

#### 第一问：

选择： 一开始其实每个人都在强调自己是对的，即使有一个人更对一些，也应该选**tell me more**

（原则8），选了之后会得到更多信息
原则8：**对问题刨根问底**，探究细节

#### 第二问：

选图书馆的服务器有没有开放关于实体书的api。
两个小哥讨论图书推荐的api应该是自己做还是用现成的。
自己做api覆盖面广，但是due赶不上。
别人做的能赶上due。 

答案：requirement优先（原则2），tell me more层层递进

原则2：为**长远考虑**，**即客户几年之后可能会出现的需求也要考虑到**， 不会为了交付短期的deadline， 而牺牲长期的价值。（比如 global api 和 local api） 
原则3：**最高标准**，“最高”对应上面的“长远”。 
原则8：**对问题刨根问底**，探究细节 



### 情境： 会议说系统出现bug

后面有会议说系统出现bug，该做出什么反应：

选：**看internal bug 记录。**



### 5个case看哪个可以通过

五个case看哪个可以通过，前人都提示过，**注意user的构造函数没有给email赋值**。



### 5个Unit Test

5个unit test 有一个是user的payment method返回的是null，一个是user的构造函数不包含email， 一个是setPrice()传进去的参数是double,但是return是int。

### 情境8：服务器老挂

经理说咱们最近服务器老挂，什么情况？ 先选看internal bug的记录

选 I think service 3 is the problem, but I would like to **see another report to confirm** 烙印，义正言辞说自己做了20年服务器，不可能有错误，刚刚调试过服务器，不可能是内部错误。 

- 选自己去查，问题的关键在于**不要麻烦别人 增加开发过程中测试的时间/测试覆盖更多case**，**放5** 
- 写Manuel test，放3 
- 还有个是unit test，也放3. 

- 增加QA的人手，放1 
- 让客户来当小白鼠发现问题，放1



### 情境9：log问题/德国
log问题。找相同原因就行。
我看的log是某个service出问题了，给了你一个report。
1. 第一问是为什么会出现德语，看report发现**出现德语的共同点是locate都在德国**，所以答案选的就是**locate**。(看半晌觉得应该是proxy的问题)
2. 第二问是为什么有的是invalid，看report发现共同点都是username都很长，因此选的username很长。( 看半晌觉得url里面客户的名字怎么都被砍短了.好像是这个问题)






### 情境7：客户deadline只有两周/延期/做完整

具体客户deadline只有两周，两个方案: 1)延到四周，做完整; 2) 另一个说先实现一部分功能做个demo，再慢慢做。

- 先做demo放5
- 按部就班周四放3
-  通知其他组说两周做不完接着做美国放1



### 情境8：估计项目开发时间

估计项目开发时间

- Manager放5，
- 找有经验的人请教4，
- 上网查资料或是先做一段时间再估计都放3， 
- 还有其他裸上的就1。



### 情境9：项目时间表设计， java

一个项目时间表设计 说你是这里最会用什么语言的，比如java



### 情境10：安排会议 

- 视频会议 5 
- 三个老二开会 3
- 老二去找老大开会 3 
- 推迟会议和邮件开会 1

 

### 情境11：搞数据库/找人帮忙？

搞个数据库.两周时间可以搞个数据，**ben可以帮忙，大腿priya可以帮，但是要等一周半 **

* 报告manager放5，
* 合作等大腿放4，
* 合作/等大腿是3
* 自己单干1
cut feaure都是1



### 情境12：系统是否升级 做两个feature

系统是否升级 做两个feature，一个让100%用户爽，一个让20%用户爽，但要升级系统，升级系统自己组会爽，但是升级会推迟做的feature，不升级吧，升级之后还得做一遍. 

**这题的中心是不升级，先做feature，先让用户爽。** 

1. 先做100的feature再升级，再做20的feature，放5 
2. 不升级，因为我们承诺要做feature，放4
3. 不升级，要搞定feature，可以以后推了其他deadline再升级，放3
4. 不升级，因为对其他组没影响
5. 我们应该focus在request上面，放2 
6. 升级，推迟这两个feature的deadline，因为升级造福子孙后代，放2 （没有让客户爽）
7. 升级，不然要做两次，放1 （没有让客户爽）

**这题的关键在于升不升级，要坚定的站在一边** （原则 1：顾客是上帝 > 原则2 & 3）



### 情境13：pick up 一个features的组合要求利益最大化

新产品设计给8周时间，选择题，让你pick up 一个features的组合要求利益最大化，每个feature都有相应的价值，H >> M >> L 都代表远大于. 

首先Deadline是前提，**中位数不能超过8太多**，那样的话就算feature再多也没意义。
同价值，按照deadline排序。同deadline按照价值排序。 



### 情境14：PurchasedByUser()

![image-20190223213931232](/Users/sonya/Library/Application Support/typora-user-images/image-20190223213931232.png)

myabe answer is b

source: https://www.1point3acres.com/bbs/thread-158368-1-1.html

### 情景15：Most effective way to imporve the ShoppingCart class?

![image-20190223214307219](/Users/sonya/Library/Application Support/typora-user-images/image-20190223214307219.png)

maybe it's c

出现的问题有email variable没有初始化;在user.getPaymentMethod().getDefault()中,getPaymentMethod返回的是个Null ; setPrice()传进去的参数是double,但是return是int,所以assertSame为false.

![image-20190223214528286](/Users/sonya/Library/Application Support/typora-user-images/image-20190223214528286.png)

### 情境17：代码分析 

三段一长**选最长**



===========

Source: https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=474434&highlight=Amazon%2Boa



### Q1: Schedule the design reviewmeeting (1)

1 - We can take our best guess at an estimate on our own

2 - We should work fora couple of days to gauge our progress, and then complete our estimate fromthere

4 - We should consulta coworker who has more relevant experience on this type of task

3 - We should conductour own investigation utilizing online research materials and internaldocumentation

5 - Let's ask ourmanager how we should go about developing an estimate





### Q2: Schedule the design review meeting (2)

3 - Ask all parties to identify a back-up person who could meet during a designated time

3 - See if there is abackup person on the Localization Team that can meet

5 - Set-up videoconferencing to include all POC's regardless of their physical location

1 - Agree to postponethe design review for two weeks when all parties have more availability

2 - Discuss the designreview over email

4 - Agree to schedulethe meeting at Xavier's location an hour away





### Q3: Response to Ravi (1)

3 - We should **miss the conference and increase the timeline to four week**s because we have four weeks of work

4 - Take a day to investigate whether adding additional resources would allow us to **meet the original timeline**, and re-evaluate afterwards

1 - Tell theLocalization team if can't be done in the timeline, so we should go ahead withthe US launch and delay the global launch even though it means adding anadditional week of effort to the four week estimate

5 - Take two weeks to create a prototype of the feature to demo at the conference, then take theadditional two weeks needed to **fully complete the feature**

2 - We can still hit the two week deadline without any changes by working harder and putting in overtime





### Q4: Response toRavi (2)

Begin yourinvestigation using the old error logs, but tell Ravi he will need to run the new logs if the old logs aren't useful





### Q5: Response to Aaron and Jacob (1)

Can you tell me moreabout what you're talking about?



### Q6: Response to Aaron and Jacob (2)

You said we have an internal database of both digital and physical books. How did we get the physical book data if the Book Database API doesn't give it to us?





### Q7: Response toAaron and Jacob (3)

I recommend you gowith Jacob's solution. We should miss the deadline to build our own service and meet all the requirements.





### Q8: Roadmap

Since you know more about the programming language than anyone else, you revise the estimate for porting to Java.





### Q9: Response to Nadia

What were the internal test case results?





### Q10: Most likely cause of German language issue

Site is using proxyserver location to determine displayed language





### Q11: Most likelycause of invalid recommendation issue

Database field storingusername is too short



### Q12: Log trace investivation success

5 - Increase time alotted for **testing in overall lifecycle**

5 - Update automatedend-to-end tests to include **broader data coverage**

3 - **Write more unit tests** to include edge cases

3 - Have t**eam members perform more manual testing** before checking code in

1 - Increase the **size of QA team**

1 - Have **more user testing** in beta phase





### Q13: Response for meeting the deadline

2 - **Work on the project on your own,** putting in extra effort to finish on time

3 - **Work on the project on your own until Priya is available**, then continue to work on ittogether

4 - **Work on the project with Ben**, being sure to watch his work closely because of his lack of experience

5 - **Tell your manager you** will not be able to complete the project in the time avaliable

1 - **Cut features from the product** so you will be able to meet the two week deadline

3 - **Start working onthe project right away with Ben.** Then **ask Priya to contribute** what she can whenshe is avaliable



### Q14: Response for completing this work on time

4 - **Work with the Customer Incentives Team** to identify the critical features that they need by the deadline, and focus on those

2 - **Push the timeline back another week** to ensure there is enough time for all work to be completedaccurately

3 - **Ask your whole team for help,** explaining the urgency that another team is blocked

5 - **Ask your manager** for help in determining the best approach to meet the new deadline

1 - **Put in extra hours yourself** to make sure everything gets done on time



### Q15: Upgrade

4 - We should **notperform this upgrade** at this point in time. We promised the Retail Website Teamwe would have their **new features complete by the proposed deadline**. Let'spostpone the **upgrade to another time**

2 - We should **notperform the upgrade** because it will not have a significant impact on the RetailWebsite Team's experience. We should **focus on the Retail Website Team'srequests**

3 - We should **notperform this upgrade at this point in time.** Our top focus is meeting our agreedupon commitment with the Retail Website Team, so we should finish that first.We can **focus on the upgrade afterwards** by **pushing our deadlines for some of ourother projects**

1 - I think we shouldperform the upgrade. The right thing to do is push back on the Retail WebsiteTeam because it will keep our team from having to do the same work twice

5 - I think we should **perform the upgrade.** As a compromise, we can **include the gift recommendationfeature** the Retail Website Team wants **by the deadline** and then **complete theupgrade.** We can finish the **seasonal-based gift recommendations** feature **afterthe deadline**

2 - I think we should**perform the upgrade**. The right thing to do is push back on the Retail WebsiteTeam because it will allow us to **more efficiently serve the customer and thecustomer will be helped in the long run.**

. 1point3acres



### Q16: New productdesign

2 - A, C, D, G

1 - A, C, D, G, H

4 - A, B, D

3 - A, C, F

5 - A, D, F

3 - F, G





**Q17: ？**

?





### Q18: Problem withProduct.wasPurchasedByUser()

It has performance issue





### Q19: Most effectiveway of improving ShoppingCart()

1）Change the design ofShoppingCart by **removing ShoppingCart user** and 

2) **making shopping cart a** **propertyof User instead**





### Q20: Five tests within ShoppingCartTest()

Fail - Test1

Pass - Test2

Fail - Test3

Pass - Test4

Fail - Test5





### Q21: Ask Jacob aquestion

3 - Do any otherprojects depend on fixing this problem?

5 - How many customersis this affecting?

5 - How does thisaffect customers

4 - Are we receivingcomplaints from customers?

2 - How long will ittake to solve this problem?

1 - If I help you withthis problem, will you help me finish my work today?



## Coding Questions: 



### Q1: K nearest restuarants (2019/1)

source: https://www.1point3acres.com/bbs/thread-483710-1-1.html

给一个List<List<Integer>>，返回距离(0,0)最近的X个点，返回类型List<List<Integer>>

https://leetcode.com/problems/k-closest-points-to-origin/

**time complexity: O(N*logN)**

**data structure: heap**

```python
from collections import defaultdict

class Solution(object):
def kClosest(self, points, K):
"""
:type points: List[List[int]]
:type K: int
:rtype: List[List[int]]

need to use max heap
"""
results = []
distance_cache = defaultdict(list)
for point in points:
x, y = point
distance = (x*x + y*y)
# print("distance", distance)
distance_cache[distance].append(point)

if len(results) < K:
heapq.heappush(results, -distance)

else:
heapq.heappushpop(results, -distance)
# print(results)

answer = []
while results:
distance = - heapq.heappop(results)
# print("distance", distance)
# print(distance_cache[distance])
answer.append(distance_cache[distance].pop())
return answer[:K]


```



### Q2: Max Device Capacity (2019/1)

source: https://www.1point3acres.com/bbs/thread-483710-1-1.html

给两个List<List<Integer>>和一个int deviceCapacity，返回不超过deviceCapacity的最大组合。



```python
"""
第二题略难。
给一个device capacity，一串 list of foreground application, 一串background application, 然后每个application是个tuple： (id, size)。 求所有总size加起来不超过device  capacity的foreground和background application的pair。比如你有foreground application: [[1, 2], [3, 4]], background application: [[4, 1], [5, 6]]， 总的capacity是8，那么答案就是 [[1, 5]] 因为 [1,2 ] 和[5,6] 组合起来刚好能撑满整个capacity。要求返回所有满足pair id。

Time Complexity: O(N log N)
- sort list O(N log N)
- for each foreground / forward_routes: do one binary search O(logN) => N * O(LogN) = O(N log N)


"""

def device_capacity(foreground, background, max_device_capacity):
"""
input foreground: list(tuple(int)), eg. [id, size]]
input background: list(tuple(int)), eg. [[id, size]]
max_device_capacity = int
"""
max_available_device_cap = -float("inf")
max_ids = []

# sort both foreground and background
foreground.sort(key=lambda x: x[1])
background.sort(key=lambda y: y[1])

print(foreground, background)

for foreground_i, foreground_size in foreground:
	print("foreground", foreground_i, foreground_size)
	if foreground_size > max_device_capacity:
	continue

	max_background_size = max_device_capacity - foreground_size

# use bineary search to search max_background_size:
start = 0
end = len(background) - 1

while start <= end:
mid = (start + end) // 2

background_size = background[mid][1]
background_i = background[mid][0]
total_size = foreground_size + background_size

if total_size <= max_device_capacity:
if total_size == max_available_device_cap:
max_ids.append((foreground_i, background_i))
print("1", max_ids)
elif total_size > max_available_device_cap:
max_available_device_cap = total_size
max_ids = [(foreground_i, background_i)]
print("2", max_ids)

if background_size == max_background_size:
print("break")
break

elif background_size < max_background_size:
start = mid + 1
print("right")

elif background_size > max_background_size:
end = mid - 1
print("left")

return max_ids


############ test case 1 ###########

# foreground = [[3, 4], [1, 2]]
# background = [[4, 1], [5, 6]]
# max_device_capacity = 8
# # return [[1,5]] b/c 2 + 6 = 8

############ test case 2 ###########
# foreground = [[1,3000],[2,5000],[3,4000],[4,10000]]
# background = [[1,2000],[2,3000],[3,4000]]
# max_device_capacity = 11000
# # return [[2, 3]]

############ test case 3 ###########
foreground = [[3, 4], [1, 2], [2, 3]]
background = [[4, 1], [5, 6], [8, 5]]
max_device_capacity = 8
# return [[1,5], [2, 8]] b/c 2 + 6 = 8


print(device_capacity(foreground, background, max_device_capacity))

```



### Q3: closest two sum < target (2019.2)

https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=478916



#### only return 1 pair of result

```python
"""
closest two sum < target

https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=478916

"""


from collections import defaultdict

########## return only 1 pair of results ##########
def closest_sum(nums, target):

nums.sort() # O(NlogN)

l = 0
r = len(nums) - 1
closest_sum = "None"
closest_pair = []

while l < r:
cur = nums[l] + nums[r]
if cur == target:
return(nums[l], nums[r])
elif cur < target:
if closest_sum == "None" or (target - cur < target - closest_sum):
closest_sum = cur
closest_pair = [nums[l], nums[r]]
l += 1
elif cur > target:
r -= 1
return closest_pair


nums = [2, 0, 6, -3, -6, 8, 10, 4]
target = 11

nums = [2, 1, 6, -3, -6, 8, 10, 4]
target = 11


print(closest_sum(nums, target))
```

#### return all quality pairs

```python
"""
closest two sum < target

https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=478916

"""


from collections import defaultdict

########## return all pair of results ##########


from collections import defaultdict

def closest_sum_all_pairs(nums, target):

nums.sort() # O(NlogN)
# print("nums", nums)

l = 0
r = len(nums) - 1
closest_sum = "None"
closest_pairs = []

"""
# if not any closest sum OR
# if the current diff < previous diff:
# target - cur < target - closest_sum
# then update
"""
while l < r:
# print("l,r", nums[l], nums[r])
cur = nums[l] + nums[r]
if cur <= target:
if closest_sum == "None" or (target - cur < target - closest_sum):
closest_sum = cur
closest_pairs = [[nums[l], nums[r]]]
# if same, then append
elif target - cur == target - closest_sum:
closest_pairs.append([nums[l], nums[r]])
if cur == target:
l += 1
r -= 1
elif cur < target:
l += 1
elif cur > target:
r -= 1
return closest_pairs


# nums = [2, 0, 6, -3, -6, 8, 10, 4]
# target = 11

nums = [2, 1, 6, -3, -6, 8, 10, 4]
target = -6


print(closest_sum_all_pairs(nums, target))


```



### Q4: Most Popular Parent Node of A Tree (2019.1)

source: https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=478915



```python
"""
第二题，most popular parent node in a tree.
给定一个多叉树的根节点，每个节点有一个值，找出一个最popular的节点。比如这样

Given a binary tree:

1
/   \
-5     11
/ \   /  \
1   2 4    -2

每个节点的popular值是以自身为根节点的树中所有节点的值之和除以以自身为根节点的树的节点数量。
可以用dfs也可以用bfs，注意读清楚题的话应该不会太难。要注意的是叶子节点不考虑。

popularity = SUM_of_substree_act_as root / NUM_of_NODES_of_substree_act_as_root

"""

class Node:
def __init__(self, val):
self.val = val
self.left = None
self.right = None


class Popularity:
def __init__(self):
self.max_popularity = float("-inf")
self.max_popular_node = None

def find_popularity(self, node):
"""
input node: a treenode

return cur_total: int, sum of this subtree.

return num_of_node: int, the number of node of this subtree including this node.
"""
if not node:
return 0, 0

left_total, left_nodes = self.find_popularity(node.left)

right_total, right_nodes = self.find_popularity(node.right)

cur_total = node.val + left_total + right_total

node_num = 1 + left_nodes + right_nodes

popularity = float(cur_total / node_num)
if popularity > self.max_popularity:
self.max_popularity = popularity
self.max_popular_node = node

print("now", "node.val{}, node.total{}, num_of_nodes{}".format(node.val, cur_total, node_num))

return cur_total, node_num

def popularity(self, root):
self.find_popularity(root)
return self.max_popularity, self.max_popular_node.val


a = Node(3)
b = Node(-12)
c = Node(14)

a.left = b
a.right = c

print(Popularity().popularity(a))

```



### Q5: Most Frequent Word that's not in Banned 找高频词（需要去除一个常用词库里面的词）(2019.1)

find the most frequent word. 大小写不重要

Source: ‎⁨iCloud Drive⁩ ▸ ⁨Documents⁩ ▸ ⁨Leetcode_sonya⁩ ▸ ⁨amazon⁩ ▸ ⁨online_assessement_OA⁩  Page 12

example: https://leetcode.com/problems/most-common-word/

```python
"""
some people use: 1) collection.Counter + 2)counter.most_common
but Counter.most_common has a time complexity of O(NlogN)

上面的方法比用方法2快： 因为1）top_frequncy + 2）top_word + 扫一遍单词快。方法二需要 O(N) > O(NlogN)


========

Regular Expression
https://developers.google.com/edu/python/regular-expressions


==========

r'\w+'

r\:  in python means "raw" string, passes into through backslashes \

\w : (lowercase w) matches a "word" character: a letter or digit or underbar [a-zA-Z0-9_]. 

+ : one or more occurrence of the pattern to the left of it  (in this case: it's \w)


=========

re.findall(pattern, string)
https://docs.python.org/2/library/re.html


Use: to find a word without space
Example: 你有各种符号，及不等数量的空格在单词之间，但是你只想要单词。
”A,a,a,a, bp apple, banan    ! Bear"

Example:  re.findall(r'\w+", text)

==========

most_common([n])
Return a list of the n most common elements and their counts from the most common to the least. If n is omitted or None, most_common() returns all elements in the counter. Elements with equal counts are ordered arbitrarily:

>>> Counter('abracadabra').most_common(3)
[('a', 5), ('r', 2), ('b', 2)]

https://docs.python.org/2/library/collections.html


"""

import collections
import re

class Solution(object):
def mostCommonWord(self, paragraph, banned):
"""
:type paragraph: str
:type banned: List[str]
:rtype: str
"""
banned = set(banned)

data = re.findall(r'\w+', paragraph.lower())
# print("data", data)

top_word = collections.Counter(w for w in data if w not in banned).most_common(1)[0][0]


return top_word
```





### Q6: Word Count Engine

input:  document = "Practice makes perfect. you'll only get Perfect by practice. just practice!"

output: [ ["practice", "3"], ["perfect", "2"], ["makes", "1"], ["youll", "1"], ["only", "1"],  ["get", "1"], ["by", "1"], ["just", "1"] ]

```python
from collections import defaultdict
import string

def word_count_engine(document):
"""
input document: str
return output: list[[str, int]]
decending order

# split
# take out the puction
# change to lower cases
# iter: count , store
"""

data = document.lower()
data = ''.join(c for c in data if c not in string.punctuation)
data = data.split()
print(data)

counter_dict = defaultdict(int)

for ele in data:
counter_dict[ele] += 1
print(counter_dict.items())

#print(data.index("youll"))
result = sorted(counter_dict.items(), key=lambda x: (x[1], -data.index(x[0])), reverse=True)
print('result', result)
final_result = []

for (key, value) in result:
pair = [key, str(value)]
final_result.append(pair)

return final_result
```



### Q4: max average sum subtree

max average sum subtree (general tree, leaves not counted), return tree node: https://cchang.gitbooks.io/codinginterview/content/binary-tree/subtree-with-maximum-average.html



```python
"""
Given a binary tree:

1
/   \
-5     11
/ \   /  \
1   2 4    -2


Find the subtree with the maximum average

"""

# from statistics import mean
# import math

class Node:
def __init__(self, val):
self.val = val
self.left = None
self.right = None

class MaxAverage:
def __init__(self):
# self.max_avg = float("-inf")
self.max_avg = 0
self.max_node = None


def find_avg(self, node):
"""
input node: a node
return a tuple (int, int) = (avg, num_of_nodes)
"""
# bottom case: just return 0
if not node:
return (0, 0)

print("down", node.val)

# if node.left, then search the average(node.left)
# if node.left:
#   left_avg, left_num = self.find_avg(node.left)


# if node.right:
#   right_avg, right_num = self.find_avg(node.right)

left_avg, left_num = self.find_avg(node.left)
right_avg, right_num = self.find_avg(node.right)

print("upward", node.val)
num_of_node = left_num + right_num + 1
cur_total = float(left_avg * left_num + right_avg * right_num + node.val)
new_average = cur_total / num_of_node

if new_average > self.max_avg:
self.max_avg = new_average
self.max_node = node

return new_average, num_of_node

def max_average(self, root):
"""
input root: node
output node: a node whose subtree with max average
"""

self.find_avg(root)

# return self.max_avg
# return self.max_node.val
return self.max_node

######## test case 1########
# a = Node(0)
# b = Node(1)
# c = Node(2)

# a.left = b
# a.right = c



########### test case 2 ######

a = Node(3)
b = Node(-12)
c = Node(14)

a.left = b
a.right = c

####### run ######
ma = MaxAverage()
result = ma.max_average(a)
print(result)

```





### Q1: Mininum Sum of BST

BST那道题，root到leaves是到最后一个leave的完整路径还是root到BST中的任意一个leave，返回root到所有leave中的minimum sum.

注意1：对的就是这样子的。但是**有坑**，题目中**给的类型和代码里的返回值不一样**。我最后都没有找出问题。|| cycle list跟ListNode没关系，题目自定义了一个CNode，用这个就行了

类似题目：Minimum Sum Path http://csegeek.com/csegeek/view/tutorials/algorithms/trees/tree_part5.php

https://leetcode.com/problems/path-sum-ii/



```python
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

```





### Q2: Insert Value into Cycle Linked List

第二题就是给一个node节点和一个target值？然后让你插进去。首尾相连的链表，但是给的那个参数节点不是链表元素最小的那个.

注意2：题目中说返回值类型是CNode，但是代码里默认的返回值是LNode。我两种都试过了，都有问题。逻辑对，但是case过不了。

类似题目：https://www.geeksforgeeks.org/sorted-insert-for-circular-linked-list/



```java
"""
Problem: Sorted insert for circular linked list

https://www.geeksforgeeks.org/sorted-insert-for-circular-linked-list/

Time Complexity: O(n) where n is the number of nodes in the given linked list.

"""


class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

class CycleLinkedList:
  def __init__(self):
    self.head = None

  def print_list(self):
    temp = self.head
    print(temp.val)
    temp = temp.next
    while temp != self.head:
      print(temp.val)
      temp = temp.next

  def insert(self, val):
    # make new node
    new_node = Node(val)

    # insert into an empty list
    if self.head == None:
      new_node.next = new_node
      self.head = new_node

    # insert before the self.head
    # thus, need to find the last node: the node before the head
    elif val <= self.head.val:
      cur = self.head
      while cur.next != self.head:
        cur = cur.next
      new_node.next = cur.next
      cur.next = new_node
      self.head = new_node

    # insert after the head
    else:
      cur = self.head
      # as long as not going back to th head and
      # the next value is still smaller than the insert val:
      # we move forward.
      # Else: we update
      while cur.next != self.head and cur.next.val < val:
        cur = cur.next
      # update
      print("found", "cur", cur.val, "next", cur.next.val)
      new_node.next = cur.next
      cur.next = new_node




# c = CycleLinkedList()
# c.insert(12)
# c.print_list()
# c.insert(56)
# print("print")
# c.print_list()


####################

arr = [12, 56, 2, 11, 1, 90, 90, 1]

c = CycleLinkedList()

i = 1
for num in arr:
  print("#", i, ":", num)
  c.insert(num)
  print("head", c.head.val)
  print("print list")
  # c.print_list()
  i += 1

# print(c.head != None)
c.print_list()

```



### 10: Count number of substrings with exactly k distinct characters (2019.2)

Given a string of lowercase alphabets, count all possible substrings (not necessarily distinct) that has exactly k distinct characters.
**Examples:**

```
Input: abc, k = 2
Output: 2
Possible substrings are {"ab", "bc"}

Input: aba, k = 2
Output: 3
Possible substrings are {"ab", "ba", "aba"}

Input: aa, k = 1
Output: 3
Possible substrings are {"a", "a", "aa"}
```



```python
"""
Given a string of lowercase alphabets, count all possible substrings (not necessarily distinct) that has exactly k distinct characters.
Examples:

Input: abc, k = 2
Output: 2
Possible substrings are {"ab", "bc"}

Input: aba, k = 2
Output: 3
Possible substrings are {"ab", "ba", "aba"}

Input: aa, k = 1
Output: 3
Possible substrings are {"a", "a", "aa"}

思路：
- 需要记住目前的substring有哪些字母： set
- 目前的substring 长度. Len(set) O(1)
- 需要记住目前已有的results set()

move forward: 
- 两个指针： i, j
- 如果发现已有重复的：1)set.remove(string[i]) 2)move i+=1 until string[i] not in current substring
- 发现len(set) == k: add string[i:j+1] into results if substring not in results_set
- len(set) < k: j +=1: 
  - 如果发现已有重复的：1)set.remove(string[i]) 2)move i+=1 until string[i] not in current substring

"""

def substring_with_length_k(string, k):
  """
  input string: string
  input k: int

  output results: list of string [string]
  or output int: len(results)
  """
  if not string or not k:
    return []
  
  substring = set()
  results = set()

  for index in range(k-1):
    substring.add(string[index])
    print(substring)

  i = 0
  j = k-1

  while j < len(string):
    print("i{}, j{}".format(i, j))
    if string[j] not in substring:
      substring.add(string[j])
      if len(substring) == k:
        word = string[i:j+1]
        print("word", word)
        if word not in results:
          results.add(word)
          print("add", results)
        substring.remove(string[i])
        i += 1
      j += 1
    else: # if string[j] is already in substring
      substring.remove(string[i])
      i += 1
  return list(results)
  # return len(results)

####### test case 1###########
# string = "apeapele"
# # ape, pea, eap, pel
# k = 3
# print(substring_with_length_k(string, k))

######## more test cases ########

# print(substring_with_length_k("", 2))
# print(substring_with_length_k("abc", 2))
# print(substring_with_length_k("aba", 2))
print(substring_with_length_k("aa", 1))

```



### 例11： Rolling Average (2019.1)



```python 
"""

input： [1,3,5,7,8] size =2
output: [2.0,4.0,6.0,7.5]

"""

def rolling_average(nums, size):
  if size == 0:
    return "division by 0"
  

  rolling_avg = []
  for i in range(len(nums) - size + 1):
    rolling_avg.append((sum(nums[i:i+size]))/size)
  return rolling_avg

# nums = [1,3,5,7,8] 
# size = 2
#output: [2.0,4.0,6.0,7.5]

nums = [1,3,5,7,8] 
size = 0

print(rolling_average(nums, size))
```





### 12: 迷宫 (2019.1)

Find Path in 2D matrix

输入一个2D的int array，其中有0，1，9。

0为墙壁 1为可以通过，9 为需要找的结果.

返回true or false，表示可以找到9或者没有办法找到。9不一定只有一个。





这道题如果真是1是路，找9比较好，可以直接用大于符号。

一亩三分地里面也有人说0是可以通过，1是墙壁，只能看着来了。出生点我定为（0,0）因为我不确定OA中给的是不是（0,0）

需要注意的特殊情况是第一个就是需要找的9，eg. {{9}}



想了一下，应该是上下左右都可以活动才对，所以又加了两个方向。感觉可以把Korsh原来写的炫酷的迷宫游戏写出来了。还是做面试准备先。
原文：https://blog.csdn.net/lycorislqy/article/details/49202651 



```python
import heapq

def maze(matrix):
  """
  input matrix: [[int]]
  output: True / False
  """
  visited = set()

  candidates = [[0, 0, 0]]
  visited.add((0, 0))
  while candidates:
    candidate = heapq.heappop(candidates)
    print("candidate", candidate)
    d, r, c = candidate
    
    neighbors = [[r+1, c], [r, c+1], [r-1, c], [r, c-1]]
    print("neighbors", neighbors)
    
    for neighbor in neighbors:
      r1, c1 = neighbor
      
      # check neighbor boundary
      if r1 < 0 or r1 >= len(matrix) \
      or c1 < 0 or c1 >= len(matrix[r1]):
        print("out of boundary")
        continue
      
      print("neighbor, row{}, col{}, val{}".format(r1, c1, matrix[r1][c1]))

      if matrix[r1][c1] == 9:
        print("found", neighbor)
        return True
      
      elif matrix[r1][c1] == 1:
        if (r1, c1) not in visited:
          print("process new neighbor")
          visited.add((r1, c1))
          distance = r1 * r1 + c1 * c1
          neighbor = (distance, r1, c1)
          heapq.heappush(candidates, neighbor)
  return False

matrix = [
  [1,1, 1],
  [1,0, 1],
  [0,0, 9]]

# matrix = [
#   [1,1, 1],
#   [1,0, 1],
#   [0,0, 0]]

print(maze(matrix))
```





### 例3：City Power

给十几个城市供电，连接不同城市的花费不同，让**花费最小**同时**连到所有的边**。给出一系列connection类，里面是edge两端的城市名和它们之间的一个cost，找出要你挑一些边，把所有城市连接起来并且总花费最小。**不能有环**，最后所以城市要连成一个连通.

不能的话输出空表，最后还要**按城市名字排序输出**，按照node1来排序,如果一样的话再排node2。



输入:

{"Acity","Bcity",1}

("Acity","Ccity",2}

("Bcity","Ccity",3}

输出：

("Acity","Bcity",1}

("Acity","Ccity",2}

补充一句，test case一共有6个。



### 例4： Longest substring with at most k distinct characters (2018-7)

Leetcode: https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/



```python
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        found = collections.Counter()
        i = max_length = 0
        for j, ele in enumerate(s, start = 1):
            found[ele] += 1
            while len(found) > k:
                found[s[i]] -= 1
                # for every WHILE loop, you run one if-statement
                if not found[s[i]]:
                    found.pop(s[i])
                # you keep moving pointer i, until len(found) > k
                i += 1
            max_length = max(max_length, j - i)
        return max_length
        
```



### Missing Number:

leetcode268 Missing Number

Easy

Given an array containing *n* distinct numbers taken from `0, 1, 2, ..., n`, find the one that is missing from the array.

**Example 1:**

```
Input: [3,0,1]
Output: 2
```

**Example 2:**

```
Input: [9,6,4,2,3,5,7,0,1]
Output: 8
```

**Solution:** 

From elementary school math, we have a popular math trick which is the sum of 1+2+...+n = n*(n+1)/2, it can be used here. Since we are finding the missing number, just get the sum of all the n number first using the formula, and the minus it to the sum of all the numbers in the array, we get the missing number.

```python
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        real_total = n*(n+1)/2
        return real_total - sum(nums)
        
```





### 例5：Sum btw two nodes in BST (2018-7)

Given a list of numbers, construct a BST from it and find the distance between two nodes.
int bstDistance(int[] values, int node1, int node2)
这题input全是用int表示的



### 例6： 

每个session(类似user) 有一个播放歌曲顺序的历史纪录 session1: A -> B -> C -> A session2: C -> A -> B -> C -> E -> A -> B -> C session3: A -> B -> C -> B -> D. 

找长度为n最热门的播放顺序 ex1 input: n=3 output: A -> B -> C



ps1:它们存session是用List of List ps2:同一个顺序在同个session裡面只会算一次, 像是session2 A -> B -> C发生两次,只会算一次



```python
def longest_n_subsequence(sessions, n):
"""
input session: list os list [[A -> B -> C -> A]]
n: integer, max_length of the subsequence
return list of int [a, b, c...]
"""
```



## 链接：

1. https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=137995&page=2
2. 
