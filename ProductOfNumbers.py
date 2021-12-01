class ProductOfNumbers:
    Head = None

    def __init__(self):
        self.Head = Node(None)

    def add(self, num: int) -> None:
        New = Node(num)
        New.Previous = self.Head
        self.Head = New

    def getProduct(self, k: int) -> int:
        result = 1
        Local = self.Head
        for i in Range(k):
            result *= Local.Val
            Local = Local.Previous
        return result


class Node:
    Val = None
    Previous = None

    def __init__(self, val):
        self.Val = val

    def Link(self, previous):
        self.Previous = previous

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)