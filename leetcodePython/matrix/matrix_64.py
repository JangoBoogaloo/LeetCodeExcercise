from typing import List


class SolutionRecursion:
    def _calculate_sum(self, grid: List[List[int]], row: int, col: int) -> float:
        if row == len(grid) or col == len(grid[0]):
            return float("inf")
        if row == len(grid) - 1 and col == len(grid[0]) - 1:
            return grid[row][col]
        return grid[row][col] + min(self._calculate_sum(grid, row + 1, col), self._calculate_sum(grid, row, col + 1))

    def minPathSum(self, grid: List[List[int]]) -> int:
        return int(self._calculate_sum(grid, 0, 0))
