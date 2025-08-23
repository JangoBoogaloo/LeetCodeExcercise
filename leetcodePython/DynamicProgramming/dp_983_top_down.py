from typing import List


class Solution:
    def _minCostAt(self, day: int, days: set[int], costForDays: dict[int, int]) -> int:
        minCost = float("inf")
        if day not in days:
            return self._minCostAt(day-1, days, costForDays)
        for ticketEffectDays in costForDays:
            ticketStartDay = max(0, day - ticketEffectDays)
            minCost = min(minCost, self._minCostAt(ticketStartDay, days, costForDays))
        return minCost

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        costForDays = {1: costs[0], 7: costs[1], 30: costs[2]}
        days = set(days)
        return self._minCostAt(days[-1], days, costForDays)
