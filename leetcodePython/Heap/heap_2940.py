from heapq import heappush, heappop
from typing import List


class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        answer = [-1] * len(queries)
        targetHeightAtPosition = self._getQueryTargetHeightAtPositions(heights, queries, answer)
        minHeight_query = []
        for pos, high in enumerate(heights):
            while minHeight_query:
                minHigh, q_i = minHeight_query[0]
                if minHigh >= high:
                    break
                heappop(minHeight_query)
                answer[q_i] = pos

            for targetHeight, q_i in targetHeightAtPosition[pos]:
                heappush(minHeight_query, (targetHeight, q_i))
        return answer

    @staticmethod
    def _getQueryTargetHeightAtPositions(heights: List[int], queries: List[List[int]], answer: List[int]) -> List[List[tuple[int, int]]]:
        maxPosAndHeightQuery = [[] for _ in heights]
        for query_i, query in enumerate(queries):
            posA, posB = query
            if posA < posB and heights[posA] < heights[posB]:
                answer[query_i] = posB
            elif posA > posB and heights[posA] > heights[posB]:
                answer[query_i] = posA
            elif posA == posB:
                answer[query_i] = posA
            else:
                maxPos = max(posA, posB)
                maxHeight = max(heights[posA], heights[posB])
                maxPosAndHeightQuery[maxPos].append((maxHeight, query_i))
        return maxPosAndHeightQuery
