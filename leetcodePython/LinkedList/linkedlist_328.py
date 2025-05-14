from typing import Optional


class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        prevEven = evenHead = ListNode()
        prevOdd = oddHead = ListNode()
        while head:
            odd = head
            even = head.next
            odd.next = None
            prevOdd.next = odd
            prevEven.next = even
            prevOdd = prevOdd.next
            prevEven = prevEven.next
            if even:
                head = even.next
            else:
                break
        prevOdd.next = evenHead.next
        return oddHead.next
