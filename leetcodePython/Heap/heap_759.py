import operator
from heapq import *
from typing import List


class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class SolutionHeap:
    def employeeFreeTime(self, schedule: List[List[Interval]]) -> List[Interval]:
        start_time_heap = []
        for employee_i, employee in enumerate(schedule):
            heappush(start_time_heap, (employee[0].start, employee_i, 0))
        ans = []

        _, employee_i, event_j = start_time_heap[0]
        prev_end = schedule[employee_i][event_j].end
        while start_time_heap:
            _, employee_i, event_j = heappop(start_time_heap)
            if event_j + 1 < len(schedule[employee_i]):
                heappush(start_time_heap, (schedule[employee_i][event_j+1].start, employee_i, event_j+1))

            event = schedule[employee_i][event_j]
            if event.start > prev_end:
                ans.append(Interval(prev_end, event.start))
            prev_end = max(prev_end, event.end)
        return ans


class SolutionSort:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # flatten schedule
        events = []
        for employee in schedule:
            for event in employee:
                events.append(event)

        # sort events by start
        events.sort(key=operator.attrgetter('start'))

        # collect result
        res = []
        iterator = iter(events)
        prev_end = next(iterator).end
        for event in iterator:
            if event.start > prev_end:
                res.append(Interval(prev_end, event.start))
            prev_end = max(prev_end, event.end)
        return res