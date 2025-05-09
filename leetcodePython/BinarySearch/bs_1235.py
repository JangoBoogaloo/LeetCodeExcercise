from typing import List
from bisect import bisect_left, bisect

class Solution:
    def jobScheduling(self, startTimes: List[int], endTimes: List[int], profits: List[int]) -> int:
        end_start_profit = sorted(zip(endTimes, startTimes, profits))
        endTime_maxProfit:List[tuple[int, int]] = [(0, 0)]
        for end, start, profit in end_start_profit:
            previousJob = bisect_left(endTime_maxProfit, start+1, key=lambda job: job[0])-1
            _, prevMaxProfit = endTime_maxProfit[previousJob]
            currentMaxProfit = prevMaxProfit + profit
            if currentMaxProfit > endTime_maxProfit[-1][1]:
                endTime_maxProfit.append((end, currentMaxProfit))
        return endTime_maxProfit[-1][1]
