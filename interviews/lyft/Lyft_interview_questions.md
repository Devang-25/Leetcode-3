## Log entry Problem - Regex

\ #Log, log-entry, entry, regex, 



'''

[02/01/2014 5:7:8 + 0000] PUT /user/4342/riders/543534 HTTP1.1 304 chrom

\1. Type: 是PUT

\2. url就是http://xxx/xxx/x

\3. Status code 是304.

\4. User Id 就是user/xxxx/, xxxx部分就是user id

'''



```python
import collections
import re

def type_count(fin):
  """
  input fin: file_handler
  output results: dict{type: count}
  type: str
  count: int
  """
  command_dict = collections.defaultdict(int)
  for line in fin:
    command_type = line[26:30]
    command_dict[command_type] += 1
  return command_dict

def user_count(fin):
  """
  input fin: file_handler
  output url_dict: dict{url: count}
  url type: str
  count type: int
  """
  user_dict = collections.defaultdict(int)
  for line in fin:
    # m = re.match('.*/user/(\d\d\d\d)/.*', line)
    m = re.match(r'.*/user/(\d*)/.*', line)
    user_id = m.group(1)
    print(user_id)
    user_dict[user_id] += 1
    return user_dict


def url_count(fin):
  """
  input fin: file_handler
  output url_dict: dict{url: count}
  url type: str
  count type: int
  """
  url_dict = collections.defaultdict(int)
  for line in fin:
    print("line", line)
    m = re.match(r'.*(HTTPs?.*|www?.*)\s', line, re.IGNORECASE)
    url = m.group(1)
    print(url)
  return

    


fin = ['[02/01/2014 5:7:8 + 0000] PUT /user/4342/riders/543534 HTTP1.1 304 chrom', 
'[03/01/2014 5:7:8 + 0000] PUT /user/4342/riders/543534 http1.1 304 chrom',
'[02/01/2014 5:7:8 + 0000] PUT /user/4342/riders/543534 https1.1 304 chrom',
'[02/01/2014 5:7:8 + 0000] PUT /user/4342/riders/543534 www.1.1 304 chrom'
]

# user_count(fin)
url_count(fin)
```



Quite Notes: 



| a*a+a? | 0 or more, 1 or more, 0 or 1       |
| ------ | ---------------------------------- |
| .      | any character except newline       |
| \d     | digit (0-9)                        |
| \w     | (a-z), (A-Z), (0-9), underscore(_) |
| \s     | white space (space, tab, newline)  |
| \b     | Word boundary eg: get "4", (\b4\b) |
| ?      | 0 or 1 of previous character       |
| *      | 0 or more                          |
| +      | 1 or more                          |
| [abc]  | any of the three                   |

Cheatsheet link: 

https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285



Regex Try-out Board: 

https://regex101.com/r/cO8lqs/2

https://regexr.com/



Python Regex Document:

https://docs.python.org/2/library/re.html#re.match

==========

## Design Log Storage System



```Python
"""
635. Design Log Storage System
Medium
119
53
Favorite
Share
You are given several logs that each log contains a unique id and timestamp. Timestamp is a string that has the following format: Year:Month:Day:Hour:Minute:Second, for example, 2017:01:01:23:59:59. All domains are zero-padded decimal numbers.

Design a log storage system to implement the following functions:

void Put(int id, string timestamp): Given a log's unique id and timestamp, store the log in your storage system.


int[] Retrieve(String start, String end, String granularity): Return the id of logs whose timestamps are within the range from start to end. Start and end all have the same format as timestamp. However, granularity means the time level for consideration. For example, start = "2017:01:01:23:59:59", end = "2017:01:02:23:59:59", granularity = "Day", it means that we need to find the logs within the range from Jan. 1st 2017 to Jan. 2nd 2017.

Example 1:
put(1, "2017:01:01:23:59:59");
put(2, "2017:01:01:22:59:59");
put(3, "2016:01:01:00:00:00");
retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Year"); // return [1,2,3], because you need to return all logs within 2016 and 2017.
retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Hour"); // return [1,2], because you need to return all logs start from 2016:01:01:01 to 2017:01:01:23, where log 3 is left outside the range.
Note:
There will be at most 300 operations of Put or Retrieve.
Year ranges from [2000,2017]. Hour ranges from [00,23].
Output for Retrieve has no order required.


Thought:
Q1: What data storage shoud I use:
1. tree - worst case o(n)
2. list - worst case o(n)
- So just use list would be easier.
- Don't use dictionary, becuse you might loose the number of timestamp

Q2: How should I get the time range I want given start and end?
- timestemp is str format.
- so create a dictionary to remember how many str need to cover up to if a level/granula of time is given;
    eg: up to year: first 4 (0:5);
        up to day: first 7 (0:8);...
- create the dictionary in a another class, so you only have to create it once
- So if people keep creating new LogSystem objects, the Index object is already created previously, and would not created again even new LogSystem is created again and agin.

Q3: So what to do when a retrieve is requested:
- use the index dictionary to cut the timestamps, including: start, end, and timestamp in the list:
- if start <= timestam <= end, return the id of that timestamp.


"""

class Index:
    def __init__(self):
        self.index = {"Year": 5,
              "Month": 8,
              "Day": 11,
              "Hour": 14,
              "Minute": 17,
              "Second": 19}

class LogSystem:

    def __init__(self):
        self.cache = []


    def put(self, id, timestamp):
        """
        :type id: int
        :type timestamp: str
        :rtype: void
        """
        self.cache.append((id, timestamp))


    def retrieve(self, s, e, gra):
        """
        :type s: str
        :type e: str
        :type gra: str
        :rtype: List[int]
        """
        level = Index().index[gra]
        start = s[:level]
        end = e[:level]
        results = [id for id, ts in self.cache if start <= ts[:level] <= end]
        return results



# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)
```



