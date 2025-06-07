from typing import Optional
from linkedlist import Node


class Solution:
    def insert(self, head: Optional[Node], insertVal: int) -> Node:
        if not head:
            head = Node(insertVal)
            head.next = head
            return head
        current = head
        while current.next != head:
            if current.val <= current.next.val:
                # curr < insert < next
                if current.val <= insertVal <= current.next.val:
                    break
            else:
                if current.val <= insertVal:
                    break
                if current.next.val >= insertVal:
                    break
            current = current.next
        newNode = Node(insertVal)
        current.next, newNode.next = newNode, current.next
        return head







