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
