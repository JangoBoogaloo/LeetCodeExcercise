from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SolutionRecursive:
    @staticmethod
    def _reverse(begin: Optional[ListNode], after_end: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = begin
        while curr != after_end:
            curr_next = curr.next
            curr.next = prev
            prev = curr
            curr = curr_next
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        curr = head
        for _ in range(k):
            if not curr:
                return head
            curr = curr.next
        after_end = curr
        begin = head
        new_head = self._reverse(begin, after_end)
        begin.next = self.reverseKGroup(after_end, k)
        return new_head