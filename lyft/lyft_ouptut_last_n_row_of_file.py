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
