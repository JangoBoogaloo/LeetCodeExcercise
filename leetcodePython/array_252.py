from typing import List
from functools import cmp_to_key


class Solution:
    def compare(self, x: List[int], y: List[int]):
        return x[0] - y[0]

    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=cmp_to_key(self.compare))
        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True