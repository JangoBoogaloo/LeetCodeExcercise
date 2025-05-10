from typing import List
from math import ceil

class Solution:
    def _canFinishWithinHours(self, piles: List[int], hourLimit: int, speed: int) -> bool:
        spendHours = 0
        for pile in piles:
            spendHours += ceil(pile/speed)
            if spendHours > hourLimit:
                return False
        return True

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minSpeed, maxSpeed = 1, max(piles)
        answerSpeed = -1
        while minSpeed <= maxSpeed:
            guessSpeed = (minSpeed + maxSpeed) // 2
            if self._canFinishWithinHours(piles, h, guessSpeed):
                answerSpeed = guessSpeed
                maxSpeed = guessSpeed - 1
            else:
                minSpeed = guessSpeed + 1
        return answerSpeed
