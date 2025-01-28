from heapq import heappush, heappop
from typing import List


class Solution:
    @staticmethod
    def _maxPosAndHeightQuery(heights: List[int], queries: List[List[int]], results: List[int]) -> List[List[tuple[int, int]]]:
        maxPosAndHeightQuery = [[] for _ in heights]
        for query_i, query in enumerate(queries):
            posA, posB = query
            if posA < posB and heights[posA] < heights[posB]:
                results[query_i] = posB
            elif posA > posB and heights[posA] > heights[posB]:
                results[query_i] = posA
            elif posA == posB:
                results[query_i] = posA
            else:
                maxPos = max(posA, posB)
                maxHeight = max(heights[posA], heights[posB])
                maxPosAndHeightQuery[maxPos].append((maxHeight, query_i))
        return maxPosAndHeightQuery

    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        results = [-1] * len(queries)
        maxPosAndHeightQuery = self._maxPosAndHeightQuery(heights, queries, results)
        minHeightHeap = []
        for pos, height in enumerate(heights):
            while minHeightHeap:
                minHeight, query_i = minHeightHeap[0]
                if minHeight < height:
                    heappop(minHeightHeap)
                    results[query_i] = pos
                else:
                    break
            for h, query_i in maxPosAndHeightQuery[pos]:
                heappush(minHeightHeap, (h, query_i))
        return results
