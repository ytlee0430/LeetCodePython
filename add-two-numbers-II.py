# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        v1, v2 = 0, 0
        while l1 is not None:
            v1 *= 10
            v1 += l1.val
            l1 = l1.next

        while l2 is not None:
            v2 *= 10
            v2 += l2.val
            l2 = l2.next

        value = v1 + v2
        result = ListNode()
        while value > 0:
            result.val = value % 10
            value //= 10
            if value == 0:
                break
            newResult = ListNode()
            newResult.next = result
            result = newResult

        return result
