from typing import List


class SolutionDFS:
    _Directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    _LAND = "1"
    _WATER = "0"

    def _isValid(self, grid: List[List[str]], pos: tuple[int, int]) -> bool:
        row, col = pos
        if row < 0 or row > len(grid) -1:
            return False
        if col < 0 or col > len(grid[0]) - 1:
            return False
        if grid[row][col] == self._WATER:
            return False
        return True

    def _dfs(self, grid: List[List[str]], pos: tuple[int, int]):
        row, col = pos
        grid[row][col] = self._WATER
        for moveRow, moveCol in self._Directions:
            newPos = (row+moveRow, col+moveCol)
            if not self._isValid(grid, newPos):
                continue
            self._dfs(grid, newPos)

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == self._WATER:
                    continue
                islands += 1
                self._dfs(grid, (row,col))
        return islands


class UnionFind:
    _WATER = "0"
    _LAND = "1"

    def __init__(self, grid: List[List[str]]):
        self._count = 0
        self._parent = []
        self._rank = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == self._LAND:
                    cell_index = row * len(grid[0]) + col
                    self._parent.append(cell_index)
                    self._count += 1
                else:
                    self._parent.append(-1)
                self._rank.append(0)

    def find(self, data: int) -> int:
        if self._parent[data] != data:
            self._parent[data] = self.find(self._parent[data])
        return self._parent[data]

    def union(self, a: int, b: int) -> None:
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            if self._rank[root_a] > self._rank[root_b]:
                self._parent[root_b] = root_a
            elif self._rank[root_a] < self._rank[root_b]:
                self._parent[root_a] = root_b
            else:
                self._parent[root_b] = root_a
                self._rank[root_a] += 1
            self._count -= 1

    def count(self) -> int:
        return self._count


class Solution:
    _WATER = "0"
    _DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def _isLand(self, grid: List[List[str]], pos: tuple[int, int]) -> bool:
        row, col = pos
        if row < 0 or col < 0:
            return False
        if row > len(grid) - 1 or col > len(grid[0]) - 1:
            return False
        if grid[row][col] == self._WATER:
            return False
        return True

    @staticmethod
    def _combineLands(grid: List[List[str]], uf: UnionFind, pos: tuple[int, int], pos_new: tuple[int, int]) -> None:
        r_new, c_new = pos_new
        r, c = pos
        pos_index = r * len(grid[0]) + c
        pos_new_index = r_new * len(grid[0]) + c_new
        uf.union(pos_index, pos_new_index)

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        uf = UnionFind(grid)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == self._WATER:
                    continue
                for row_move, col_move in self._DIRECTIONS:
                    pose_new = (row + row_move, col + col_move)
                    if not self._isLand(grid, pose_new):
                        continue
                    self._combineLands(grid, uf, (row, col), pose_new)
        return uf.count()
