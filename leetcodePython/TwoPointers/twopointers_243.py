import bisect
from collections import defaultdict
from typing import List


class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        word_indexes = defaultdict(list)
        for i, word in enumerate(wordsDict):
            word_indexes[word].append(i)
        list1 = word_indexes[word1]
        list2 = word_indexes[word2]
        min_dist = float('inf')
        for num in list1:
            i2 = bisect.bisect(list2, num)
            if i2 > 0:
                min_dist = min(num - list2[i2 - 1], min_dist)
            if i2 < len(list2):
                min_dist = min(list2[i2] - num, min_dist)
        return min_dist


class SolutionOnePass:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
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
