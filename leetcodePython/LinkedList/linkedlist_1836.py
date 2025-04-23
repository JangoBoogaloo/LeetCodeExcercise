from typing import Optional
from collections import Counter


class ListNode:
    def __init__(self, x=0):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicatesUnsorted(self, head: Optional[ListNode]) -> Optional[ListNode]:
        valueCount = Counter()
        node = head

        while node:
            valueCount[node.val] += 1
            node = node.next

        dummyHead = ListNode()
        dummyHead.next = head
        prev = dummyHead
        current = head

        while current:
            if valueCount[current.val] > 1:
                prev.next = current.next
                current.next = None
                current = prev
            prev = current
            current = current.next

        return dummyHead.next
