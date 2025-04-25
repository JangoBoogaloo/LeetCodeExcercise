import bisect
from typing import List


class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.word_index_map = {}
        # build a word to its index list map: space O(n)
        for i in range(len(wordsDict)):
            if wordsDict[i] not in self.word_index_map:
                self.word_index_map[wordsDict[i]] = []
            # the list is already in ascending order as we iterate from left to right
            self.word_index_map[wordsDict[i]].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        list1 = self.word_index_map[word1]
        list2 = self.word_index_map[word2]
        i1, i2 = 0, 0
        min_diff = float('inf')
        while i1 < len(list1) and i2 < len(list2):
            min_diff = min(min_diff, abs(list1[i1] - list2[i2]))
            if list1[i1] < list2[i2]:
                i1 += 1
            else:
                i2 += 1
        return min_diff


class WordDistanceBinarySearch:

    def __init__(self, wordsDict: List[str]):
        self.word_index_map = {}
        # build a word to its index list map: space O(n)
        for i in range(len(wordsDict)):
            if wordsDict[i] not in self.word_index_map:
                self.word_index_map[wordsDict[i]] = []
            # the list is already in ascending order as we iterate from left to right
            self.word_index_map[wordsDict[i]].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        min_dist = float('inf')
        indexes_a = self.word_index_map[word1]
        indexes_b = self.word_index_map[word2]
        a_idx = b_idx = 0
        while min_dist and (a_idx < len(indexes_a)) and (b_idx < len(indexes_b)):
            a = indexes_a[a_idx]
            b = indexes_b[b_idx]
            min_dist = min(min_dist, abs(a - b))
            if a < b:
                a_idx = bisect.bisect_left(indexes_a, b_idx, a_idx + 1)
            else:
                b_idx = bisect.bisect_left(indexes_b, a_idx, b_idx + 1)
        return min_dist
