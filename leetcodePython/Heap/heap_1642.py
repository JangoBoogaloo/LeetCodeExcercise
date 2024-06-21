from typing import List
from heapq import *

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        used_ladder_min_heap = []
        for i in range(len(heights)-1):
            climb = heights[i+1] - heights[i]
            if climb <= 0:
                continue

            heappush(used_ladder_min_heap, climb)
            if len(used_ladder_min_heap) <= ladders:
                continue

            bricks -= heappop(used_ladder_min_heap)

            if bricks < 0:
                return i

        return len(heights) - 1