from typing import List
from union_find import UF

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        uf = UF()
        for row in range(len(isConnected)):
            uf.add(row)
            for col in range(row+1, len(isConnected[0])):
                uf.add(col)
                if not isConnected[row][col]:
                    continue
                uf.union(row, col)
        return len(uf)






