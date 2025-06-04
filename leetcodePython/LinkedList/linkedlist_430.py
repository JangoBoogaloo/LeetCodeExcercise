from typing import Optional


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def _flattenRecursive(self, head: Node) -> tuple[Node, Node]:
        curr = head
        tail = None
        while curr:
            if not curr.child:
                tail = curr
                curr = curr.next
                continue
            childHead, childTail = self._flattenRecursive(curr.child)
            end = curr.next
            curr.next, childHead.prev = childHead, curr
            childTail.next = end
            tail = childTail
            if end:
                end.prev = tail
                tail = end
            curr.child = None
            curr = curr.next
        print(tail.val)
        return head, tail

    def flatten(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return head
        self._flattenRecursive(head)
        return head