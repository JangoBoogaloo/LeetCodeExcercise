from typing import List


class Solution:
    def _shortestDistanceSameWords(self, wordsDict: List[str], word: str) -> int:
        prevPos, currPos = -1, -1
        minDist = float("inf")
        for i in range(len(wordsDict)):
            if wordsDict[i] != word:
                continue
            if prevPos == -1:
                prevPos = i
            else:
                currPos = i
                minDist = min(minDist, currPos - prevPos)
                prevPos = currPos
        return minDist

    def _shortestDistanceTwoWords(self, wordsDict: List[str], word1: str, word2: str) -> int:
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

    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        if word1 == word2:
            return self._shortestDistanceSameWords(wordsDict, word1)
        else:
            return self._shortestDistanceTwoWords(wordsDict, word1, word2)








