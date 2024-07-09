from typing import List
from heapq import *


class SolutionMinHeap:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        minHeap = []
        for row in range(min(k, n)):
            heappush(minHeap, (matrix[row][0], row, 0))
        data = 0
        for i in range(k):
            data, r, c = heappop(minHeap)
            if c >= n - 1:
                continue
            heappush(minHeap, (matrix[r][c + 1], r, c + 1))
        return data
