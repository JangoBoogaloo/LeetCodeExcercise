from typing import List
from heapq import heappush, heappop


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        maxFuelPQ = []
        currentStationIndex = 0
        furthest = startFuel
        fuelCount = 0
        while furthest < target:
            while currentStationIndex < len(stations) and stations[currentStationIndex][0] <= furthest:
                heappush(maxFuelPQ, -stations[currentStationIndex][1])
                currentStationIndex += 1
            if not maxFuelPQ:
                return -1
            furthest += -heappop(maxFuelPQ)
            fuelCount += 1
        return fuelCount
