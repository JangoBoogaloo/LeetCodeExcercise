from collections import Counter


class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        count = Counter()
        ans = left = 0
        for right, ch in enumerate(s):
            count[ch] += 1
            while count[ch] > 1:
                count[s[left]] -= 1
                left += 1
            ans += right - left + 1
        return ans
