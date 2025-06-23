from typing import List
from union_find import UF

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        uf = UF()
        for p in range(n):
            uf.add(p)
        for p1, p2 in connections:
            if uf.find(p1) != uf.find(p2):
                uf.union(p1, p2)
        return len(uf) - 1