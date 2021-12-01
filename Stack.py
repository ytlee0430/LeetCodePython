class node:
    def __init__(self, v):
        self.value = v
        self.max = v
        self.next = None
        pass


class stack:
    def __init__(self):
        self.node = None
        pass

    def push(self, v):
        if self.node is None:
            self.node = node(v)
            return
        n = node(v)
        n.max = max(self.node.max, v)
        n.next = self.node
        self.node = n

    def pop(self):
        if self.node is not None:
            num = self.node.value
            self.node = self.node.next
            return num
        return None

    def max(self):
        return self.node.max


s = stack()
s.push(4)
s.push(3)
s.push(2)
s.push(1)

print(s.max())
print(s.pop())

print(s.max())
print(s.pop())

print(s.max())
print(s.pop())

print(s.max())
print(s.pop())

