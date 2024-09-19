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


class SolutionInPlaceDP:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        for row in range(1, rows):
            grid[row][0] += grid[row - 1][0]

        for col in range(1, cols):
            grid[0][col] += grid[0][col - 1]

        for row in range(1, rows):
            for col in range(1, cols):
                grid[row][col] += min(grid[row - 1][col], grid[row][col - 1])
        return grid[-1][-1]
