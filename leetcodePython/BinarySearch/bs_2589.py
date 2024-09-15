from typing import List


class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: (x[1], x[0]))
        times = [False] * 2001
        for start, end, duration in tasks:
            for i in range(start, end + 1):
                if times[i]:
                    duration -= 1
            while duration > 0:
                if not times[end]:
                    times[end] = True
                    duration -= 1
                end -= 1
        return sum(times)
