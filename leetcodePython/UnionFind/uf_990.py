from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf_equal = UF(26)
        for i in range(len(equations)):
            a, equal, _, b = equations[i]
            a = ord(a) - ord("a")
            b = ord(b) - ord("a")
            if equal == "!" and a == b:
                return False
            if equal == "=":
                uf_equal.union(a, b)

        for i in range(len(equations)):
            a, equal, _, b = equations[i]
            a = ord(a) - ord("a")
            b = ord(b) - ord("a")
            if equal == "!" and uf_equal.find(a) == uf_equal.find(b):
                return False
        return True


class UF:
    def __init__(self, size: int) -> None:
        self.ranks = [0] * size
        self.parents = list(range(size))

    def find(self, a: int) -> int:
        if self.parents[a] != a:
            self.parents[a] = self.find(self.parents[a])
        return self.parents[a]

    def union(self, a: int, b: int) -> None:
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return
        if self.ranks[root_a] > self.ranks[root_b]:
            self.parents[root_b] = root_a
        elif self.ranks[root_b] > self.ranks[root_a]:
            self.parents[root_a] = root_b
        else:
            self.parents[root_b] = root_a
            self.ranks[root_a] += 1