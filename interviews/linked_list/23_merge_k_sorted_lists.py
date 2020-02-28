"""
23. Merge k Sorted Lists
Hard
1701
106


Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6

"""


#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # print('total len', len(lists))

        def merge2lists(list1, list2):
            # print("list1", list1.val)
            # print("list2", list2.val)
            head = cur = ListNode(0)
#             while (list1 != None) or (list2 != None):
            while list1 or list2:
#                 if (list2 == None):
                if (list2 == None):
                    #print("no list2")
                    cur.next = list1
                    list1 = list1.next
                    cur = cur.next
                elif (list1 == None):
                    #print("no list1")
                    cur.next = list2
                    list2 = list2.next
                    cur = cur.next
                elif (list1.val <= list2.val):
                    #print("list1.val <= list2.val")
                    cur.next = list1
                    list1 = list1.next
#                     print(list1.val, list2.val)
                    cur = cur.next
                elif (list1.val > list2.val):
                    #print('list1.val > list2.val')
                    cur.next = list2
                    list2 = list2.next
                    cur = cur.next
                #print("merge2list")
                # self.dprint(head.next)
            return head.next

        def dp(lists):
            n = len(lists)
            # print("n", n)
            if n == 0:
                return []
            elif n == 1:
                # print("1 list only", lists[0].val)
                # print("type", type(lists), type(lists[0]))
                return lists[0]
            elif n == 2:
                # print("2")
                # self.dprint(lists[0])
                # self.dprint(lists[1])
                return merge2lists(lists[0], lists[1])
            elif len(lists) >= 3:
                left = dp(lists[:len(lists) // 2])
                right = dp(lists[len(lists)//2 :])
                return merge2lists(left, right)
#                 self.dprint(left)
#                 self.dprint(right)
                # return merge2lists(dp(lists[:len(lists) // 2]), dp(lists[len(lists)//2 :]))

        return dp(lists)

    # def dprint(self, head):
    #     node = head
    #     print("new list")
    #     while node:
    #         print(node.val)
    #         node = node.next


#######################

a = ListNode(1)
b = ListNode(4)
c = ListNode(2)
d = ListNode(5)
e = ListNode(3)
f = ListNode(6)


a.next = b
c.next = d
e.next = f

#################

s = Solution()
s.dprint(a)
s.dprint(c)

#############

head = s.mergeKLists([a, c, e])
s.dprint(head)
