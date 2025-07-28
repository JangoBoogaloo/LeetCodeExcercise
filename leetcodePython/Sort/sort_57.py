from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        newSmall, newBig = newInterval
        while i < len(intervals):
            if intervals[i][1] >= newSmall:
                newSmall = min(intervals[i][0], newSmall)
                break
            result.append(intervals[i])
            i += 1

        while i < len(intervals):
            if intervals[i][0] > newBig:
                break
            newBig = max(intervals[i][1], newBig)
            i += 1
        result.append([newSmall, newBig])
        result += intervals[i:]
        return result





