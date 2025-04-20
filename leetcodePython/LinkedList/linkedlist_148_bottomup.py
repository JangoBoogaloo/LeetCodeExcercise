from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head

        def getSize(head):
            # Simply count the length of linked list
            counter = 0
            while head:
                counter += 1
                head = head.next
            return counter

        def split(head, size):
            # given the head & size, return the the start node of next chunk
            for i in range(size - 1):
                if not head:
                    break
                head = head.next

            if not head: return None
            next_start, head.next = head.next, None  # disconnect

            return next_start

        def merge(l1, l2, dummy_start):
            # Given dummy_start, merge two lists, and return the tail of merged list
            curr = dummy_start
            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next, l1 = l1, l1.next
                else:
                    curr.next, l2 = l2, l2.next
                curr = curr.next

            curr.next = l1 if l1 else l2
            while curr.next: curr = curr.next  # Find tail
            # the returned tail should be the "dummy_start" node of next chunk
