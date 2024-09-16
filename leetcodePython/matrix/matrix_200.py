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


class SolutionBFS:
    @staticmethod
    def _addLand(grid: List[List[str]], neigh_bor: List[tuple[int, int]], row: int, col: int) -> None:
        if row < 0 or col < 0:
            return
        if row > len(grid) - 1 or col > len(grid[0]) - 1:
            return
        if grid[row][col] == "1":
            grid[row][col] = "0"
            neigh_bor.append((row, col))

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "0":
                    continue
                grid[row][col] = "O"
                islands += 1
                neigh_bors = [(row, col)]
                while neigh_bors:
                    r, c = neigh_bors.pop()
                    self._addLand(grid, neigh_bors, r - 1, c)
                    self._addLand(grid, neigh_bors, r + 1, c)
                    self._addLand(grid, neigh_bors, r, c - 1)
                    self._addLand(grid, neigh_bors, r, c + 1)
        return islands
