from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        maxWinStartAt = [0] * len(piles)
        for i in range(len(piles)):
            maxWinStartAt[i] = piles[i]

        for right in range(1, len(piles)):
            for left in range(right-1, -1, -1):
                maxWinStartAt[left] = max(piles[left] - maxWinStartAt[left+1], piles[right] - maxWinStartAt[left])
        return maxWinStartAt[0] > 0









