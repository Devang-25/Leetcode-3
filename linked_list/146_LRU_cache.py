"""
146. LRU Cache
Hard
1983
61


Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

“”“

"""
The solution is:

1. Doulbe Linked List + Dict
2. always add an item to the end of the linked list
3. The dict will store: 1)key 2)address for that particular node at linked list


"""

class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int

        # if key not in dict: return -1
        # if key in dict:
            # remove it
            # add it again at the end of tail
        """
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add(node)
        # self.dprint()
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void

        # if key already in cache:
            # del it from linked list
            # del it from dict
        # if at capacity:
            # remove the node pointed by the head (head.next)
            # remove that node from dec
        # add the new (key, val)
        """
        if key in self.cache:
            self._remove(self.cache[key])
        elif len(self.cache) == self.cap:
            print("overload")
            old_node = self.head.next
            self._remove(old_node)
            del self.cache[old_node.key]

        new_node = Node(key, value)
        self._add(new_node)
        self.cache[key] = new_node
        # self.dprint()


    def _add(self, node):
        p = self.tail.prev
        p.next = node
        node.prev = p
        node.next = self.tail
        self.tail.prev = node

    def _remove(self, node):
        p = node.prev
        p.next = node.next
        node.next.prev = p

    # def dprint(self):
    #     node = self.head
    #     print("new list")
    #     while node:
    #         print(node.val)
    #         node = node.next

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
