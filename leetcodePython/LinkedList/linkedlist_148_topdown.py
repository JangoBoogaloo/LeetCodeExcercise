from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        middle = self._breakAndGetMiddle(head)
        half = self.sortList(head)
        half2 = self.sortList(middle)
        return self._merge(half, half2)

    @staticmethod
    def _breakAndGetMiddle(head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        beforeMiddle = slow
        while fast and fast.next:
            beforeMiddle = slow
            slow = slow.next
            fast = fast.next.next
        beforeMiddle.next = None
        return slow

    @staticmethod
    def _merge(node1: ListNode, node2: ListNode) -> ListNode:
        dummy = ListNode()
        current = dummy
        while node1 and node2:
            if node1.val < node2.val:
                current.next = node1
                node1 = node1.next
            else:
                current.next = node2
                node2 = node2.next
            current = current.next
        if node1:
            current.next = node1
        else:
            current.next = node2
        return dummy.next
