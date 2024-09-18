from typing import List


class Solution:
    @staticmethod
    def _out_of_bound(rows: int, columns: int, row: int, col: int) -> bool:
        if row < 0 or col < 0:
            return True
        if row >= rows or col >= columns:
            return True
        return False

    def _dfs_get_area(self, grid: List[List[int]], row: int, col: int) -> int:
        if self._out_of_bound(len(grid), len(grid[0]), row, col):
            return 0
        if grid[row][col] == 0:
            return 0
        area = 1
        grid[row][col] = 0
        area += self._dfs_get_area(grid, row - 1, col)
        area += self._dfs_get_area(grid, row + 1, col)
        area += self._dfs_get_area(grid, row, col - 1)
        area += self._dfs_get_area(grid, row, col + 1)
        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                curr_area = self._dfs_get_area(grid, row, col)
                max_area = max(max_area, curr_area)
        return max_area
