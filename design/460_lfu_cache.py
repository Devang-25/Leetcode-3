from collections import defaultdict


class Node(object):

  def __init__(self, key, val):
    self.key = key
    self.val = val
    self.freq = 1

    self.prev = None
    self.next = None


class LFUCache(object):

  def __init__(self, capacity):
    """
        :type capacity: int
        """
    self.address_dict = defaultdict()  #{key: node}
    self.freq_dict = defaultdict()  #{freq:(head, tail)}
    self.min_freq = 0
    self.count = 0
    self.capacity = capacity

  def get(self, key):
    """
        :type key: int
        :rtype: int
        """
    # print("get key:{}".format(key))
    if key not in self.address_dict:
      return -1

    node = self.address_dict[key]
    # pop node from its original linked list
    self._pop(node)
    # update its freq += 1
    node.freq += 1
    # add it to its new linked list
    self._add(node, node.freq)

    # print("get key{} val{}".format(node.key, node.val))
    return node.val

  def put(self, key, value):
    """
        :type key: int
        :type value: int
        :rtype: None
        """
    # if reach capacity
    if self.capacity == 0:
      return

    if key in self.address_dict:
      node = self.address_dict[key]
      node.val = value

      self._pop(node)
      node.freq += 1
      self._add(node, node.freq)

    else:
      #
      if self.count == self.capacity:
        print("count exceed")
        while self.min_freq not in self.freq_dict:
          self.min_freq += 1
        freq = self.min_freq
        head, tail = self.freq_dict[freq]
        node = head.next
        # print("plan to evict node key{} val{}".format(node.key, node.val))

        self._pop(node)

        # clean up dict
        del self.address_dict[node.key]

        self.count -= 1

      # print("put key:{}, value{}".format(key, value))
      node = Node(key, value)
      self.address_dict[key] = node

      # add new node into freq_dict[1]
      self._add(node, 1)
      self.min_freq = 1
      self.count += 1

  def _pop(self, node):
    """
        pop a node from a linked list
        """
    pre = node.prev
    nxt = node.next

    pre.next = nxt
    nxt.prev = pre

    self._clean_freq_dict(node.freq)

  def _clean_freq_dict(self, freq):
    head, tail = self.freq_dict[freq]
    node = head.next
    if not node.key and not node.val:
      del self.freq_dict[freq]

  def _add(self, node, freq):
    """
        add a node to the given freq linked list
        """
    if not node.freq in self.freq_dict:
      self._create_linked_list(node.freq)

    try:
      head, tail = self.freq_dict[freq]
    except KeyError:
      print(self.freq_dict.keys())

    pre = tail.prev
    pre.next = node
    node.prev = pre

    node.next = tail
    tail.prev = node

  def _create_linked_list(self, freq):
    """
        create a linked list with head and tail
        """
    head = Node(None, None)
    tail = Node(None, None)
    head.next = tail
    tail.prev = head
    self.freq_dict[freq] = (head, tail)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)