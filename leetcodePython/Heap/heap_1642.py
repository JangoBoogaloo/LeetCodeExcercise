from typing import List
from heapq import *


class Solution:
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


if __name__ == "__main__":
    sol = Solution()
    sol.furthestBuilding([2, 7, 9, 3, 1, 2, 5, 9, 4, 6], 8, 2)
