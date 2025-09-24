from typing import List
from union_find import UF

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        uf = UF()
        RANGE_LIMIT = 10001
        for row, col in stones:
            colId = col + RANGE_LIMIT
            uf.add(row), uf.add(colId)
            uf.union(row, colId)
        return len(stones) - len(uf)





