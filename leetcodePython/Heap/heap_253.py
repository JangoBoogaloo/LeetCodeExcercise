import heapq
from typing import List


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
        start_i = end_i = 0

        while start_i < len(start_times):
            if start_times[start_i] < end_times[end_i]:
                used_rooms += 1
            else:
                end_i += 1
            start_i += 1
        return used_rooms


class SolutionPQ:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        end_time_pq = []
        # push the end time for 1st meeting to note a room
        heapq.heappush(end_time_pq, intervals[0][1])

        for interval in intervals[1:]:
            start_time = interval[0]
            end_time = interval[1]
            if end_time_pq[0] <= start_time:
                heapq.heappop(end_time_pq)
            heapq.heappush(end_time_pq, end_time)
        return len(end_time_pq)


if __name__ == '__main__':
    solution = SolutionTwoPointers()
    solution.minMeetingRooms([[0, 30], [5, 10], [15, 20]])
