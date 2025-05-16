from heapq import heappop, heappush
from typing import List


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        end = max([e for s, e in events])
        events.sort()
        start = events[0][0]
        visitEventIndex = 0
        endtimePQ = []
        answer = 0
        for today in range(start, end+1):
            while endtimePQ and endtimePQ[0] < today:
                heappop(endtimePQ)
            while visitEventIndex < len(events) and events[visitEventIndex][0] == today:
                heappush(endtimePQ, events[visitEventIndex][1])
                visitEventIndex += 1
            if endtimePQ:
                heappop(endtimePQ)
                answer += 1
        return answer
