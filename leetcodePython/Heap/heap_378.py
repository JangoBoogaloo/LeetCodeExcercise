from typing import List
from heapq import heappush, heappop


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        minHeap = []
        for row in range(min(k, len(matrix))):
            heappush(minHeap, (matrix[row][0], row, 0))

        ith = 0
        for i in range(k):
            ith, r, c = heappop(minHeap)
            if c >= len(matrix[0]) - 1:
                continue
            biggerInCurrentRow = (matrix[r][c+1], r, c+1)
            heappush(minHeap, biggerInCurrentRow)
        return ith
