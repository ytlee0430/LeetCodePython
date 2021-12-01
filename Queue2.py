class node:
    def __init__(self, v):
        self.value = v
        self.next = None
        pass


class queue:
    def __init__(self):
        self.head = None
        self.tail = None
        pass

    def push(self, v):
        if self.head is None:
            self.head = node(v)
            self.tail = self.head
            return
        self.tail.next = node(v)
        self.tail = self.tail.next

    def pop(self):
        if self.head is not None:
            num = self.head.value
            self.head = self.head.next
            return num
        return None


q = queue()

q.push(1)
q.push(2)
q.push(3)
q.push(4)

print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
