from typing import List, Optional
from heapq import *


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for node in lists:
            if node:
                heappush(heap, HeapNode(node))

        dummy = ListNode(-1)
        curr = dummy
        while heap:
            minimum = heappop(heap).node
            curr.next = minimum
            if minimum.next:
                heappush(heap, HeapNode(minimum.next))
            curr = curr.next
        return dummy.next


class HeapNode:
    def __init__(self, node: ListNode):
        self.node = node

    def __lt__(self, other) -> bool:
        # Define comparison based on ListNode's value
        return self.node.val < other.node.val