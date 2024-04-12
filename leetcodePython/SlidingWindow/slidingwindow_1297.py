from collections import Counter

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        substr_freq = Counter(s[i:i + minSize] for i in range(len(s) - minSize + 1))
        ans = 0
        for substr in substr_freq:
            if len(set(substr)) <= maxLetters:
                ans = max(ans, substr_freq[substr])
        return ans