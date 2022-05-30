# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
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
