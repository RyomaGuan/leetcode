# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


# class Solution:
#     def levelOrder(self, root: TreeNode):
#         if root == None:
#             return []
#         dq = deque([root])
#         ans = []
#         lst = []
#         last = nLast = root
#         while len(dq) > 0:
#             cur = dq.popleft()
#             lst.append(cur.val)
#             if cur.left != None:
#                 dq.append(cur.left)
#                 nLast = cur.left
#             if cur.right != None:
#                 dq.append(cur.right)
#                 nLast = cur.right
#             if cur == last:
#                 ans.append(lst)
#                 lst = []
#                 last = nLast
#         return ans

class Solution:
    def levelOrder(self, root: TreeNode):
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