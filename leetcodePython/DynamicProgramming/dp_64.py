from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        minSumAt = [[0] * cols for _ in range(rows)]
        minSumAt[0][0] = grid[0][0]
        for row in range(1, rows):
            minSumAt[row][0] = minSumAt[row - 1][0] + grid[row][0]

        for col in range(1, cols):
            minSumAt[0][col] = minSumAt[0][col - 1] + grid[0][col]

        for row in range(1, rows):
            for col in range(1, cols):
                minSumAt[row][col] = grid[row][col] + min(minSumAt[row - 1][col], minSumAt[row][col - 1])

        return minSumAt[-1][-1]
