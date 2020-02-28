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

REASON for 2. always PUT an item to the end of the linked list:
- head: older nodes - least recenlty used
- tail: recently used (get or put) nodes
- always add newly PUT and newly GET node at the end of the linked list, so when we need to evict/eleminate certain element from the head, we alwasy evict / eliminate the least recently used node which are those closer to the head of the linked list.

所以，当我们GET一个node时，我们需要把它从原来的linked list里_remove 和 _add到linked list的尾部. 这样的话，我们就知道它最近被提取过，不会被删掉。

当我们需要PUT一个node时，我们需要考虑两点：
1）这个node是否已存在现在的Linked List里：查看dict
2）现在的capacity 够不够： 查看len(dict)
（如果这个节点已经存在在现在的链接里:那么不用担心capacity不够，因为肯定会删掉一个再加如新的；
但是这个节点没有存在在现在的链接里:那么的话，新增加的节点有可能导致exceed capacity.)

1-如果node没有存在：
· 加到现在dict
. 添加到现在的linkdlist的尾部

1-如果node已经存在：
- 从现有的 Linked list 里删除
- 更新字典里的value

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
        """
        remove the node by:
        connect the node.previous with the node.next
        """
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
