class Node:
    def __init__(self, key, val, fre = 1):
        self.val = val
        self.key = key
        self.fre = fre
        self.pre = None
        self.next = None


class DoubleLinkList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = self.head

    def add(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            self.size += 1
            return

        node.pre = self.head
        self.head.next = node
        self.head = node
        self.size += 1

    def remove(self, node):
        if node.pre and node.next:
            node.pre.next = node.next
            node.next.pre = node.pre
            self.size -= 1
            return
        if node.pre:
            self.head = node.pre
            self.head.next = None
            self.size -= 1
            return
        if node.next:
            self.tail = node.next
            self.tail.pre = None
            self.size -= 1
            return
        self.head = None
        self.tail = self.head
        self.size = 0


class LFUCache:
    def __init__(self, capacity: int):
        self.minFre = 1
        self.capacity = capacity
        self.frequencyDlist = {}
        self.hashMap = {}

    def update(self, node):
        dList = self.frequencyDlist.get(node.fre)
        dList.remove(node)
        if node.fre == self.minFre and dList.size == 0:
            self.minFre += 1
        node.fre += 1
        dList = self.frequencyDlist.get(node.fre, None)
        if not dList:
            dList = DoubleLinkList()
            self.frequencyDlist[node.fre] = dList
        node.pre = None
        node.next = None
        dList.add(node)
        self.hashMap[node.key] = node

    def get(self, key: int) -> int:
        if key not in self.hashMap:
            return -1

        node = self.hashMap.get(key)
        self.update(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return None

        if key in self.hashMap:
            node = self.hashMap.get(key)
            node.val = value
            self.update(node)
            return None

        if len(self.hashMap) == self.capacity:
            dList = self.frequencyDlist[self.minFre]
            node = dList.tail
            self.hashMap.pop(node.key, None)
            dList.remove(node)

        node = Node(key, value)
        self.hashMap[key] = node
        dList = self.frequencyDlist.get(1, None)
        if not dList:
            dList = DoubleLinkList()
            self.frequencyDlist[1] = dList
        dList.add(node)
        self.minFre = 1
        return None

LFU = LFUCache(3)
LFU.put(2, 2)
LFU.put(1, 1)
LFU.get(2)
LFU.get(1)
LFU.get(2)
LFU.put(3, 3)
LFU.put(4, 4)
LFU.get(3)
LFU.get(2)
LFU.get(1)
LFU.get(4)
