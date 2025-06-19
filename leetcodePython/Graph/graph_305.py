from typing import List
from union_find import UF

class Solution:
    _Neighbours = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    def _joinNeighbours(self, id: int, pos: tuple[int, int], uf: UF, rows:int, cols:int) ->None:
        for move in self._Neighbours:
            neighbour = (pos[0]+move[0], pos[1]+move[1])
            neighbourId = neighbour[0] * cols + neighbour[1]
            if not self._valid(neighbour, rows, cols):
                continue
            if not uf.valid(neighbourId):
                continue
            uf.union(id, neighbourId)

    def _valid(self, pos: tuple[int, int], rows: int, cols:int) -> bool:
        r, c = pos
        if r < 0 or r >= rows:
            return False
        if c < 0 or c >= cols:
            return False
        return True

    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        uf = UF(m*n)
        islandsChange = []
        for r, c in positions:
            id = r * n + c
            uf.add(id)
            self._joinNeighbours(id, (r, c), uf, m, n)
            islandsChange.append(len(uf))
        return islandsChange
