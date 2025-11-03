from collections import deque
from typing import List


class Solution:
    _DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def _isPosValid(self, row:int, col:int, grid: List[List[int]]) -> bool:
        if row < 0 or row > len(grid) - 1:
            return False
        if col < 0 or col > len(grid[0]) - 1:
            return False
        if grid[row][col] == 1:
            return False
        return True

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        level = deque([(0, 0)])
        steps = 0
        while level:
            levelSize = len(level)
            steps += 1
            for _ in range(levelSize):
                currRow, currCol = level.popleft()
                if currRow == len(grid) - 1 and currCol == len(grid[0]) - 1:
                    return steps
                for dirR, dirC in self._DIRECTIONS:
                    nextR, nextC = currRow + dirR, currCol + dirC
                    if self._isPosValid(nextR, nextC, grid):
                        level.append((nextR, nextC))
                        grid[nextR][nextC] = 1
        return -1







