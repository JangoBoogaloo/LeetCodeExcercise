from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def _count_nodes(head: Optional[ListNode]) -> int:
        count, curr = 0, head
        while curr:
            count += 1
            curr = curr.next
        return count

    @staticmethod
    def _reverse_return_heads(current: Optional[ListNode], k: int) -> tuple[Optional[ListNode], Optional[ListNode]]:
        prev = None
        for _ in range(k):
            current.next, prev, current = prev, current, current.next
        return prev, current

    def _reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = self._count_nodes(head)
        dummy = prev_tail = ListNode()  # the new list to insert to
        current_head = head
        next_tail = head
        for _ in range(count // k):
            new_head, next_head = self._reverse_return_heads(current_head, k)
            prev_tail.next = new_head
            prev_tail = next_tail
            next_tail = next_head
            current_head = next_head
        prev_tail.next = next_tail
        return dummy.next

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self._reverseKGroup(head, 2)
