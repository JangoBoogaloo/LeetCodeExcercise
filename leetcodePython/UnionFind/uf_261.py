from typing import List


class UF:
    def __init__(self, size: int) -> None:
        self.ranks = [0] * size
        self.parents = list(range(size))

    def find(self, data: int) -> int:
        if self.parents[data] != data:
            self.parents[data] = self.find(self.parents[data])
        return self.parents[data]

    def union(self, a: int, b: int) -> bool:
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return False
        if self.ranks[root_b] < self.ranks[root_a]:
            self.parents[root_b] = root_a
        elif self.ranks[root_a] < self.ranks[root_b]:
            self.parents[root_a] = root_b
        else:
            self.parents[root_b] = root_a
            self.ranks[root_a] += 1
        return True


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UF(n)
        components = n
        for a, b in edges:
            if not uf.union(a, b):
                return False
            components -= 1
        return components == 1


if __name__ == "__main__":
    sol = Solution()
    ans = sol.validTree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]])
    print(ans)