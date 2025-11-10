from typing import List, Optional


class Solution:
    def _maxWinWithin(self, left, right, piles: List[int], maxWinWithin: List[List[Optional[int]]]) -> int:
        if left > right:
            return 0
        if maxWinWithin[left][right] is not None:
            return maxWinWithin[left][right]

        maxWinWithin[left][right] = max(piles[left] - self._maxWinWithin(left+1, right, piles, maxWinWithin),
                                        piles[right] - self._maxWinWithin(left, right-1, piles, maxWinWithin))
        return maxWinWithin[left][right]

    def stoneGame(self, piles: List[int]) -> bool:
        maxWinWithin = [[None] * len(piles) for _ in range(len(piles))]
        return self._maxWinWithin(0, len(piles)-1, piles, maxWinWithin) > 0