=========

## Output Last N Rows of File



```Python
"""
given a file or file_handler.

Implement a function that:
tail(file, n =10): #default n = 10
- give last 10 rows of line in the file

tail(file, n):
- give last n rows of lines in the file


Thought:
- since we need to read the file line by line:
- but we only want to last n rows of file
- so we wish to pop out / throw away for unwanted lines at the front
- thus we need to use queue. --> import collections.deque
- queue data structure: first in, first out.

2 Queue options in python:
1. queue.Queue  # different threads to communicate using queued messages/data
2. collections.deque  # used as datastructure

** Note: collections.deque is an alternative implementation of unbounded queues with fast atomic append() and popleft() operations that do not require locking

"""

import collections

def tail(fin, n=10):
    """
    input fin: file_handler
    input n: int # last n rows
    ouput: print out the last n rows of file
    """
    cache = collections.deque()
    for line in fin:
        cache.append(line)
        if len(cache) > n:
            cache.popleft()

    for l in cache:
        print(l)


fin = ["I love u", "i want to eat", "i want to"]

tail(fin, n=2)

```

=================

## Cipher Ceasar



```Python
'''
Ceasar Cipher   简单说就是   abc  + 2  --> cde,  xyz + 2 -->  zab  
- 不是字母不变 
- 区分大小写  
要求编译通过运行
'''

import re
import string

def cipher(code, num):
  letters = string.ascii_letters
  # abc....ABC

  result = ""
  for w in code:
    print("word", w)
    if w in letters:
      i = letters.index(w)
      result += letters[i+num]
      print("1", result)
    else:
      result += w
      print("2", result)
  
  return result

a = cipher("Ac_d", 2)
print(a)
```

===========

## Kth bigges element in list

```Python
"""
find the kth biggest number in the list

Thougt: 

data structure? 
- Heap

Algorithm		Average	Worst case
Space		O(n)	O(n)
Search		O(n)	O(n)
Insert		O(1)	O(log n)
Delete		O(log n)	O(log n)
Peek		O(1)	O(1)

So, make a heap with k element. 
1. insert k ele into the heap: O(K), worst case: O(KlogK) # linear time for heapq library in Python
2. insert k+1...nth element into the tree: each O(logn)
"""

import heapq

def kth_biggest(nums, k):
  """
  input nums: list
  input k: int
  output: if nums, ouput int
  if not nums: return None
  """
  if not nums:
    return None
  myheap = nums[:k] # implement myheap as a list
  heapq.heapify(myheap) # heapify the list
  for i in range(k, len(nums)):
    heapq.heappush(myheap, nums[i])
  return myheap[0]

nums = []
k = 5
print(kth_biggest(nums, k))

```

=========



## Uniform Probabiliy of list with repeated numbers



```Python
"""
Question: 
given a list and a target number
give all the index of this number in the list, return one of them with uniform probablity

Thougt:
if list is acending order:
  - binary search for the target number
  - O(log(N))

if list is not in order:
  - O(N)

- random.choice(O(1))
"""

import random

print(random.choice([1, 2, 3]))

# def uniform_location_choice(nums, target):
#   """
#   input nums: list[int]
#   input target: int
#   output: int
#   """
#   candidate = []
  
#   # binary search - find right bound
#   l = 0
#   r = len(nums) - 1
#   while l <= r:
#     mid = (l + r) // 2
#     if nums[mid-1] == target:
#       break
#     elif target < nums[mid]:
#       r = mid - 1
#     else:
#       l = mid + 1
#   return (mid - 1)
  
# nums = [1, 2, 2, 2, 4, 5]
# target = 2
# print(uniform_location_choice(nums, target))
```

=======



## Driving time violation

