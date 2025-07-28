from typing import List


class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        word1Pos, word2Pos = -1, -1
        minDist = float("inf")
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                word1Pos = i
            if wordsDict[i] == word2:
                word2Pos = i
            if word1Pos != -1 and word2Pos != -1:
                minDist = min(minDist, abs(word1Pos - word2Pos))
        return minDist





