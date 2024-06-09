from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SolutionMonotonicStack:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(1000000)
        dummy.next = head
        stack = [dummy]
        curr = head
        while curr:
            while stack[-1] != dummy and stack[-1].val < curr.val:
                stack.pop()
            stack[-1].next = curr
            stack.append(curr)
            curr = curr.next
        return dummy.next


class SolutionRecursion:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        head.next = self.removeNodes(head.next)
        if head.next and head.val < head.next.val:
            return head.next
        return head
