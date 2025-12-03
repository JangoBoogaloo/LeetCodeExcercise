from typing import List
from collections import deque
from heapq import heappop, heappush

class Solution:
    _THIEF = 1
    _NOT_VISITED = -1
    _directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def _findThief(self, grid: List[List[int]], bfsLayer: deque[(int, int)], thiefDistance):
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == self._THIEF:
                    bfsLayer.append((row, col))
                    thiefDistance[row][col] = 0

    def _bfsSetThiefDistance(self, grid: List[List[int]], bfsLayer: deque[(int, int)], thiefDistance: List[List[int]]):
        while bfsLayer:
            row, col = bfsLayer.popleft()
            for dr, dc in self._directions:
                newR, newC = row + dr, col + dc
                if not self._inbound(newR, newC, grid) or thiefDistance[newR][newC] != self._NOT_VISITED:
                    continue
                thiefDistance[newR][newC] = thiefDistance[row][col] + 1
                bfsLayer.append((newR, newC))

    @staticmethod
    def _inbound(row, col, grid: List[List[int]]) -> bool:
        if row < 0 or row >= len(grid):
            return False
        if col < 0 or col >= len(grid[0]):
            return False
        return True

    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        bfsLayer = deque()
        thiefDistance = [[self._NOT_VISITED] * len(grid[0]) for _ in range(len(grid))]
        self._findThief(grid, bfsLayer, thiefDistance)
        self._bfsSetThiefDistance(grid, bfsLayer, thiefDistance)
        distanceMaxHeap = [(-thiefDistance[0][0], 0, 0)]
        maxSafeAt = [[-1] * len(grid[0]) for _ in range(len(grid))]
        maxSafeAt[0][0] = thiefDistance[0][0]

        while distanceMaxHeap:
            negDistance, row, col = heappop(distanceMaxHeap)
            distance = -negDistance
            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                return distance
            for dr, dc in self._directions:
                nRow, nCol = row + dr, col + dc
                if not self._inbound(nRow, nCol, grid):
                    continue
                newDistance = min(distance, thiefDistance[nRow][nCol])
                if maxSafeAt[nRow][nCol] < newDistance:
                    maxSafeAt[nRow][nCol] = newDistance
                    heappush(distanceMaxHeap, (-newDistance, nRow, nCol))
        return -1








