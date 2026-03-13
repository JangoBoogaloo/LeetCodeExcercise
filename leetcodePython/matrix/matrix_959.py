from typing import List


class Solution:
    _DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    @staticmethod
    def _expandGrid(originGrid: List[str]) -> List[List[int]]:
        gridSize = len(originGrid)
        expandedGrid = [[1] * gridSize * 3 for _ in range(gridSize*3)]
        for row in range(len(originGrid)):
            for col in range(len(originGrid)):
                expandedRow = row*3
                expandedCol = col*3
                if originGrid[row][col] == '\\':
                    expandedGrid[expandedRow][expandedCol] = 0
                    expandedGrid[expandedRow+1][expandedCol+1] = 0
                    expandedGrid[expandedRow+2][expandedCol+2] = 0
                elif originGrid[row][col] == '/':
                    expandedGrid[expandedRow][expandedCol+2] = 0
                    expandedGrid[expandedRow+1][expandedCol+1] = 0
                    expandedGrid[expandedRow+2][expandedCol] = 0
        return expandedGrid

    @staticmethod
    def _isLand(grid: List[List[int]], row, col) -> bool:
        if row < 0 or row > len(grid)-1:
            return False
        if col < 0 or col > len(grid[0])-1:
            return False
        return grid[row][col] == 1

    def _dfsSinkIsland(self, grid: List[List[int]], row, col):
        grid[row][col] = 0
        for dirR, dirC in self._DIRECTIONS:
            newR, newC = row + dirR, col + dirC
            if not self._isLand(grid, newR, newC):
                continue
            self._dfsSinkIsland(grid, newR, newC)

    def regionsBySlashes(self, grid: List[str]) -> int:
        expandedGrid = self._expandGrid(grid)
        regions = 0
        for row in range(len(expandedGrid)):
            for col in range(len(expandedGrid[0])):
                if self._isLand(expandedGrid, row, col):
                    regions += 1
                    self._dfsSinkIsland(expandedGrid, row, col)

        return regions
