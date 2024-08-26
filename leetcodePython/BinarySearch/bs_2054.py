import heapq
from typing import List


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        chained_event_heap = []
        max_chained_value = 0
        max_value = 0
        for start, end, value in events:
            while chained_event_heap:
                chained_end, chained_value = chained_event_heap[0]
                if chained_end >= start:
                    break
                heapq.heappop(chained_event_heap)
                max_chained_value = max(max_chained_value, chained_value)
            max_value = max(max_value, max_chained_value + value)
            heapq.heappush(chained_event_heap, (end, value))
        return max_value
