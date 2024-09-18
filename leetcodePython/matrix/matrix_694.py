from typing import List


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        seen = set()
        unique_island = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                path = []
                self._dfs(grid, seen, path, row, col, "S")
                if path:
                    unique_island.add(tuple(path))
        return len(unique_island)

    def _dfs(self, grid: List[List[int]], seen: set, path: List[str], row: int, col: int, direction: str) -> None:
        if row < 0 or col < 0:
            return
        if row >= len(grid) or col >= len(grid[0]):
            return
        if (row, col) in seen or grid[row][col] == 0:
            return
        seen.add((row, col))
        path.append(direction)
        self._dfs(grid, seen, path, row + 1, col, "D")
        self._dfs(grid, seen, path, row - 1, col, "U")
        self._dfs(grid, seen, path, row, col + 1, "R")
        self._dfs(grid, seen, path, row, col - 1, "L")
        path.append("^")
