import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        pq = [(grid[0][0], 0, 0)]
        visited = set()
        visited.add((0,0))
        ans = 0
        while True:
            time, row, col = heapq.heappop(pq)
            ans = max(ans, time)
            if row == col == n - 1:
                return ans
            for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
                if 0 <= c < n and 0 <= r < n and (r, c) not in visited:
                    visited.add((r,c))
                    heapq.heappush(pq, (grid[r][c], r,c))
