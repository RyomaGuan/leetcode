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


# [0053]最大子数组和
给你一个整数数组 $nums$ ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
子数组 是数组中的一个连续部分。
示例 1：
```
输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
```
```python
def maxSubArray(nums):
    total = maxTotal = nums[0]
    for num in nums[1:]:
        total = max(0, total) + num
        maxTotal = max(maxTotal, total)
    return maxTotal
```

# [0021]合并两个有序链表
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
```python
def mergeTwoLists(list1, list2):
    head = p = ListNode()
    p1, p2 = list1, list2
    while p1 and p2:
        if p1.val < p2.val:
            p.next = p1
            p1 = p1.next
        else:
            p.next = p2
            p2 = p2.next
        p = p.next
    p.next = p1 if p1 else p2
    return head.next
```

```python
def mergeTwoLists(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1
    if list1.val < list2.val:
        list1.next = mergeTwoLists(list1.next, list2)
        return list1
    else:
        list2.next = mergeTwoLists(list1, list2.next)
        return list2
```


# [0146]LRU 缓存
请你设计并实现一个满足 $LRU$ (最近最少使用) 缓存约束的数据结构。实现 $LRUCache$ 类：
- $LRUCache(int capacity)$ 以 正整数 作为容量$ capacity$ 初始化 $LRU$ 缓存
- $int get(int key)$ 如果关键字 $key$ 存在于缓存中，则返回关键字的值，否则返回 -1 。
- $void put(int key, int value)$ 如果关键字 $key$ 已经存在，则变更其数据值 $value$ ；如果不存在，则向缓存中插入该组 $key-value$ 。如果插入操作导致关键字数量超过 $capacity$ ，则应该 逐出 最久未使用的关键字。
- 函数 $get$ 和 $put$ 必须以 $O(1)$ 的平均时间复杂度运行。
```python
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.pre = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node("#", -1)
        self.tail = Node("#", -1)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.key2node = dict()

    def get(self, key: int) -> int:
        if key not in self.key2node:
            return -1
        # 移除结点
        node = self.key2node[key]
        node.pre.next = node.next
        node.next.pre = node.pre
        # 放置头部
        self.head.next.pre = node
        node.next = self.head.next
        self.head.next = node
        node.pre = self.head
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.key2node and len(self.key2node) == self.capacity:
            # 移除尾结点
            tailNode = self.tail.pre
            tailNode.pre.next = tailNode.next
            tailNode.next.pre = tailNode.pre
            self.key2node.pop(tailNode.key)

        if key in self.key2node:
            # 修改结点
            node = self.key2node[key]
            node.value = value
            # 移除结点
            node.pre.next = node.next
            node.next.pre = node.pre
        else:
            self.key2node[key] = Node(key, value)

        # 放置头部
        node = self.key2node[key]
        self.head.next.pre = node
        node.next = self.head.next
        self.head.next = node
        node.pre = self.head
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

# [0215]数组中的第K个最大元素
给定整数数组 $nums$ 和整数 $k$，请返回数组中第 $k$ 个最大的元素。
请注意，你需要找的是数组排序后的第 $k$ 个最大的元素，而不是第$ k$ 个不同的元素。
示例 1:
```
输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
```
```python
def partition(left, right, nums):
    i, baseNum = left, nums[right]
    # < baseNum 右边界, > baseNum 左边界
    l, r = left - 1, right + 1
    while i < r:
        if nums[i] == baseNum:
            i += 1
        elif nums[i] < baseNum:
            l += 1
            nums[l], nums[i] = nums[i], nums[l]
            i += 1
        else:
            r -= 1
            nums[i], nums[r] = nums[r], nums[i]
    return l + 1, r - 1


def findKthLargest(nums, k: int) -> int:
    # 返回值的索引
    k = len(nums) - k
    # 快排的左右边界
    left, right = 0, len(nums) - 1
    # 已排序的左右边界
    l, r = partition(left, right, nums)
    while not l <= k <= r:
        if k < l:
            right = l - 1
        else:
            left = r + 1
        l, r = partition(left, right, nums)
    return nums[k]
```