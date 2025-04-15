from typing import List
from heapq import heappush, heappop

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        weightMaxHeap = []
        for stone in stones:
            heappush(weightMaxHeap, -stone)

        while len(weightMaxHeap) >= 2:
            largeStone = -heappop(weightMaxHeap)
            smallStone = -heappop(weightMaxHeap)
            newStone = largeStone - smallStone
            if newStone:
                heappush(weightMaxHeap, -newStone)
        if weightMaxHeap:
            return -weightMaxHeap[0]
        return 0