```Python
"""
- write a function to determinte whether a driver is allowed to enter a drive mode

- drive is NOT allowed to drive a total of 12 hours without 8 hours break

- input: a list of driver shrifts as [[start, end], [start, end]]
- the star and end time are integers relative lyft launch

- input current time: int, time since lyft launch

return bool


+++++++++++++

True example:
# 9 hours break, 1 hour drive, 2 hours break, 10 hours driver
# history = [(9, 10), (12, 22)]
cur_time = 24


"""

# brutal force:
def can_drive(history, cur_time):
  drive = 0
  i = len(history) - 1
  last_start = cur_time
  while i >= 0:
    rest = last_start - history[i][1]
    drive += history[i][1] - history[i][0]
    if rest >= 8:
      return True
    if drive >= 12:
      return False
    last_start = history[i][0]
    i -= 1
  return True
  # while rest < 8 or drive < 12:



history = [(9, 10), (12, 22)]
current_time = 24
# True

# history = [(0,4), (5, 9), (10, 14), (15, 19), (20, 24)]
# current_time = 24
# False

print(history)
print(can_drive(history, current_time))	
```



======

## Search in a roated array II

```Python
"""
81. Search in Rotated Sorted Array II
Medium
463
228
Favorite
Share
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

"""


"""
Since there is repetition of digit happens here,
so there might be cases where there is not sufficient information to choose which half to search.

Thus we divide into three scenario:
1. left half if ascending
2. rotating happen if the left half
(the alternative nums[r] >= nums[mid] ### MUST be equal to as well
### nums[r] > nums[mid] will not work
b/c
right side might be all same numbers, which is not ascending,
eg: [1, 3, 1, 1, 1])
3. information loss in cases [1, 3, 1, 1, 1]:
so increment left += 1 and search again.

"""

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l = 0
        r = len(nums) - 1
        #print("e", r)
        while l <= r:
          mid = (l + r) // 2
          if target == nums[mid]:
            return True
          # if left is the aseceinding half
          elif nums[l] < nums[mid]:
            if nums[l] <= target < nums[mid]:
              r = mid - 1
            else:
              l = mid + 1
          # if the rotating happen on the left half:
          elif nums[l] > nums[mid]:
          # elif nums[r] >= nums[mid]:
            if nums[mid] < target <= nums[r]:
              l = mid + 1
            else:
              r = mid - 1
          # example for this case: [1, 3, 1, 1, 1]
          # else there is information loss:
          # l = mid -> not sure which half to check
          # increement l += 1 until there is new information
          else:
            l += 1
        return False


# nums = [3, 1, 1]
# target = 3

nums = [1,3,1,1,1]
target = 3
s = Solution().search(nums, target)
print(s)
```





=================

## Common Element of Iterator



```Python
"""
Question:

arr1 = [1, 2, 4, 8]
arr2 = [2, 8, 9]

return [2, 8]
"""

# build a iterator-like object
class myIter:
    def __init__(self, arr):
        self.arr = arr
        self.i = 0

    def has_next(self):
        return self.i < len(self.arr)

    def next(self):
        """
        when object.next() is called,
        return the next ele in the iterable
        if no next: raise Error (that is the behavior of iterable)
        """
        cur = self.arr[self.i]
        self.i += 1
        return cur


#######################

arr1 = [1, 2, 4, 8]
object1 = myIter(arr1)
results = []
while object1.has_next():
  results.append(object1.next())
print(results)
print(bool(results == [1, 2, 4, 8]))


########################
# build a CommonElement class that has 1) next and has_next fuction for iterators

class commonElement:
  def __init__(self, arr1, arr2):
    """
    input: 2 list or array, turn them into interator using class myInter
    """
    self.arr1 = myIter(arr1)
    self.arr2 = myIter(arr2)

    # self.arr1 and self.arr2 has behaviro of an iterators
    # call its next value by arr.next()
    self.v1 = self.arr1.next()
    self.v2 = self.arr2.next()

    # keep track of the next_common_ele
    self.next_common_ele = self._find_next()

  def _find_next(self):
    while self.v1 is not None and self.v2 is not None:
      # find common element
      if self.v1 == self.v2:
        cur = self.v1
        self.v1 = self.arr1.next() if self.arr1.has_next() else None
        self.v2 = self.arr2.next() if self.arr2.has_next() else None
        return cur
      # if v2 is smaller, move the curser of v2 to arr2.next()
      elif self.v1 > self.v2:
        self.v2 = self.arr2.next() if self.arr2.has_next() else None
      else: # self.v1 < self.v2: move the arr1.next()
        self.v1 = self.arr1.next() if self.arr1.has_next() else None

  def next(self):
    """
    return the next ele if has
    raise error message if not (behavior of iterable)
    """
    if self.next_common_ele is None:
      raise Exception("Iterator has reached the end")

    cur = self.next_common_ele
    self.next_common_ele = self._find_next()
    return cur


  def has_next(self):
    # return bool(self.next_common_ele != None)
    return self.next_common_ele is not None

########################

arr1 = [1, 2, 4, 8]
arr2 = [2, 8, 9]
object2 = commonElement(arr1, arr2)
print("1", object2.next())
print("2", object2.has_next())
print("3", object2.has_next())
print("4", object2.next())
print("5", object2.has_next())
print("6", object2.next())

########################

```

