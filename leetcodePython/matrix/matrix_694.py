from typing import List


class Solution:
    _DIRECTIONS = {
        "U":(-1, 0),
        "D":(1, 0),
        "L":(0, -1),
        "R":(0, 1)
    }

    @staticmethod
    def _isValid(row, col, grid) -> bool:
        if row < 0 or row > len(grid) - 1:
            return False
        if col < 0 or col > len(grid[0]) - 1:
            return False
        if grid[row][col] == 0:
            return False
        return True

    def _checkIsland(self, row, col, directionKey, grid, islandPattern):
        if not self._isValid(row, col, grid):
            return
        islandPattern.append(directionKey)
        grid[row][col] = 0
        for direction in self._DIRECTIONS:
            newRow = row + self._DIRECTIONS[direction][0]
            newCol = col + self._DIRECTIONS[direction][1]
            self._checkIsland(newRow, newCol, direction, grid, islandPattern)
        islandPattern.append("T")

    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        islandPatterns = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                islandPattern = []
                self._checkIsland(row, col, "S", grid, islandPattern)
                if islandPattern:
                    patternHash = "".join(islandPattern)
                    islandPatterns.add(patternHash)
        return len(islandPatterns)







