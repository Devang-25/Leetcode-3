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
