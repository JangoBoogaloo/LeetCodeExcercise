from typing import List


class Solution:
    @staticmethod
    def _achieveSweetnessWithinPiece(sweetness: List[int], minPieces: int, sweetExpect: int) -> bool:
        currSweet = 0
        piece = 0
        for sweet in sweetness:
            currSweet += sweet
            if currSweet >= sweetExpect:
                piece += 1
                currSweet = 0
            if piece >= minPieces:
                return True
        return False

    def maximizeSweetness(self, sweetness: List[int], friends: int) -> int:
        minSweet, maxSweet = min(sweetness), sum(sweetness) // (friends + 1)
        answerSweet = 0
        while minSweet <= maxSweet:
            guessSweet = (minSweet + maxSweet) // 2
            if self._achieveSweetnessWithinPiece(sweetness, friends+1, guessSweet):
                answerSweet = guessSweet
                minSweet = guessSweet + 1
            else:
                maxSweet = guessSweet - 1
        return answerSweet
