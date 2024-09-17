from typing import List


class UnionFind:
    def __init__(self, size):
        self._rank = [0] * size
        self._parent = [i for i in range(size)]

    def find(self, a: int) -> int:
        if self._parent[a] != a:
            self._parent[a] = self.find(self._parent[a])
        return self._parent[a]

    def union(self, a: int, b: int) -> None:
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return
        if self._rank[root_a] > self._rank[root_b]:
            self._parent[root_b] = root_a
        elif self._rank[root_b] > self._rank[root_a]:
            self._parent[root_a] = root_b
        else:
            self._parent[root_b] = root_a
            self._rank[root_a] += 1


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for a, b in edges:
            uf.union(a, b)
        components = set()
        for i in range(n):
            components.add(uf.find(i))
        return len(components)
