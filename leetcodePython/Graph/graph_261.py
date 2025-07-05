from typing import List
from union_find import UF


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UF()
        [uf.add(i) for i in range(n)]
        for p1, p2 in edges:
            if uf.find(p1) == uf.find(p2):
                return False
            uf.union(p1, p2)
        return len(uf) == 1






