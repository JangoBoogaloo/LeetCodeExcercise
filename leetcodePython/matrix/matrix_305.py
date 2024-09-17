from typing import List


class UnionFind:
    def __init__(self, size: int) -> None:
        self._rank = [0 for _ in range(size)]
        self._parent = [-1 for _ in range(size)]
        self._count = 0

    def add(self, a: int) -> None:
        if self._parent[a] < 0:
            self._parent[a] = a
            self._count += 1

    def is_valid(self, a: int) -> bool:
        return self._parent[a] >= 0

    def count(self) -> int:
        return self._count

    def find(self, a: int) -> int:
        if self._parent[a] != a:
            self._parent[a] = self.find(self._parent[a])
        return self._parent[a]

    def union(self, a: int, b: int) -> None:
        root_a, root_b = self.find(a), self.find(b)
        if root_a == root_b:
            return
        if self._rank[root_a] > self._rank[root_b]:
            self._parent[root_b] = root_a
        elif self._rank[root_a] < self._rank[root_b]:
            self._parent[root_a] = root_b
        else:
            self._parent[root_b] = root_a
            self._rank[root_a] += 1
        self._count -= 1


class Solution:

    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        uf = UnionFind(m * n)
        ans = []
        for r, c in positions:
            land_id = r * n + c
            uf.add(land_id)
            self._join_neighbor(uf, land_id, m, n, r - 1, c)
            self._join_neighbor(uf, land_id, m, n, r + 1, c)
            self._join_neighbor(uf, land_id, m, n, r, c - 1)
            self._join_neighbor(uf, land_id, m, n, r, c + 1)
            ans.append(uf.count())
        return ans

    @staticmethod
    def _join_neighbor(uf: UnionFind, land_id: int, m: int, n: int, r: int, c: int) -> None:
        if r < 0 or c < 0:
            return
        if r >= m or c >= n:
            return
        neighbor_id = r * n + c
        if not uf.is_valid(neighbor_id):
            return
        uf.union(land_id, neighbor_id)
