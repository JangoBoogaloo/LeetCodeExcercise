from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return head

        # insert new node between next
        current = head
        while current:
            new_current = Node(current.val, current.next)
            current.next = new_current
            current = new_current.next

        # construct random
        current = head
        while current:
            if current.random:
                new_current = current.next
                new_random = current.random.next
                new_current.random = new_random
            current = current.next.next

        old_current = head
        new_head = new_current = head.next
        while old_current:
            old_current.next = old_current.next.next
            if new_current:
                new_current.next = new_current.next.next

            old_current = old_current.next
            new_current = new_current.next
        return new_head