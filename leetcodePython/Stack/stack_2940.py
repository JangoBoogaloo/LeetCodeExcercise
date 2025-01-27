from typing import List


class Solution:
    @staticmethod
    def _search(fromHeight: int, increaseStack: List[tuple[int, int]]) -> int:
        left, right = 0, len(increaseStack) - 1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            height, query_i = increaseStack[mid]
            if height > fromHeight:
                ans = max(ans, mid)
                left = mid + 1
            else:
                right = mid - 1
        return ans

    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        result = [-1 for _ in range(len(queries))]
        newQueries: List[List[tuple[int, int]]]
        newQueries = [[] for _ in range(len(heights))]

        for i in range(len(queries)):
            a, b = queries[i]
            if a > b:
                a, b = b, a
            if heights[b] > heights[a] or a == b:
                result[i] = b
            else:
                newQueries[b].append((heights[a], i))

        decreaseStack = []
        for rightIndex in range(len(heights)-1, -1, -1):
            for leftHeight, queryIndex in newQueries[rightIndex]:
                pos = self._search(leftHeight, decreaseStack)
                if len(decreaseStack) > pos >= 0:
                    result[queryIndex] = decreaseStack[pos][1]
            while decreaseStack and decreaseStack[-1][0] <= heights[rightIndex]:
                decreaseStack.pop()
            decreaseStack.append((heights[rightIndex], rightIndex))
        return result
