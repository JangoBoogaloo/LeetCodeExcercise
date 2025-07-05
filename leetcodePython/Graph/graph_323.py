from union_find import UF
from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UF()
        for p in range(n):
            uf.add(p)
        for p1, p2 in edges:
            uf.union(p1, p2)
        return len(uf)







