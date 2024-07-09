from typing import List
from heapq import *


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projects = list(zip(capital, profits))
        projects.sort()
        heap = []
        ptr = 0
        capital = w
        for i in range(k):
            while ptr < n and projects[ptr][0] <= capital:
                heappush(heap, -projects[ptr][1])
                ptr += 1
            if not heap:
                break
            capital += -heappop(heap)
        return capital
