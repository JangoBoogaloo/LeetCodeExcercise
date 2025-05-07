from typing import List
from collections import deque


class SolutionMonotonicStack:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        decreaseValue_indexStack = []
        ans = []
        for right in reversed(range(n)):
            while decreaseValue_indexStack and heights[decreaseValue_indexStack[-1]] < heights[right]:
                decreaseValue_indexStack.pop()
            if not decreaseValue_indexStack:
                ans.append(right)
            decreaseValue_indexStack.append(right)
        ans.reverse()
        return ans


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        prev_height = 0
        ans = deque()
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > prev_height:
                prev_height = heights[i]
                ans.appendleft(i)
        return list(ans)
