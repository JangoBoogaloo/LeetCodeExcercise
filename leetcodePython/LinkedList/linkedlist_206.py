from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev -> curr -> next
        # next -> curr -> prev

        # none -> head -> next
        # none <- head <- next

        prev = None
        curr = head
        while curr:
            curr_next = curr.next
            # none <- head  or prev <- curr
            curr.next = prev
            prev = curr
            curr = curr_next
        return prev
