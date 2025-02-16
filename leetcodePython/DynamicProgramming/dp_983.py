from typing import List


class Solution:
    def _costForPassFrom(self, day: int, cost: int, costAt: List[int]) -> int:
        beforePassDay = max(0, day)
        return costAt[beforePassDay] + cost

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        lastDay = days[-1]
        costAt = [0] * (lastDay + 1)
        dayIndex = 0
        passCostFor = {1: costs[0], 7: costs[1], 30:costs[2]}

        for day in range(1, lastDay + 1):
            if day < days[dayIndex]:
                costAt[day] = costAt[day-1]
                continue
            dayIndex += 1
            costAt[day] = float("inf")
            for dayOption in passCostFor:
                passStartDay = day - dayOption
                costAt[day] = min(costAt[day], self._costForPassFrom(passStartDay, passCostFor[dayOption], costAt))
        return costAt[-1]