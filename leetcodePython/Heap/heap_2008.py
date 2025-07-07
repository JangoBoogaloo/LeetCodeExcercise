from typing import List
from heapq import heappop, heappush

class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort()
        end_profit_heap = []
        prevMaxProfit = 0
        for start, end, tip in rides:
            if end > n:
                continue
            singleProfit = tip + end - start
            while end_profit_heap and start >= end_profit_heap[0][0]:
                prevMaxProfit = max(prevMaxProfit, end_profit_heap[0][1])
                heappop(end_profit_heap)
            currentMaxProfit = prevMaxProfit + singleProfit
            heappush(end_profit_heap, (end, currentMaxProfit))

        maxProfit = 0
        while end_profit_heap:
            _, profit = heappop(end_profit_heap)
            maxProfit = max(maxProfit, profit)
        return maxProfit
