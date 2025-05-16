from collections import Counter
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = {c: 0 for c in 'abc'}
        left = 0
        ans = 0
        for right, ch in enumerate(s):
            count[ch] += 1
            while all(count.values()):
                count[s[left]] -= 1
                left += 1
            ans += left
        return ans