from typing import List


class UnionFindInt:
    def __init__(self, grid: List[List[str]]):
        self._count = 0
        self._parent = []
        self._rank = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
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