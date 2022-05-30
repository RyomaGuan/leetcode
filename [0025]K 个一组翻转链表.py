# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head, k: int):
        nextHead = head
        i = 0
        while nextHead != None and i != k:
            nextHead = nextHead.next
            i += 1
        if i != k:
            return head
        pre, cur = head, head.next
        i = 1
        while i < k:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
            i += 1
        head.next = self.reverseKGroup(nextHead, k)
        return pre
