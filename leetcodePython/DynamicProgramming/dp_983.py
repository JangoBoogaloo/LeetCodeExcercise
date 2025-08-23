from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        lastDay = days[-1]
        costAt = [0] * (lastDay + 1)
        ticketForDays = {1: costs[0], 7: costs[1], 30: costs[2]}
        playDayIndex = 0
        for day in range(1, lastDay+1):
            if day < days[playDayIndex]:
                costAt[day] = costAt[day-1]
                continue
            playDayIndex += 1
            costAt[day] = float("inf")
            for ticketDays in ticketForDays:
                ticketStartDay = max(0, day - ticketDays)
                costAt[day] = min(costAt[day], costAt[ticketStartDay] + ticketForDays[ticketDays])
        return costAt[-1]







