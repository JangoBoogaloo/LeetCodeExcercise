from heapq import heappush, heappop
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        furthestPoints = []
        for x, y in points:
            distance = x*x + y*y
            heappush(furthestPoints, (-distance, [x, y]))
            if len(furthestPoints) > k:
                heappop(furthestPoints)
        return [point for _, point in furthestPoints]
