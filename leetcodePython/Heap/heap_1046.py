from typing import List
from heapq import heappush, heappop

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heappush(heap, -stone)
        while len(heap) >= 2:
            stone_x = -heappop(heap)
            stone_y = -heappop(heap)
            stone_left = stone_x - stone_y
            if stone_left > 0:
                heappush(heap, -stone_left)
        if len(heap) >0:
            return -heappop(heap)
        else:
            return 0