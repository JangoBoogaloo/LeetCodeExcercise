from heapq import heappush, heappop
from typing import List


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        furthestWithRefuelCount = [startFuel] + [0] * len(stations)
        for i, (pos, fuel) in enumerate(stations):
            for t in range(i, -1, -1):
                if furthestWithRefuelCount[t] >= pos:
                    furthestWithRefuelCount[t+1] = max(furthestWithRefuelCount[t+1], furthestWithRefuelCount[t] + fuel)
        for refuelCount, position in enumerate(furthestWithRefuelCount):
            if position >= target:
                return refuelCount
        return -1


class SolutionPQ:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        maxFuelPQ = []
        currentFurthest = startFuel
        checkStationIndex = 0
        refuelCount = 0
        while currentFurthest < target:
            while checkStationIndex < len(stations) and stations[checkStationIndex][0] <= currentFurthest:
                heappush(maxFuelPQ, -stations[checkStationIndex][1])
                checkStationIndex += 1
            if not maxFuelPQ:
                return -1
            currentFurthest += -heappop(maxFuelPQ)
            refuelCount += 1
        return refuelCount