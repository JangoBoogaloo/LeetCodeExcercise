from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        minCapacity, maxCapacity = max(weights), sum(weights)
        answerCapacity = -1
        while minCapacity <=maxCapacity:
            guess = (minCapacity + maxCapacity) // 2
            if self._canShipWithinDays(weights, days, guess):
                answerCapacity = guess
                maxCapacity = guess - 1
            else:
                minCapacity = guess + 1
        return answerCapacity

    def _canShipWithinDays(self, weights: List[int], days: int, weightCapacity: int) -> bool:
        currentWeight = 0
        currentDays = 1
        for weight in weights:
            if currentWeight + weight <= weightCapacity:
                currentWeight += weight
            else:
                currentWeight = weight
                currentDays += 1
                if currentDays > days:
                    return False
        return True
