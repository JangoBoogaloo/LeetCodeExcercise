from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def _countNodes(head: Optional[ListNode]) -> int:
        count = 0
        while head:
            count += 1
            head = head.next
        return count

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        nodeCount = self._countNodes(head)
        iterateCount = nodeCount - (k % nodeCount)
        current = head
        prev = current
        for _ in range(iterateCount):
            prev = current
            current = current.next
        prev.next = None
        if not current:
            return head
        newHead = current
        tail = None
        while current:
            tail = current
            current = current.next
        tail.next = head
        return newHead
