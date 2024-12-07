from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummyHead = ListNode(-101)
        dummyHead.next = head
        lastUnique = dummyHead
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                lastUnique.next = head.next
            else:
                lastUnique = lastUnique.next
            head = head.next
        return dummyHead.next
