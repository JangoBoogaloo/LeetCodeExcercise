import collections
from typing import List
from heapq import *


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        grid_size = len(grid)
        distance = [[float('inf')] * grid_size for _ in range(grid_size)]
        pos_queue = collections.deque()
        self._record_thief_pos(grid, pos_queue, distance)
        self._set_thief_distance(pos_queue, distance, directions)
        safeness_max_heap = [(-distance[0][0], 0, 0)]
        max_safeness: List[List[float]]
        max_safeness = [[-1] * grid_size for _ in range(grid_size)]
        max_safeness[0][0] = distance[0][0]

        while safeness_max_heap:
            neg_safe, r, c = heappop(safeness_max_heap)
            safeness = - neg_safe
            if r == grid_size - 1 and c == grid_size - 1:
                return int(safeness)
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if self._out_of_bound(grid_size, nr, nc):
                    continue
                distance_new = distance[nr][nc]
                new_safe = min(safeness, distance_new)
                if new_safe > max_safeness[nr][nc]:
                    max_safeness[nr][nc] = new_safe
                    heappush(safeness_max_heap, (-new_safe, nr, nc))
        return -1

    def _set_thief_distance(self, pos_queue: collections.deque, distance: List[List[float]],
                            directions: List[tuple[int, int]]) -> None:
        grid_size = len(distance)
        while pos_queue:
            r, c = pos = pos_queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if self._out_of_bound(grid_size, nr, nc):
                    continue
                if distance[nr][nc] != float('inf'):
                    continue
                distance[nr][nc] = distance[r][c] + 1
                pos_queue.append((nr, nc))

    @staticmethod
    def _record_thief_pos(grid: List[List[int]], pos_queue: collections.deque, distance: List[List[float]]) -> None:
        THIEF = 1
        grid_size = len(grid)
        # start from thief, visit all position
        for row in range(grid_size):
            for col in range(grid_size):
                # start from thief, just record all thieves
                if grid[row][col] == THIEF:
                    pos_queue.append((row, col))
                    distance[row][col] = 0

    @staticmethod
    def _out_of_bound(grid_size: int, row: int, col: int) -> bool:
        if row < 0 or col < 0:
            return True
        if row >= grid_size or col >= grid_size:
            return True
        return False
