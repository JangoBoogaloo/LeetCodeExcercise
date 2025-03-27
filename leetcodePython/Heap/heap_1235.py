from typing import List
from heapq import heappush, heappop

class Solution:
    @staticmethod
    def _getMaxPreviousProfit(start: int, end_maxProfit: List[tuple[int, int]]) -> int:
        maxProfit = 0
        while end_maxProfit:
            prev_end, prev_profit = end_maxProfit[0]
            if start < prev_end:
                break
            maxProfit = max(maxProfit, prev_profit)
            heappop(end_maxProfit)
        return maxProfit

    @staticmethod
    def _findMaxProfit(start_end_profit: List[tuple[int, int,int]]) -> int:
        end_maxProfit: List[tuple[int, int]] = []
        maxProfit = 0

        for i in range(len(start_end_profit)):
            start, end, profit = start_end_profit[i]
            prevMaxProfit = Solution._getMaxPreviousProfit(start, end_maxProfit)
            maxProfit = max(maxProfit, prevMaxProfit)
            end_profit_i = (end, maxProfit+profit)
            heappush(end_maxProfit, end_profit_i)
        maxProfit = 0
        for _, profit in end_maxProfit:
            maxProfit = max(maxProfit, profit)
        return maxProfit

    def jobScheduling(self, startTimes: List[int], endTime: List[int], profit: List[int]) -> int:
        sorted_start_end_profit = [(startTimes[i], endTime[i], profit[i]) for i in range(len(startTimes))]
        sorted_start_end_profit.sort()

        return self._findMaxProfit(sorted_start_end_profit)