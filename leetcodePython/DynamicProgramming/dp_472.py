from typing import List


class Solution:
    def _canConcat(self, word: str, wordSet: frozenset[str], concatState: dict) -> bool:
        if word in concatState:
            return concatState[word]
        for prefixIndex in range(self._minWordLength, len(word) - self._minWordLength+1):
            prefix, suffix = word[:prefixIndex], word[prefixIndex:]
            if prefix not in wordSet:
                continue
            if suffix in wordSet:
                concatState[word] = True
                return True
            if self._canConcat(suffix, wordSet, concatState):
                concatState[word] = True
                return True
        concatState[word] = False
        return False

    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordSet = frozenset(words)
        self._minWordLength = min(map(len, words))
        concatState = {}
        concatWords = []
        for word in words:
            if self._canConcat(word, wordSet, concatState):
                concatWords.append(word)
        return concatWords








