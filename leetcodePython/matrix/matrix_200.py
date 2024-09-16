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


class SolutionDFSNoModify:
    def _dfs_sink_island(self, grid: List[List[str]], visited: List[List[bool]], row: int, col: int) -> None:
        if row < 0 or col < 0:
            return
        if row >= len(grid) or col >= len(grid[0]):
            return

        if visited[row][col] or grid[row][col] != "1":
            visited[row][col] = True
            return
        visited[row][col] = True
        self._dfs_sink_island(grid, visited, row - 1, col)
        self._dfs_sink_island(grid, visited, row + 1, col)
        self._dfs_sink_island(grid, visited, row, col - 1)
        self._dfs_sink_island(grid, visited, row, col + 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False] * len(grid[i]) for i in range(len(grid))]

        if not grid:
            return 0

        islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if visited[row][col]:
                    continue
                if grid[row][col] == "1":
                    self._dfs_sink_island(grid, visited, row, col)
                    islands += 1
                visited[row][col] = True
        return islands


from UnionFind.DataStructure import UnionFindInt


class SolutionUnionFind:
    @staticmethod
    def _join_new_land(grid: List[List[str]], uf: UnionFindInt, land: tuple[int, int],
                       new_land: tuple[int, int]) -> None:
        r_new, c_new = new_land
        if r_new < 0 or c_new < 0:
            return
        if r_new > len(grid) - 1 or c_new > len(grid[0]) - 1:
            return
        if grid[r_new][c_new] == "0":
            return
        r, c = land
        land_id = r * len(grid[0]) + c
        new_land_id = r_new * len(grid[0]) + c_new
        uf.union(land_id, new_land_id)

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        uf = UnionFindInt(grid)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "0":
                    continue
                self._join_new_land(grid, uf, (row, col), (row - 1, col))
                self._join_new_land(grid, uf, (row, col), (row + 1, col))
                self._join_new_land(grid, uf, (row, col), (row, col - 1))
                self._join_new_land(grid, uf, (row, col), (row, col + 1))
        return uf.count()


if __name__ == "__main__":
    sol = SolutionUnionFind()
    ans = sol.numIslands(
        [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]])
    print(ans)
