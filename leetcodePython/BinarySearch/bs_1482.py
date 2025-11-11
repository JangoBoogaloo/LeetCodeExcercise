from typing import List


class Solution:
    def _canGetBouquets(self, bloomDay: List[int], bouquets: int, adjacentFlowers: int, days: int) -> bool:
        actualBouquets = 0
        adjacentCount = 0
        for bloom in bloomDay:
            if bloom > days:
                adjacentCount = 0
            else:
                adjacentCount += 1
            if adjacentCount == adjacentFlowers:
                actualBouquets += 1
                adjacentCount = 0
            if actualBouquets >= bouquets:
                return True
        return False

    def minDays(self, bloomDay: List[int], bouquets: int, adjacentFlowers: int) -> int:
        need_flowers = bouquets * adjacentFlowers
        if need_flowers > len(bloomDay):
            return -1

        minDays, maxDays = min(bloomDay), max(bloomDay)
        answerDays = -1
        while minDays <= maxDays:
            guessDays = (minDays + maxDays) // 2
            if self._canGetBouquets(bloomDay, bouquets, adjacentFlowers, guessDays):
                answerDays = guessDays
                maxDays = guessDays - 1
            else:
                minDays = guessDays + 1
        return answerDays
