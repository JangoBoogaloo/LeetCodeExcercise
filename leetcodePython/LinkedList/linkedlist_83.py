from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        prev = head
        current = head.next

        while current:
            if prev.val == current.val:
                prev.next = current.next
            else:
                prev = current
            current = current.next
        return head
