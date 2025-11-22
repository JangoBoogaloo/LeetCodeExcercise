from functools import lru_cache


class Solution:
    @lru_cache
    def isMatch(self, text: str, pattern: str) -> bool:
        if not pattern:
            return not text
        firstMatch = bool(text) and pattern[0] in {text[0], "."}
        if len(pattern) >= 2 and pattern[1] == "*":
            return self.isMatch(text, pattern[2:]) or firstMatch and self.isMatch(text[1:], pattern)
        else:
            return firstMatch and self.isMatch(text[1:], pattern[1:])








