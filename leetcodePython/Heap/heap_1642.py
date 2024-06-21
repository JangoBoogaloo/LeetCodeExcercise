from typing import List
from heapq import *


class SolutionMinHeap:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        used_ladder_min_heap = []
        for i in range(len(heights) - 1):
            climb = heights[i + 1] - heights[i]
            if climb <= 0:
                continue
            # we always push and assume a ladder first before we check
            heappush(used_ladder_min_heap, climb)
            # the ladder we want to use is already more than we have, replace the smallest with bricks
            # the smallest can also just be the latest
            if len(used_ladder_min_heap) > ladders:
                bricks -= heappop(used_ladder_min_heap)
                if bricks < 0:
                    return i

        return len(heights) - 1


class SolutionMaxHeap:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        used_brick_max_heap = []
        for i in range(len(heights) - 1):
            climb = heights[i + 1] - heights[i]
            if climb <= 0:
                continue
            heappush(used_brick_max_heap, -climb)
            bricks -= climb

            if bricks < 0:
                bricks += -heappop(used_brick_max_heap)
                ladders -= 1
                if ladders < 0:
                    return i
        return len(heights) - 1