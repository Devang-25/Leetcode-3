"""

24. Swap Nodes in Pairs
Medium
764
64


Given a linked list, swap every two adjacent nodes and return its head.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # corner case: [], None
        # only one node, head.next == None
        if (not head) or (not head.next):
            return head

        else:
            prev = head
            cur = prev.next
            new_head = cur
            post = cur.next
            self.dprint(new_head)

            while prev and cur:
                print("cur", cur.val, "prev", prev.val)
                cur.next = prev
                head.next = cur
                prev.next = post
                print("change dir")
                print("new_head", new_head.val)
                self.dprint(new_head)

                if post and post.next:
                    print("change pointer")
                    head = prev
                    cur = post.next
                    prev = prev.next
                    post = cur.next
                    print("new_head", new_head.val)
                    self.dprint(new_head)
                else:
                    break

        return new_head

    def dprint(self, head):
        node = head
        print("new list")
        while node:
            print(node.val)
            node = node.next

"""
Test:

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)

head = a
a.next = b
b.next = c
c.next = d

s = Solution()
# print the head just created
s.dprint(head)

# rearrange the head
s.swapPairs(head)

""""
