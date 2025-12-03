from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        maxWinWithin = [[0] * len(piles) for _ in range(len(piles))]
        for i in range(len(piles)):
            maxWinWithin[i][i] = piles[i]

        for right in range(1, len(piles)):
            for left in range(right-1, -1, -1):
                maxWinWithin[left][right] = max(piles[left] - maxWinWithin[left+1][right], piles[right] - maxWinWithin[left][right-1])
        return maxWinWithin[0][len(piles)-1] > 0