============



## Asteroid Collision

```Python
class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        
        for star in asteroids:
            #print("star", star)
            if star > 0:
                stack.append(star)
            else:
                while stack and stack[-1] > 0 and abs(star) > stack[-1]:
                    stack.pop()
                if not stack or stack[-1] < 0:
                    stack.append(star)
                elif stack[-1] == abs(star):
                    stack.pop()
                # below two lines does not work:
                # reason: there might not be any asteroid in the stack:
                # thus, if stack[-1] before "not stack", 
                # then there might be error.
                # if always check for "not stack" first, 
                # then no problem.
                
                # if stack[-1] == abs(star):
                #     stack.pop()
                # elif (not stack) or (stack[-1] < 0) :
                #     stack.append(star)
        return(stack)
```

========



## Trapping Rain Water

```python
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        
        **Thought:
        
        Q: which bound matter? 
        - only the lower of (left_bound, right_bound) matter to how much water trap at a piont
        - so, you have two pointers: i, j, keep track of left-bound and right bound respectively.
        - move i or j whichever one is the lower bound. (i++, j--)
        
        Q: How much water trap:
        - water = max(0, lower_bound - height)
        - if height is higher than lower_bound, no water trap
        
        Q: When do you update the amount of water trap:
        - you update the amoutn of water trap at height[i] when you pointer is that that place. 
        - so, after you update the water trap at height[i], you move the pointer forward or backward depend on which point you move (i++, j--)
        
        Q: When do you stop update:
        - Since you only update the water at a place when you about the move that pointer forward or backward, 
        - so you update until i surpass j. (water at height[i] is only updated when a pointer i or j surpass it, NOT when the pointer is at it.)
        
        
        """
        i = 0
        j = len(height) - 1
        left_bound = 0
        right_bound = 0
        total = 0
        while i < len(height) and j > 0 and i <= j:
            #print("i", i, "j", j)
            if height[i] <= height[j]:
                # the amount of the water can hold: lower_bound - height
                total += max(0, left_bound - height[i])
                # update the bound
                left_bound = max(left_bound, height[i])
                # move pointer
                i += 1
            elif height[i] > height[j]:
                total += max(0, right_bound - height[j])
                right_bound = max(right_bound, height[j])
                j -= 1
        return total
        
        
#     def trap(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#           time complexity: O(N)    
#         """
#         left = [0] * len(height)
#         right = [0] * len(height)
#         total = 0
#         for i in range(1, len(height)):
#             left[i] = max(left[i-1], height[i-1])
#         for j in range(len(height)-2, -1, -1):
#             right[j] = max(right[j+1], height[j+1])
#         for k in range(len(height)):
#             lower_bound = min(left[k], right[k])
#             water = max(0, lower_bound - height[k])
#             total += water
#         return total
    

        
```



========



## Number of Islands

```python
class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def sink(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == "1":
                grid[i][j] = "0"
                a = list(map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1)))
                return(1)
            return(0)
                
        return(sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i]))))
```



========



## Number of Distinct Islands



```Python
class Solution:
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        def find_island(i, j, island, x, y):
            """
            input i: int, index of current cell
            input j: int, index of current cell
            input island: list
            """
            if 0 <= i < rows and 0 <= j < cols and grid[i][j]:
                # island.append('%d,%d' % (x-i, y-j))
                island.append((x-i, y-j))
                grid[i][j] = 0
                find_island(i+1, j, island, x, y)  # right
                find_island(i, j+1, island, x, y)  # down
                find_island(i-1, j, island, x, y)  # left
                find_island(i, j-1, island, x, y)  # up
                return island
        
        def if_new_island(island):
            island = tuple(island)
            # island = ','.join(island)
            if island not in islands:
                islands.add(island)

        cell_to_islands = {}
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:  # is island
                    island = find_island(i, j, [], i, j)
                    # if_new_island(island)
                    
                    cells = len(island)
                    if cells in cell_to_islands:
                        cell_to_islands[cells].append(island)
                    else:
                        cell_to_islands[cells] = [island]
        
        unique_count = 0
        for cell, islands in cell_to_islands.items():
            if len(islands) == 1:
                unique_count += 1
            else:
                unique_count += len(set(tuple(island) for island in islands))
        return unique_count
```

