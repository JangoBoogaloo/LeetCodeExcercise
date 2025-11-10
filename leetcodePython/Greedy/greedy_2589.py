from typing import List


class Solution:
    _TIMERANGE = 2001
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        # sort by end time and start time
        tasks.sort(key=lambda x:(x[1], x[0]))
        alreadyEnabledAt = [False] * self._TIMERANGE
        for start, end, duration in tasks:
            for time in range(start, end + 1):
                if alreadyEnabledAt[time]:
                    duration -= 1
            while duration > 0:
                # more likely to overlap if we take the end
                if not alreadyEnabledAt[end]:
                    alreadyEnabledAt[end] = True
                    duration -= 1
                end -= 1
        return sum(alreadyEnabledAt)








