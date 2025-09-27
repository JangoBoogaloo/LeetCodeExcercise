from typing import List
from union_find import UF

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UF()
        for p1, p2 in edges:
            uf.add(p1)
            uf.add(p2)
            if uf.find(p1) == uf.find(p2):
                return [p1, p2]
            uf.union(p1, p2)
        return []






