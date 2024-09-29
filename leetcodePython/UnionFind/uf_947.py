from typing import List


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        STONE_COUNT = len(stones)
        uf = UF(STONE_COUNT)
        for a in range(STONE_COUNT):
            for b in range(a+1, STONE_COUNT):
                row_a, col_a = stones[a]
                row_b, col_b = stones[b]
                if row_a == row_b or col_a == col_b:
                    uf.union(a, b)

        return STONE_COUNT - uf.count


class UF:
    def __init__(self, size: int) -> None:
        self.parents = [-1] * size
        self.count = size

    def find(self, a: int) -> int:
        if self.parents[a] == -1:
            return a
        self.parents[a] = self.find(self.parents[a])
        return self.parents[a]

    def connected(self, a: int, b: int) -> bool:
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return True
        return False

    def union(self, a: int, b: int) -> None:
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return
        self.parents[root_b] = root_a
        self.count -= 1


class SolutionOptimize:
    def removeStones(self, stones: List[List[int]]) -> int:
        GRID_SIZE = 20002
        uf = UFOptimize(GRID_SIZE)
        for row, col in stones:
            a = row
            b = col + 10001
            uf.union(a, b)
        return len(stones) - uf.count


class UFOptimize:
    def __init__(self, size: int) -> None:
        self.parents = [-1] * size
        self.count = 0
        self.nodes = set()

    def find(self, a: int) -> int:
        if a not in self.nodes:
            self.count += 1
            self.nodes.add(a)

        if self.parents[a] == -1:
            return a
        self.parents[a] = self.find(self.parents[a])
        return self.parents[a]

    def connected(self, a: int, b: int) -> bool:
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return True
        return False

    def union(self, a: int, b: int) -> None:
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return
        self.parents[root_b] = root_a
        self.count -= 1
