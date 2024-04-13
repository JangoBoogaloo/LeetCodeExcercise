from collections import Counter
class SolutionRecursion:
    def longestSubstring(self, s: str, k: int) -> int:
        freq = Counter(s)
        ans = 0
        for c in freq:
            if freq[c] < k:
                for substr in s.split(c):
                    if len(substr) >= k:
                        ans = max(ans, self.longestSubstring(substr, k))
                return ans
        return len(s)