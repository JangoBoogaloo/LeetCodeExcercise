from typing import List, Mapping
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


class Solution:
    def add_word(self, trie: Mapping, word: str) -> None:
        curr_node = trie
        for c in word:
            if c not in curr_node:
                curr_node[c] = {}
            curr_node = curr_node[c]
        curr_node['#'] = {}

    def get_words(self, trie: Mapping, prefix: str) -> List[str]:
        if self.k == 0:
            return []
        res = []
        if '#' in trie:
            self.k -= 1
            res.append(prefix)
        for i in range(26):
            c = chr(ord('a') + i)
            if c in trie:
                res += self.get_words(trie[c], prefix + c)
        return res

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        n = len(words)
        cnt = Counter(words)
        bucket = [{} for _ in range(n+1)]
        self.k = k

        for word, freq in cnt.items():
            self.add_word(bucket[freq], word)

        res = []
        for i in range(n, 0, -1):
            if self.k == 0:
                return res
            if bucket[i]:
                res += self.get_words(bucket[i], '')
        return res