from collections import deque
from typing import List


class Solution:
    _DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    @staticmethod
    def _isWater(row:int, col:int, grid: List[List[int]]):
        if row < 0  or row >= len(grid):
            return False
        if col < 0 or col >= len(grid[0]):
            return False
        return grid[row][col] == 0

    def maxDistance(self, grid: List[List[int]]) -> int:
        levelLands = deque()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    levelLands.append((row, col))
        if len(levelLands) == len(grid) * len(grid[0]):
            return -1
        levels = -1
        while levelLands:
            levelSize = len(levelLands)
            for i in range(levelSize):
                row, col = levelLands.popleft()
                for dirR, dirC in self._DIRECTIONS:
                    newR, newC = row+dirR, col+dirC
                    if self._isWater(newR, newC, grid):
                        grid[newR][newC] = 1
                        levelLands.append((newR, newC))
            levels += 1
        return levels







import pytest
target = Solution()

@pytest.mark.parametrize("grid, expect",
[
    ([
        [1, 0, 1],
        [0, 0, 0],
        [1, 0, 1]
    ], 2),

    ([
        [1, 1],
        [1, 1]
    ], -1),

    ([
         [0, 0],
         [0, 0]
     ], -1),
])
def test_checkType(grid, expect):
    assert target.maxDistance(grid) == expect