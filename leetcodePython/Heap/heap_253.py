import collections
import heapq
from typing import List
from heapq import *


class SolutionSweepLine:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        meeting_change = collections.defaultdict(int)
        for start, end in intervals:
            meeting_change[start] += 1
            meeting_change[end] -= 1

        curr_meetings = 0
        ans = 0
        for t, change in sorted(meeting_change.items()):
            curr_meetings += change
            ans = max(curr_meetings, ans)
        return ans


class SolutionPQ:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        end_time_heap = []
        heappush(end_time_heap, intervals[0][1])
        for start_time, end_time in intervals[1:]:
            if end_time_heap[0] <= start_time:
                heappop(end_time_heap)
            heappush(end_time_heap, end_time)
        return len(end_time_heap)


class SolutionTwoPointers:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start_times = []
        end_times = []
        for interval in intervals:
            start_times.append(interval[0])
            end_times.append(interval[1])

        start_times.sort()
        end_times.sort()

        used_rooms = 0
        end_i = 0

        for start_time in start_times:
            if start_time < end_times[end_i]:
                used_rooms += 1
            else:
                end_i += 1
        return used_rooms
