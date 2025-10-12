from typing import List


class Solution:
    def _minCostFrom(self, day: int, lastDay:int, days: set[int], costForDays: dict[int, int], minCostAt: List[int]) -> int:
        if day > lastDay:
            return 0
        if day not in days:
            return self._minCostFrom(day+1, lastDay, days, costForDays, minCostAt)

        if minCostAt[day] != -1:
            return minCostAt[day]
        minCost = float('inf')
        for ticketDays in costForDays:
            minCost = min(minCost, costForDays[ticketDays] + self._minCostFrom(day + ticketDays, lastDay, days, costForDays, minCostAt))
        minCostAt[day] = minCost
        return minCostAt[day]

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        costForDays = {1: costs[0], 7: costs[1], 30: costs[2]}
        lastDay = days[-1]
        days = set(days)
        minCostAt = [-1] * (lastDay + 1)
        return self._minCostFrom(1, lastDay, days, costForDays, minCostAt)





