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
