from typing import List
from bisect import bisect_left, bisect

class SolutionDP:
    def jobScheduling(self, startTimes: List[int], endTimes: List[int], profits: List[int]) -> int:
        start_end_profit = sorted(zip(startTimes, endTimes, profits), key=lambda job: job[1])
        endTime_maxProfit:List[tuple[int, int]] = [(0, 0)]
        for start, end, profit in start_end_profit:
            nextJobIndex = bisect_left(endTime_maxProfit, start+1, key=lambda job: job[0])-1
            _, nextMaxProfit = endTime_maxProfit[nextJobIndex]
            if nextMaxProfit + profit > endTime_maxProfit[-1][1]:
                endTime_maxProfit.append((end, nextMaxProfit+profit))
        return endTime_maxProfit[-1][1]
