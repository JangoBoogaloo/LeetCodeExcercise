from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        minForce, maxForce = 1,  int((position[-1] - position[0]) / (m - 1.0)) + 1
        answer = 0
        while minForce <= maxForce:
            guessForce = (minForce + maxForce) // 2
            balls = self._distributeBalls(guessForce, m, position)
            if balls < m:
                maxForce = guessForce - 1
            else:
                answer = guessForce
                minForce = guessForce + 1
        return answer

    def _distributeBalls(self, force: int, balls: int, position: List[int]) -> int:
        prevPos = position[0]
        ballCount = 1
        for currPos in position[1:]:
            if currPos - prevPos >= force:
                ballCount += 1
                prevPos = currPos
                if ballCount > balls:
                    return ballCount
        return ballCount