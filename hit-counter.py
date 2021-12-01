class Node:
    def __init__(self, val, timestamp):
        self.val = val
        self.timestamp = timestamp
        self.next = None


class DList:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.size = 0

    def append(self, node):
        self.size += 1
        if self.head is None:
            self.head = node
            self.tail = self.head
            return
        self.head.next = node
        self.head = node

    def removeTail(self):
        if self.tail is not None:
            self.size -= 1
            self.tail = self.tail.next

        if self.tail is None:
            self.head = self.tail


class HitCounter:

    def __init__(self):
        self.count = 0
        self.dList = DList()
        self.dList.append(Node(1, 0))

    def hit(self, timestamp: int) -> None:
        self.count += 1
        self.dList.append(Node(self.count, timestamp))

    def getHits(self, timestamp: int) -> int:
        while self.dList.tail and self.dList.tail.timestamp <= timestamp - 300:
            self.dList.removeTail()

        if not self.dList.tail:
            return 0

        return self.count - self.dList.tail.val + 1


hc = HitCounter()
hc.hit(2)
hc.hit(3)
hc.hit(4)
hc.getHits(300)
hc.getHits(301)
hc.getHits(302)
hc.getHits(303)
hc.getHits(304)
hc.hit(501)
hc.getHits(600)
hc.getHits(301)
