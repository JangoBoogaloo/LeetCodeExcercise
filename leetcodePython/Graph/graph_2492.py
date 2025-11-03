from typing import List
from union_find import UF

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        uf = UF()
        for src, dst, dist in roads:
            uf.add(src), uf.add(dst)
            uf.union(src, dst)

        expectComponent = uf.find(n)
        minDist = float("inf")
        for src, dst, dist in roads:
            if uf.find(src) == expectComponent:
                minDist = min(minDist, dist)
        return minDist






