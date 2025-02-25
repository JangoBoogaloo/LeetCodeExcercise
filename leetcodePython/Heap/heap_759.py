import operator
from heapq import *
from typing import List


class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        schedule_time = []
        for employee in schedule:
            for interval in employee:
                schedule_time.append((interval.start, interval.end))
        schedule_time.sort()
        end_time_heap = []
        heappush(end_time_heap, schedule_time[0][1])
        answer = []
        for start, end in schedule_time[1:]:
            prev_end_time = end_time_heap[0]
            while end_time_heap and end_time_heap[0] < start:
                prev_end_time = end_time_heap[0]
                heappop(end_time_heap)
            if not end_time_heap:
                answer.append(Interval(prev_end_time, start))
            heappush(end_time_heap, end)
        return answer