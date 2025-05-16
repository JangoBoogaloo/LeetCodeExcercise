from typing import List
from collections import deque


class SolutionFromRight:
    def findBuildings(self, heights: List[int]) -> List[int]:
        prev_height = 0
        ans = deque()
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > prev_height:
                prev_height = heights[i]
                ans.appendleft(i)
        return list(ans)


class SolutionMonotonicStack:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        stack = []
        ans = []
        for right in reversed(range(n)):
            while stack and heights[stack[-1]] < heights[right]:
                stack.pop()
            if not stack:
                ans.append(right)
            stack.append(right)
        ans.reverse()
        return ans
