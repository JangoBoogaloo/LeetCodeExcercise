from typing import List


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations.sort()
        minStopsToStation = [i for i in range(len(stations))]
        # reverse consider
        # lastStation[i] to target, minFuelInCar > target - lastPosition
        # or minFuelInCar + lastFuel >= target - lastPostion
        return -1