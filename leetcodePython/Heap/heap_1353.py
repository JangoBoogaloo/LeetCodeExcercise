from typing import List
from heapq import heappush, heappop


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda e: e[0])
        end_time_pq = []
        checked_event = 0
        attended_events = 0
        for day in range(1, 100001):
            # events already ended, remove it
            while end_time_pq and end_time_pq[0] < day:
                heappop(end_time_pq)

            # put events started today into consideration
            while checked_event < len(events) and events[checked_event][0] == day:
                heappush(end_time_pq, events[checked_event][1])
                checked_event += 1

            # on this day, we can only attend 1 event
            if end_time_pq:
                heappop(end_time_pq)
                attended_events += 1

            if checked_event >= len(events) and not end_time_pq:
                break

        return attended_events


class SolutionOptimizedReversed:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda e: -e[0])
        end_time_pq = []
        attended_events = 0
        day = 0
        while events or end_time_pq:
            if not end_time_pq:
                day = events[-1][0]
            while events and events[-1][0] <= day:
                earliest = events.pop()
                heappush(end_time_pq, earliest[1])
            heappop(end_time_pq)
            attended_events += 1
            day += 1
            while end_time_pq and end_time_pq[0] < day:
                heappop(end_time_pq)
        return attended_events


if __name__ == "__main__":
    sol = Solution()
    sol.maxEvents([[3, 4], [1, 2], [2, 3]])
