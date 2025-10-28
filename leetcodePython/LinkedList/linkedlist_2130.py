from typing import Optional
from linkedlist import ListNode

class Solution:
    @staticmethod
    def _getMiddle(head: Optional[ListNode]) -> ListNode:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    @staticmethod
    def _reverse(head: Optional[ListNode]) -> ListNode:
        prev, curr, = None, head
        while curr:
            curr.next, curr, prev = prev, curr.next, curr
        return prev

    def pairSum(self, head: Optional[ListNode]) -> int:
        middle = self._getMiddle(head)
        reverseMiddle = self._reverse(middle)
        maxSum = float('-inf')
        while reverseMiddle:
            maxSum = max(maxSum, head.val+reverseMiddle.val)
            head = head.next
            reverseMiddle = reverseMiddle.next
        return maxSum




