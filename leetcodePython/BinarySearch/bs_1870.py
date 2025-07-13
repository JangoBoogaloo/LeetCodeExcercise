from typing import List
from math import ceil

class Solution:
    def _canArriveWithin(self, hour:float, dist: List[int], speed:int) -> bool:
        totalHours = 0
        for d in dist[:-1]:
            totalHours += ceil(d / speed)
            if totalHours > hour:
                return False
        return totalHours + dist[-1] / speed <= hour

    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        minSpeed, maxSpeed = 1, ceil(sum(dist) / hour)
        answerSpeed = -1
        while minSpeed <= maxSpeed:
            guess = (minSpeed + maxSpeed) // 2
            if self._canArriveWithin(hour, dist, guess):
                answerSpeed = guess
                maxSpeed = guess - 1
            else:
                minSpeed = guess + 1
        return answerSpeed
