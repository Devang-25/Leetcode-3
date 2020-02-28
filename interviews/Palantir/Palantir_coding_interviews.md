# Palantir 

第一轮：给java写的代码，找错，debug。
两个错误：

（1）只算了to的邮件，没有算cc的
（2）bfs的时候用的方法不efficient

第二轮：coding，各一个stream of integer， 实现median，mode，mean
第三轮：系统设计，给一系列food ingredient， 返回dishes
注意：这里food ingredient有数量



https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=465952







第一轮 上机写了一个react的UI，从一个API获取数据，然后展示出来。先讨论了下能用数据展示什么，然后写了一个简单的表格……



第二轮 设计，有害虫数据（如果当地气温在这个range里持续多长时间，那么认为这个害虫出现的概率很大）和一个获取地点气温的API（只有实时数据），如何设计一个系统，以及这个系统可以做什么

首先我们有全国的农场信息，我们可以通过每隔1h从那个天气API获得农场气温，然后存在DB里边。然后我们有个batch或者offline process去根据害虫表格里的信息，推测出哪里已经有虫害，哪里快要有虫害。这样就可以提醒农场。以及，我们也可以存全国的信息，来指出哪里适合建农场之类的。



第三轮 一个2d int array，问任意一点是否可以走到数字为0的地方，只能往四个方向走，只能往比当前数字小的格子走

https://www.1point3acres.com/bbs/thread-439013-1-1.html



===========



https://shawnlincoding.wordpress.com/2015/03/16/palantir%E9%9D%A2%E7%BB%8F/