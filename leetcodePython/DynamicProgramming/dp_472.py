import collections
from functools import cache
from typing import List


class SolutionCacheDP:
    """
    Calculate if a word is concat of words in seen.
    If it's calculated, simply return the cached result
    """

    @cache
    def _can_concat(self, word: str, seen: frozenset[str]) -> bool:
        # [prefix] + [------suffix------]
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]
            if prefix not in seen:
                continue
            if suffix in seen:
                return True
            # recursion [prefix_suffix] + [------suffix_suffix------] to check suffix
            if self._can_concat(suffix, seen):
                return True
        return False

    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        seen = frozenset(words)
        ans = []
        for word in words:
            if self._can_concat(word, seen):
                ans.append(word)
        return ans


class SolutionDP:
    def _can_concat(self, word: str, seen: frozenset[str], concat_state: dict) -> bool:
        if word in concat_state:
            return concat_state[word]

        # [prefix] + [------suffix------]
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]
            if prefix not in seen:
                continue
            if suffix in seen:
                concat_state[word] = True
                return True
            # recursion [prefix_suffix] + [------suffix_suffix------] to check suffix
            if self._can_concat(suffix, seen, concat_state):
                concat_state[word] = True
                return True
        concat_state[word] = False
        return False

    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        seen = frozenset(words)
        concat_state = {}
        ans = []
        for word in words:
            if self._can_concat(word, seen, concat_state):
                ans.append(word)
        return ans
