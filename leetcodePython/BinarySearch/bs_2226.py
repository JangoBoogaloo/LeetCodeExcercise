from typing import List


class Solution:
    def _canDistribute(self, candies:List[int], children: int, candiesEach: int) -> bool:
        if not candiesEach:
            return True
        childrenHappy = 0
        for candy in candies:
            childrenHappy += candy // candiesEach
            if childrenHappy >= children:
                return True
        return False

    def maximumCandies(self, candies: List[int], children: int) -> int:
        minCandies, maxCandies = 0, sum(candies) // children
        answerCandies = 0
        while minCandies <= maxCandies:
            guessCandies = (minCandies + maxCandies) // 2
            if self._canDistribute(candies, children, guessCandies):
                answerCandies = guessCandies
                minCandies = guessCandies + 1
            else:
                maxCandies = guessCandies - 1
        return answerCandies