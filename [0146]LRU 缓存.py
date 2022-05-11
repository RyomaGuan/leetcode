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
