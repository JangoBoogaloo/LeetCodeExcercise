from heapq import heappop, heappush
from typing import List


class Solution:
    _DIRECTIONS = [(-1,0), (1, 0), (0, -1), (0, 1)]

    def _isPosValid(self, row: int, col: int, visited: set[tuple[int, int]], grid: List[List[int]]) -> bool:
        if row < 0 or row >= len(grid):
            return False
        if col < 0 or col >= len(grid[0]):
            return False
        if (row, col) in visited:
            return False
        return True

    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        minTimeConsideredPos = [(grid[0][0], 0, 0)]
        consideredPos: set[tuple[int, int]] = {(0,0)}
        ans = 0
        while True:
            time, row, col = heappop(minTimeConsideredPos)
            ans = max(ans, time)
            if row == len(grid)-1 and col == len(grid[0])-1:
                break
            for dirR, dirC in Solution._DIRECTIONS:
                r, c = row+dirR, col+dirC
                if not self._isPosValid(r, c, consideredPos, grid):
                    continue
                consideredPos.add((r,c))
                heappush(minTimeConsideredPos, (grid[r][c], r,c))
        return ans
