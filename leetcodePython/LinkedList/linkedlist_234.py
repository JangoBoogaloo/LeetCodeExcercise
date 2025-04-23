from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.next = next
        self.val = val


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        middle = fast = head
        # A -> B -> None return A
        # A -> B -> C -> None return B
        # fast.next.next not None make sure we have at least 3 element to move
        # A -> B -> None return A
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            middle = middle.next

        # A -------- middle -> ........end
        prev = None
        curr = middle.next
        while curr:
            curr_next = curr.next
            curr.next = prev
            prev = curr
            curr = curr_next

        # A -------- middle  |  after_middle <- ........prev
        half_head = prev
        while half_head:
            if half_head.val != head.val:
                return False
            head = head.next
            half_head = half_head.next
        return True
