from typing import List
from collections import Counter


class SolutionBruteforce:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_counts = Counter(words)
        # O(nlog(n)) time
        # O(n) space
        return sorted(list(word_counts.keys()), key=lambda x: (-word_counts[x], x))[:k]


from heapq import heappush, heappop


class Word:
    def __init__(self, word: str, freq: int):
        self.word = word
        self.freq = freq

    def __lt__(self, other):
        return self.freq < other.freq or (self.freq == other.freq and self.word > other.word)


class SolutionMinHeap:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_counts = Counter(words)
        min_heap = []
        for word, freq in word_counts.items():
            heappush(min_heap, Word(word, freq))
            if len(min_heap) > k:
                heappop(min_heap)
        return [pair.word for pair in sorted(min_heap, reverse=True)]
