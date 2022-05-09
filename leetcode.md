# [0003]无重复字符的最长子串
给定一个字符串 $s$ ，请你找出其中不含有重复字符的 最长子串 的长度。
示例 1:
```
输入: s = "abcabcbb"
输出: 3 
```
```python
def lengthOfLongestSubstring(s):
    charSet = set()
    i = j = 0
    maxLen = 0
    while j < len(s):
        while s[j] in charSet:
            charSet.remove(s[i])
            i += 1
        while j < len(s) and s[j] not in charSet:
            charSet.add(s[j])
            j += 1
        maxLen = max(maxLen, j - i)
    return maxLen
```

```python
def lengthOfLongestSubstring(s):
    idxMap = {}
    i = 0
    maxLen = 0
    for j in range(len(s)):
        i = max(idxMap.get(s[j], -1) + 1, i)
        maxLen = max(maxLen, j - i + 1)
        idxMap[s[j]] = j
    return maxLen
```



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

