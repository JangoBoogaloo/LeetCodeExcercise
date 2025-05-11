from typing import List
from heapq import *


class Solution:
    def findMaximizedCapital(self, projectLimit: int, initialCapital: int, capitalProfits: List[int], requireCapitals: List[int]) -> int:
        minCostProjects = list(zip(requireCapitals, capitalProfits))
        minCostProjects.sort()
        maxProfitHeap = []

        currentCapital = initialCapital
        index = 0
        for i in range(projectLimit):
            while index < len(minCostProjects) and minCostProjects[index][0] <= currentCapital:
                heappush(maxProfitHeap, -minCostProjects[index][1])
                index += 1

            if not maxProfitHeap:
                break
            currentCapital += -heappop(maxProfitHeap)
        return currentCapital