from collections import defaultdict
from typing import List

class WordDistance:
    def __init__(self, wordsDict: List[str]) -> None:
        self._indexesOf = defaultdict(list)
        for index, word in enumerate(wordsDict):
            self._indexesOf[word].append(index)
    def shortest(self, word1: str, word2: str) -> int:
        word1Indexes = self._indexesOf[word1]
        word2Indexes = self._indexesOf[word2]
        return self._closestDistance(word1Indexes, word2Indexes)

    def _closestDistance(self, array1, array2) -> int:
        index1, index2 = 0, 0
        minDistance = float('inf')
        while minDistance and index1 < len(array1) and index2 < len(array2):
            value1 = array1[index1]
            value2 = array2[index2]
            minDistance = min(minDistance, abs(value1 - value2))
            if value1 < value2:
                index1 += 1
            else:
                index2 += 1
        return minDistance







