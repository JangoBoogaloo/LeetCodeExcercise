from heapq import heappop, heappush
from typing import List


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        end_value_heap = []
        prevMaxValue = 0
        maxValue = 0
        for start, end, value in events:
            while end_value_heap and start >= end_value_heap[0][0]:
                prevStart, prevEnd, prevValue = heappop(end_value_heap)
                prevMaxValue = max(prevMaxValue, prevValue)
            maxValue = max(maxValue, prevMaxValue + value)
            heappush(end_value_heap, (end, value))
        return maxValue