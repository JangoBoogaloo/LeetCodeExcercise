from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1
        uf = UF(n)
        components = n
        for i in range(len(connections)):
            src, dst = connections[i]
            if not uf.connected(src, dst):
                uf.union(src, dst)
                components -= 1
        return components - 1


class UF:
    def __init__(self, size: int) -> None:
        self.ranks = [0] * size
        self.parents = list(range(size))

    def find(self, a: int) -> int:
        if self.parents[a] != a:
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
        if self.ranks[root_a] > self.ranks[root_b]:
            self.parents[root_b] = root_a
        elif self.ranks[root_b] > self.ranks[root_a]:
            self.parents[root_a] = root_b
        else:
            self.parents[root_b] = root_a
            self.ranks[root_a] += 1


if __name__ == "__main__":
    sol = Solution()
    ans = sol.makeConnected(5, [[0,1],[0,2],[3,4],[2,3]])
    print(ans)
