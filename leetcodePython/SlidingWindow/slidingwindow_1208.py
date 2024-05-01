class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        ans = left = right = 0
        for right, ch in enumerate(s):
            maxCost -= abs(ord(ch) - ord(t[right]))
            if maxCost < 0:
                maxCost += abs(ord(s[left]) - ord(t[left]))
                left += 1
        return right - left + 1