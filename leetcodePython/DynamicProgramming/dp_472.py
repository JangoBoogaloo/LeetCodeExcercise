from functools import cache
from typing import List


class Solution:
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
