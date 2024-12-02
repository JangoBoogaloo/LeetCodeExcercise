class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = {c: 0 for c in 'abc'}
        zeros = len(count)
        left = 0
        ans = 0
        for right, ch in enumerate(s):
            count[ch] += 1
            if count[ch] == 1:
                zeros -= 1
            while zeros == 0:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    zeros += 1
                left += 1
            ans += left
        return ans
