from math import isqrt
from typing import List
from collections import Counter


class Solution:
    @staticmethod
    def canFixCarsInTime(rankFreq: Counter, time: int, carToFix: int) -> bool:
        fixedCars = 0
        for rank in rankFreq:
            fixedCars += isqrt(time // rank) * rankFreq[rank]
            if fixedCars >= carToFix:
                return True
        return False

    def repairCars(self, ranks: List[int], cars: int) -> int:
        rankFreq = Counter(ranks)
        minRank = min(rankFreq.keys())
        minTime = minRank
        maxTime = minRank * cars * cars
        answer = 0
        while minTime <= maxTime:
            guessTime = (minTime + maxTime) // 2
            if self.canFixCarsInTime(rankFreq, guessTime, cars):
                answer = guessTime
                maxTime = guessTime - 1
            else:
                minTime = guessTime + 1
        return answer