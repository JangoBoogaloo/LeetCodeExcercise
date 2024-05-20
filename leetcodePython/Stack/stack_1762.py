from typing import List
from collections import deque


class SolutionFromRight:
    def findBuildings(self, heights: List[int]) -> List[int]:
        prev_height = 0
        ans = deque()
        for i in range(len(heights)-1, -1, -1):
            if heights[i] > prev_height:
                prev_height = heights[i]
                ans.appendleft(i)
        return list(ans)