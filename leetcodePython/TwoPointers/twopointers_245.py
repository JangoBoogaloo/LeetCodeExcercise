from typing import List


class Solution:
    def _shortestDistanceDiffWords(self, wordsDict: List[str], word1: str, word2: str) -> int:
        i1, i2 = -1, -1
        min_dist = float('inf')
        for i, word in enumerate(wordsDict):
            if word == word1:
                i1 = i
            elif word == word2:
                i2 = i
            if i1 != -1 and i2 != -1:
                min_dist = min(abs(i1 - i2), min_dist)
        return min_dist

    def _shortestDistanceSameWords(self, wordsDict: List[str], word1: str) -> int:
        prev_i = -1
        min_dist = float('inf')
        for i, word in enumerate(wordsDict):
            if word != word1:
                continue
            if prev_i == -1:
                prev_i = i
                continue
            min_dist = min(i - prev_i, min_dist)
            prev_i = i

        return min_dist

    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        if word1 != word2:
            return self._shortestDistanceDiffWords(wordsDict, word1, word2)
        else:
            return self._shortestDistanceSameWords(wordsDict, word1)
