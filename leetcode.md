# [0001]两数之和
给定一个整数数组 $nums$ 和一个整数目标值 $target$，请你在该数组中找出和为目标值 $target$  的那两个整数，并返回它们的数组下标。
- 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
- 你可以按任意顺序返回答案。
```python
def twoSum(nums, target: int):
    num2idx = dict()
    for i in range(len(nums)):
        if target - nums[i] in num2idx:
            return [num2idx[target - nums[i]], i]
        else:
            num2idx[nums[i]] = i
```


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

# [0015]三数之和
给你一个包含 $n$ 个整数的数组 $nums$，判断 $nums$ 中是否存在三个元素 $a$，$b$，$c$ ，使得 $a + b + c = 0$ ？请你找出所有和为 0 且不重复的三元组。
- 答案中不可以包含重复的三元组。

示例 1：
```
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
```
```pyhton
def threeSum(nums):
    if len(nums) < 3:
        return []
    nums.sort()
    i = 0
    ans = []
    while i < len(nums) - 2 and nums[i] <= 0:
        j, k = i + 1, len(nums) - 1
        while j < k:
            if nums[j] + nums[k] > -nums[i]:
                k -= 1
            elif nums[j] + nums[k] < -nums[i]:
                j += 1
            else:
                ans.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
                while j < len(nums) and nums[j - 1] == nums[j]:
                    j += 1
                while k > i and nums[k + 1] == nums[k]:
                    k -= 1
        i += 1
        while i < len(nums) and nums[i] == nums[i - 1]:
            i += 1
    return ans
```


# [0025]K 个一组翻转链表
给你链表的头节点 $head$ ，每 $k$ 个节点一组进行翻转，请你返回修改后的链表。
$k$ 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 $k$ 的整数倍，那么请将最后剩余的节点保持原有顺序。
- 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

示例 1：

![img](leetcode.assets/reverse_ex1.jpg)
```
输入：head = [1,2,3,4,5], k = 2
输出：[2,1,4,3,5]
```
```python
def reverseKGroup(head, k: int):
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
    head.next = reverseKGroup(nextHead, k)
    return pre
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

# [0020]有效的括号
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 $s$ ，判断字符串是否有效。
有效字符串需满足：

- 左括号必须用相同类型的右括号闭合。
- 左括号必须以正确的顺序闭合。
```python
def isValid(s: str) -> bool:
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = list()
    for c in s:
        if c in pairs:
            if not stack or stack[-1] != pairs[c]:
                return False
            stack.pop()
        else:
            stack.append(c)
    return len(stack) == 0
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

# [0102]二叉树的层序遍历
给你二叉树的根节点 $root$ ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
示例 1：
![img](leetcode.assets/tree1.jpg)

```
输入：root = [3,9,20,null,null,15,7]
输出：[[3],[9,20],[15,7]]
```
```python
from collections import deque

def levelOrder(root: TreeNode):
    if root == None:
        return []
    dq = deque([root])
    ans = []
    while len(dq) > 0:
        i = len(dq)
        lst = []
        while i > 0:
            cur = dq.popleft()
            lst.append(cur.val)
            i -= 1
            if cur.left != None:
                dq.append(cur.left)
            if cur.right != None:
                dq.append(cur.right)
        ans.append(lst)
    return ans
```

```python
from collections import deque

def levelOrder(root: TreeNode):
    if root == None:
        return []
    dq = deque([root])
    ans = []
    lst = []
    last = nLast = root
    while len(dq) > 0:
        cur = dq.popleft()
        lst.append(cur.val)
        if cur.left != None:
            dq.append(cur.left)
            nLast = cur.left
        if cur.right != None:
            dq.append(cur.right)
            nLast = cur.right
        if cur == last:
            ans.append(lst)
            lst = []
            last = nLast
    return ans
```

# [0103]二叉树的锯齿形层序遍历
给你二叉树的根节点 $root$ ，返回其节点值的 锯齿形层序遍历 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
示例 1：
![img](leetcode.assets/tree1-20220524105241374.jpg)

```
输入：root = [3,9,20,null,null,15,7]
输出：[[3],[20,9],[15,7]]
```

```python
def zigzagLevelOrder(root: TreeNode):
    if not root:
        return []
    ans = []
    left2rightStack = list([root])
    right2leftStack = list()
    while len(left2rightStack) > 0 or len(right2leftStack) > 0:
        lst = []
        if len(left2rightStack) > 0:
            while len(left2rightStack) > 0:
                node = left2rightStack.pop()
                lst.append(node.val)
                if node.left:
                    right2leftStack.append(node.left)
                if node.right:
                    right2leftStack.append(node.right)
        else:
            while len(right2leftStack) > 0:
                node = right2leftStack.pop()
                lst.append(node.val)
                if node.right:
                    left2rightStack.append(node.right)
                if node.left:
                    left2rightStack.append(node.left)
        ans.append(lst)
    return ans
```




# [0141]环形链表
给你一个链表的头节点 $head$ ，判断链表中是否有环。
如果链表中有某个节点，可以通过连续跟踪 $next$ 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 $pos$ 来表示链表尾连接到链表中的位置（索引从 0 开始）。注意：$pos$ 不作为参数进行传递 。仅仅是为了标识链表的实际情况。
如果链表中存在环 ，则返回 $true$ 。 否则，返回 $false$ 。
示例 1：
![img](leetcode.assets/circularlinkedlist.png)

```
输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。
```

```python
def hasCycle(head) -> bool:
    p1 = p2 = head
    while p1 and p1.next:
        p1 = p1.next.next
        p2 = p2.next
        if p1 == p2:
            return True
    return False
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