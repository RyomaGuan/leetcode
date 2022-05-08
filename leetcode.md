# [0206]反转链表
给你单链表的头节点 $head$ ，请你反转链表，并返回反转后的链表。
示例 1：

<img src="https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg" alt="img" style="zoom: 67%;" />


```python
def reverseList(head):
    if head == None or head.next == None:
        return head
    newHead = reverseList(head.next)
    head.next.next = head
    head.next = None
    return newHead
```
```python
def reverseList(head):
    pre = None
    while head:
        next = head.next
        head.next = pre
        pre = head
        head = next
    return pre
```

