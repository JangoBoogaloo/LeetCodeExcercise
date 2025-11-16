from bisect import bisect_right
from typing import List


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        starts = []
        ends = []

        for start, end in flowers:
            starts.append(start)
            ends.append(end + 1)
        starts.sort()
        ends.sort()
        ans = []
        for arrive_time in people:
            idx_valid_start = bisect_right(starts, arrive_time)
            idx_valid_end = bisect_right(ends, arrive_time)
            ans.append(idx_valid_start - idx_valid_end)
        return ans