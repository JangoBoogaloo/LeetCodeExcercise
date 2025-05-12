from typing import List
from collections import Counter
from heapq import heappop, heappush


class Word:
    def __init__(self, word: str, freq: int):
        self.word = word
        self.freq = freq

    def __lt__(self, other):
        return self.freq < other.freq or (self.freq == other.freq and self.word > other.word)


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordFrequency = Counter(words)
        minFreqKWordHeap = []
        for word, freq in wordFrequency.items():
            heappush(minFreqKWordHeap, Word(word, freq))
            if len(minFreqKWordHeap) > k:
                heappop(minFreqKWordHeap)
        return [word.word for word in sorted(minFreqKWordHeap, reverse=True)]
