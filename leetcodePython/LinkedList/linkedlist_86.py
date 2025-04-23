from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy_small = ListNode(-1)
        dummy_big = ListNode(-1)
        small = dummy_small
        big = dummy_big
        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                big.next = head
                big = big.next
            prev = head
            head = head.next
            prev.next = None
        small.next = dummy_big.next
        return dummy_small.next
