from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return head
        right = right - left + 1
        left -= 1

        before_left = None
        left_node = head
        for _ in range(left):
            before_left = left_node
            left_node = left_node.next

        curr = left_node
        prev = None
        for _ in range(right):
            curr_next = curr.next
            curr.next = prev
            prev = curr
            curr = curr_next

        if before_left:
            before_left.next = prev
        else:
            head = prev

        left_node.next = curr
        return head