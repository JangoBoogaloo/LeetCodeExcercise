from typing import List


class Solution:
    def _canAchievePenaltyWithinOps(self, ballBags: List[int], operations: int, penalty: int) -> bool:
        ops = 0
        for balls in ballBags:
            ops += (balls - 1) // penalty
            if ops > operations:
                return False
        return True

    def minimumSize(self, ballBags: List[int], maxOperations: int) -> int:
        ballBags.sort(reverse=True)
        minPenalty, maxPenalty = 1, max(ballBags)
        answerPenalty = 1
        while minPenalty <= maxPenalty:
            guess = (maxPenalty + minPenalty) // 2
            if self._canAchievePenaltyWithinOps(ballBags, maxOperations, guess):
                answerPenalty = guess
                maxPenalty = guess - 1
            else:
                minPenalty = guess + 1
        return answerPenalty
