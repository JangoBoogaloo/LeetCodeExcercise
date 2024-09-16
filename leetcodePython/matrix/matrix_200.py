from typing import List


class SolutionDFS:
    def _dfs_sink_island(self, grid: List[List[str]], row: int, col: int) -> None:
        if row < 0 or col < 0:
            return
        if row >= len(grid) or col >= len(grid[0]):
            return

        if grid[row][col] != "1":
            return
        # sink this land, so it won't be calculated again for another island
        grid[row][col] = "0"
        self._dfs_sink_island(grid, row - 1, col)
        self._dfs_sink_island(grid, row + 1, col)
        self._dfs_sink_island(grid, row, col - 1)
        self._dfs_sink_island(grid, row, col + 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    self._dfs_sink_island(grid, row, col)
                    islands += 1
        return islands
