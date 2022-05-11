class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
#     def mergeTwoLists(self, list1, list2):
#         head = p = ListNode()
#         p1, p2 = list1, list2
#         while p1 and p2:
#             if p1.val < p2.val:
#                 p.next = p1
#                 p1 = p1.next
#             else:
#                 p.next = p2
#                 p2 = p2.next
#             p = p.next
#         p.next = p1 if p1 else p2
#         return head.next


class Solution:
    def mergeTwoLists(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
