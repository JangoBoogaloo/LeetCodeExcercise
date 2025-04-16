from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def _get_middle(head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    @staticmethod
    def _reverse(head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head
        while current:
            current.next, previous, current = previous, current, current.next
        return previous

    def _adjacent_merge(self, head1: Optional[ListNode], head2: Optional[ListNode]):
        while head1 and head2:
            next1 = head1.next
            next2 = head2.next
            # head1 -> head2 ->
            head1.next = head2
            head2.next = next1
            head1 = next1
            head2 = next2

    def reorderList(self, head: Optional[ListNode]) -> None:
        middle = self._get_middle(head)
        reverse_middle = self._reverse(middle.next)
        middle.next = None
        self._adjacent_merge(head, reverse_middle)
