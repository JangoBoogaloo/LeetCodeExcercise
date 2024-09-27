from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        uf = UF(len(isConnected))

        for city_a in range(len(isConnected)):
            for city_b in range(len(isConnected[0])):
                if isConnected[city_a][city_b] == 1:
                    uf.union(city_a, city_b)
        return uf.count


class UF:
    def __init__(self, size: int):
        self.parents = list(range(size))
        self.ranks = [0] * size
        self.count = size

    def find(self, a: int) -> int:
        if self.parents[a] != a:
            self.parents[a] = self.find(self.parents[a])
        return self.parents[a]

    def union(self, a: int, b: int) -> None:
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return

        self.count -= 1
        if self.ranks[root_a] > self.ranks[root_b]:
            self.parents[root_b] = root_a
        elif self.ranks[root_a] < self.ranks[root_b]:
            self.parents[root_a] = root_b
        else:
            self.parents[root_b] = root_a
            self.ranks[root_a] += 1