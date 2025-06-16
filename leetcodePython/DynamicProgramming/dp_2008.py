from typing import List


class Solution:
    def maxTaxiEarnings(self, locations: int, rides: List[List[int]]) -> int:
        maxProfitAt = [0] * (locations+1)
        rides.sort(key=lambda r: r[1])
        rideIndex = 0
        for location in range(1, len(maxProfitAt)):
            maxProfitAt[location] = maxProfitAt[location-1]
            while rideIndex < len(rides) and location == rides[rideIndex][1]:
                start, end, tip = rides[rideIndex]
                profit = tip + end - start
                maxProfitAt[location] = max(maxProfitAt[location], maxProfitAt[start] + profit)
                rideIndex += 1
        return maxProfitAt[-1]