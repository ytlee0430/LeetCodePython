import threading
import time


class Node(object):
    def __init__(self, value: int):
        self.value = value
        self.pre = None
        self.next = None


class LockObject(object):
    def __init__(self):
        self.size = 0
        self.writeLock = threading.Lock()
        self.readLock = threading.Lock()


class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.head = None
        self.tail = self.head
        self.lock = LockObject()
        self.capacity = capacity

    def enqueue(self, element: int) -> None:
        self.lock.writeLock.acquire()
        while self.lock.size == self.capacity:
            time.sleep(1/1000)
        if self.head is None:
            self.head = Node(element)
            self.tail = self.head
            self.lock.size += 1
            self.lock.writeLock.release()
            return
        node = Node(element)
        self.head.next = node
        node.pre = self.head
        self.head = node
        self.lock.size += 1
        self.lock.writeLock.release()

    def dequeue(self) -> int:
        self.lock.readLock.acquire()
        while self.lock.size <= 0:
            time.sleep(1/1000)

        r = self.tail.value
        self.tail = self.tail.next
        if self.tail:
            self.tail.pre = None
        else:
            self.head = self.tail
        self.lock.size = self.lock.size - 1
        self.lock.readLock.release()
        return r

    def size(self) -> int:
        return self.lock.size


def write():
    queue.enqueue(1)
    queue.enqueue(0)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)


def read():
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()


queue = BoundedBlockingQueue(2)
writeThread = threading.Thread(target=write)
readThread = threading.Thread(target=read)

writeThread.start()
readThread.start()
writeThread.join()
readThread.join()


queue.size()
