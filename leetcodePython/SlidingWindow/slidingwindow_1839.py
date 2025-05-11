class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        seen = set()
        lo, longest = -1, 0
        for hi, c in enumerate(word):
            if hi > 0 and c < word[hi - 1]:
                seen = set()
                lo = hi - 1
            seen.add(c)
            if len(seen) == 5:
                longest = max(longest, hi - lo)
        return longest