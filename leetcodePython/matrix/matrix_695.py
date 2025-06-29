from typing import List


class Solution:
    _DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def _isValid(self, row, col, grid) -> bool:
        if row < 0 or row > len(grid) - 1:
            return False
        if col < 0 or col > len(grid[0]) - 1:
            return False
        return True

    def _dfsGetArea(self, row, col, grid) -> int:
        if grid[row][col] == 0:
            return 0
        grid[row][col] = 0
        area = 1
        for dirR, dirC in self._DIRECTIONS:
            newRow = row + dirR
            newCol = col + dirC
            if self._isValid(newRow, newCol, grid):
                area += self._dfsGetArea(newRow, newCol, grid)
        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                maxArea = max(maxArea, self._dfsGetArea(row, col, grid))
        return maxArea








